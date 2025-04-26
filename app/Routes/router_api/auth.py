from fastapi import APIRouter, Depends, HTTPException, Security
from typing import Annotated
from app import schemas, models
from app.Routes import deps
from sqlalchemy.orm import Session
from app.core import security, config
from datetime import timedelta
from app.schemas.user import UserOutDB
from pydantic import BaseModel
from fastapi.security import (
    OAuth2PasswordBearer,
    OAuth2PasswordRequestForm,
    SecurityScopes,
)
from app.core.security import get_password_hash, get_salt
from app.core.config import settings
from app.crud.crud_user import crud_user
from app.crud.crud_user_role import user_role as crud_user_role
from app.crud.crud_unit import unit as crud_unit
from app.crud.crud_user_permission import user_permission as crud_user_permission
from app.crud.crud_role import role as crud_role

class AuthModel(BaseModel):
    username: str
    password: str
router = APIRouter(tags=['auth'])
# login
@router.post("/login" )
async def login_for_access_token(
    auth: AuthModel,
    db: Annotated[Session, Depends(deps.get_db)]
):
    user = security.authenticate_user(auth.username,auth.password, db=db)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=config.settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    # Get role id by user id
    role_user_id = crud_user_role.get_by_user_id(user_id=user.id, db=db)
    # Get Unit id of User
    unit = crud_unit.get_by_user_id(user_id=user.id, db=db)
    # Get Permission id by user id
    permission = crud_user_permission.get_by_user_id(user_id=user.id, db=db)
    # Create access token
    access_token = security.create_access_token(
        subject={"id": str(user.id), "username": user.username, "unit_id": str(unit.unit_id) if unit else None, "role": [f'{role_user_id.role_id}'], "permission": permission},
        expires_delta=access_token_expires,
    )
    return {"access_token": access_token, "token_type": "bearer"}

# verify token to check valid user
@router.post("/verify_token", response_model=UserOutDB)
async def verify_token(current_user=Security(deps.get_current_active_user, scopes=[])):
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
    user = crud_user.get_by_username(db, username=user_in.username)
    if user:
        raise HTTPException(
            status_code=400,
            detail="Username already registered",
        )
    
    # Tạo salt mới cho user
    salt = get_salt()
    
    # Tạo user mới với password đã được mã hóa và is_active = False
    user_in.salt = salt
    user_in.password = get_password_hash(user_in.password + salt)
    user_in.is_active = False
    
    user = crud_user.create(db, obj_in=user_in)
    
    # Gán role mặc định cho user mới (nếu cần)
    default_role = crud_role.get_by_name(db, name="admin")
    if default_role:
        user_role = schemas.user_role.UserRoleCreate(
            user_id=user.id,
            role_id=default_role.id
        )
        crud_user_role.create(db, obj_in=user_role)
    
    return user
