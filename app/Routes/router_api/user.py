from fastapi import APIRouter, Body, Depends, HTTPException, Security, Depends
from typing import Annotated
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

router = APIRouter(prefix="/user", tags=["user"])
# Migrate accounts super admin
@router.get("")
async def get(db: Session = Depends(deps.get_db) ):
    user = crud.crud_user.get_by_name(db=db, username=settings.FIRST_SUPER_ADMIN_ACCOUNT_NAME)
    salt= get_salt()
    if user is None:
        model_user_admin= schemas.user.UserCreate(
            username= settings.FIRST_SUPER_ADMIN_ACCOUNT_NAME,
            active= True,
            salt= salt,
            password= get_password_hash(f'lph77{salt}'),
        )
        crud.crud_user.create(db, obj_in=model_user_admin) 
        return model_user_admin

# Create new User
@router.post("/create")
async def post(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], 
    db: Session = Depends(deps.get_db),
    current_user: models.user.User = Security(deps.get_current_user, scopes=['5', "7"])
    ):
    user = crud.crud_user.get_by_name(db=db, username=form_data.username)
    salt= get_salt()
    if user is None:
        model_user= schemas.user.UserCreate(
            username= form_data.username,
            active= False,
            salt= salt,
            password= get_password_hash(f'{form_data.password}{salt}'),
        )
        crud.crud_user.create(db, obj_in=model_user) 
        return model_user
    else:
        raise HTTPException(
            status_code=400,
            detail="Username Exist"
        )

# @router.get("/get_all")
# async def get_all (
#     db: Session = Depends(deps.get_db),
#     current_user: models.user.User = Security(deps.get_current_active_user(), scopes=[])
# ):
#     id = current_user.get('id')
#     Users= crud.crud_user.get_all()