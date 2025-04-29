from fastapi import APIRouter, Depends, HTTPException, Security
from typing import Annotated
from app import schemas, models
from app.Routes import deps
from sqlalchemy.orm import Session
from app.core import config
from datetime import timedelta
from app.schemas.user import UserOutDB
from pydantic import BaseModel
from fastapi.security import (
    OAuth2PasswordBearer,
    OAuth2PasswordRequestForm,
    SecurityScopes,
)
from app.core.password import get_password_hash, get_salt
from app.core.config import settings
from app.crud.crud_user import crud_user
from app.crud.crud_user_role import user_role as crud_user_role
from app.crud.crud_unit import unit as crud_unit
from app.crud.crud_user_permission import user_permission as crud_user_permission
from app.crud.crud_role import role as crud_role
from app.core.jwt import create_access_token
import uuid

class AuthModel(BaseModel):
    username: str
    password: str

router = APIRouter(tags=['auth'])

@router.post("/login")
async def login_for_access_token(
    auth: AuthModel,
    db: Annotated[Session, Depends(deps.get_db)]
):
    print(f"[DEBUG] Attempting login for username: {auth.username}")
    
    user = crud_user.authenticate(db=db, username=auth.username, password=auth.password)
    if not user:
        print(f"[DEBUG] Authentication failed for username: {auth.username}")
        raise HTTPException(
            status_code=400,
            detail="Incorrect username or password"
        )
    
    print(f"[DEBUG] User authenticated successfully: {user.username}")
    
    if not user.is_active:
        print(f"[DEBUG] User {user.username} is not active")
        raise HTTPException(
            status_code=400,
            detail="User is not active"
        )
    
    access_token_expires = timedelta(minutes=config.settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    # Get role id by user id
    role_user_id = crud_user_role.get_by_user_id(user_id=user.id, db=db)
    if not role_user_id:
        print(f"[DEBUG] User {user.username} has no role assigned")
        raise HTTPException(
            status_code=400,
            detail="User has no role assigned"
        )
    print(f"[DEBUG] User {user.username} has role: {role_user_id}")
    
    # Get role names
    role_names = []
    for role in role_user_id:
        role_obj = crud_role.get(db=db, id=role.role_id)
        if role_obj:
            role_names.append(role_obj.name)
    print(f"[DEBUG] User {user.username} has roles: {role_names}")
    
    # Get Unit id of User
    unit = crud_unit.get_by_user_id(user_id=user.id, db=db)
    if not unit:
        print(f"[DEBUG] User {user.username} has no unit assigned")
        raise HTTPException(
            status_code=400,
            detail="User has no unit assigned"
        )
    print(f"[DEBUG] User {user.username} belongs to unit: {unit.id}")
    
    # Get Permission id by user id
    permission = crud_user_permission.get_by_user_id(user_id=user.id, db=db)
    print(f"[DEBUG] User {user.username} has permissions: {permission}")
    
    # Create access token
    access_token = create_access_token(
        subject={
            "id": str(user.id),
            "username": user.username,
            "unit_id": str(unit.id),
            "role": role_names,
            "permission": permission
        },
        expires_delta=access_token_expires,
    )
    print(f"[DEBUG] Generated access token for user: {user.username}")
    
    return {"access_token": access_token, "token_type": "bearer"}

# verify token to check valid user
@router.post("/verify_token", response_model=UserOutDB)
async def verify_token(current_user=Security(deps.get_current_active_user, scopes=[])):
    print(f"[DEBUG] Verifying token for user: {current_user.username}")
    print(f"[DEBUG] User ID: {current_user.id}")
    print(f"[DEBUG] User is active: {current_user.is_active}")
    return current_user

@router.post("/register", response_model=schemas.user.User)
def register(
    *,
    db: Session = Depends(deps.get_db),
    user_in: schemas.user.UserCreate,
) -> any:
    """
    Register new user.
    """
    print(f"[DEBUG] Registering user with username: {user_in.username}")
    
    # Kiểm tra username đã tồn tại chưa
    user = crud_user.get_by_username(db, username=user_in.username)
    if user:
        print(f"[DEBUG] Username {user_in.username} already exists")
        raise HTTPException(
            status_code=400,
            detail="Username already registered",
        )
    
    # Kiểm tra unit_id có tồn tại và hợp lệ không
    try:
        unit_id = uuid.UUID(user_in.unit_id)
        print(f"[DEBUG] Unit ID is valid: {unit_id}")
    except ValueError:
        print(f"[DEBUG] Invalid unit_id format: {user_in.unit_id}")
        raise HTTPException(
            status_code=400,
            detail="Invalid unit_id format"
        )
    
    unit = crud_unit.get(db=db, id=unit_id)
    if not unit:
        print(f"[DEBUG] Unit not found with ID: {unit_id}")
        raise HTTPException(
            status_code=404,
            detail="Unit not found"
        )
    
    # Tạo salt mới cho user
    salt = get_salt()
    print(f"[DEBUG] Generated salt: {salt}")
    
    # Tạo user mới với password đã được mã hóa và is_active = False
    user_in_db = schemas.user.UserCreateInDB(
        **user_in.dict(),
        salt=salt,
        is_active=False
    )
    
    # Mã hóa password với salt
    print(f"[DEBUG] Password to hash: {user_in.password}")
    user_in_db.password = get_password_hash(password=user_in.password, salt=salt)
    print(f"[DEBUG] Hashed password: {user_in_db.password}")
    
    # Tạo user
    user = crud_user.create(db, obj_in=user_in_db)
    print(f"[DEBUG] Created user with ID: {user.id}")
    
    # Gán role mặc định cho user mới (nếu cần)
    default_role = crud_role.get_by_name(db, name="admin")
    if default_role:
        print(f"[DEBUG] Assigning default role: {default_role.name}")
        user_role = schemas.user_role.UserRoleCreate(
            user_id=user.id,
            role_id=default_role.id
        )
        crud_user_role.create(db, obj_in=user_role)
    
    return user
