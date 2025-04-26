from fastapi import APIRouter, Body, Depends, HTTPException, Security, Depends
from typing import Annotated, List
from app.Routes import deps
from sqlalchemy.orm import Session
from app.core.config import settings
from app import crud, schemas, models
from datetime import datetime
from app.core.security import get_salt, get_password_hash
from fastapi.security import (
    OAuth2PasswordBearer,
    OAuth2PasswordRequestForm,
    SecurityScopes,
)
from app.schemas.user import UserCreate, UserUpdate, User
from pydantic import BaseModel
import uuid

class UserCreateForm(BaseModel):
    username: str
    password: str
    unit_id: str

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=List[User])
def get_users(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user = Security(deps.get_current_superadmin, scopes=[]),
):
    """
    Get all users.
    """
    users = crud.user.get_multi(db, skip=skip, limit=limit)
    return users

@router.post("/", response_model=User)
def create_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: UserCreate,
    current_user = Security(deps.get_current_superadmin, scopes=[]),
):
    """
    Create new user.
    """
    user_obj = crud.user.create(db=db, obj_in=user_in)
    return user_obj

@router.put("/{id}", response_model=User)
def update_user(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
    user_in: UserUpdate,
    current_user = Security(deps.get_current_superadmin, scopes=[]),
):
    """
    Update user.
    """
    user_obj = crud.user.get(db=db, id=id)
    if not user_obj:
        raise HTTPException(status_code=404, detail="User not found")
    user_obj = crud.user.update(db=db, db_obj=user_obj, obj_in=user_in)
    return user_obj

@router.get("/{id}", response_model=User)
def get_user(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
    current_user = Security(deps.get_current_superadmin, scopes=[]),
):
    """
    Get user by ID.
    """
    user_obj = crud.user.get(db=db, id=id)
    if not user_obj:
        raise HTTPException(status_code=404, detail="User not found")
    return user_obj

@router.delete("/{id}", response_model=User)
def delete_user(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
    current_user = Security(deps.get_current_superadmin, scopes=[]),
):
    """
    Delete user.
    """
    user_obj = crud.user.get(db=db, id=id)
    if not user_obj:
        raise HTTPException(status_code=404, detail="User not found")
    user_obj = crud.user.remove(db=db, id=id)
    return user_obj

@router.put("/{id}/activate", response_model=User)
def activate_user(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
    current_user = Security(deps.get_current_superadmin, scopes=[]),
):
    """
    Activate user.
    """
    user_obj = crud.user.get(db=db, id=id)
    if not user_obj:
        raise HTTPException(status_code=404, detail="User not found")
    user_in = UserUpdate(is_active=True)
    user_obj = crud.user.update(db=db, db_obj=user_obj, obj_in=user_in)
    return user_obj

@router.put("/{id}/deactivate", response_model=User)
def deactivate_user(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
    current_user = Security(deps.get_current_superadmin, scopes=[]),
):
    """
    Deactivate user.
    """
    user_obj = crud.user.get(db=db, id=id)
    if not user_obj:
        raise HTTPException(status_code=404, detail="User not found")
    user_in = UserUpdate(is_active=False)
    user_obj = crud.user.update(db=db, db_obj=user_obj, obj_in=user_in)
    return user_obj

# Migrate accounts super admin
@router.get("")
async def get(db: Session = Depends(deps.get_db) ):
    user = crud.user.get_by_username(db=db, username=settings.FIRST_SUPER_ADMIN_ACCOUNT_NAME)
    salt= get_salt()
    if user is None:
        model_user_admin= schemas.user.UserCreate(
            username= settings.FIRST_SUPER_ADMIN_ACCOUNT_NAME,
            is_active= True,
            salt= salt,
            password= get_password_hash(f'lph77{salt}'),
        )
        crud.user.create(db, obj_in=model_user_admin) 
        return model_user_admin

# Create new User
@router.post("/create")
async def post(
    user_data: UserCreateForm,
    db: Session = Depends(deps.get_db),
    current_user: models.user.User = Security(deps.get_current_user, scopes=['5', "7"])
    ):
    # Kiểm tra username đã tồn tại chưa
    user = crud.user.get_by_username(db=db, username=user_data.username)
    if user:
        raise HTTPException(
            status_code=400,
            detail="Username Exist"
        )

    # Kiểm tra unit_id có tồn tại không
    unit = crud.unit.get(db=db, id=user_data.unit_id)
    if not unit:
        raise HTTPException(
            status_code=404,
            detail="Unit not found"
        )

    # Tạo salt mới
    salt = get_salt()
    
    # Tạo user mới
    model_user = schemas.user.UserCreate(
        username=user_data.username,
        is_active=False,
        salt=salt,
        password=get_password_hash(f'{user_data.password}{salt}'),
        unit_id=user_data.unit_id
    )
    
    # Lưu user vào database
    user = crud.user.create(db, obj_in=model_user)
    return user

# @router.get("/get_all")
# async def get_all (
#     db: Session = Depends(deps.get_db),
#     current_user: models.user.User = Security(deps.get_current_active_user(), scopes=[])
# ):
#     id = current_user.get('id')
#     Users= crud.crud_user.get_all()