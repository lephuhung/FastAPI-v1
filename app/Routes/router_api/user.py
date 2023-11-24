from fastapi import APIRouter, Body, Depends, HTTPException, Security, Depends
from typing import Annotated
from app.Routes import deps
from sqlalchemy.orm import Session
from app.core.config import settings
from app import crud, schemas
from datetime import datetime
from app.core.sercurity import get_salt, get_password_hash
router = APIRouter(prefix="/user", tags=["user"])

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

@router.post("")
async def post():
    return {'123':'123'}

@router.put("/{uid}")
async def update():
    return {'123':'123'}

@router.delete("/{uid}")
async def delete(uid: Annotated[int, 0]):
    return {'123':uid}
