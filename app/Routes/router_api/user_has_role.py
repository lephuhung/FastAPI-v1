from fastapi import APIRouter, Body, Depends, HTTPException, Security
from typing import Annotated
from sqlalchemy.orm import Session
from app.Routes import deps
from pydantic import UUID4
from app.schemas.user_has_role import User_has_RoleCreate

from app import crud
router = APIRouter(prefix="/user-has-role", tags=["User has Role"])

@router.get("/get-role-by-user/{user_id}")
async def get(user_id: UUID4, db: Session = Depends(deps.get_db)):
    user_has_role = crud.crud_user_has_role.get_user_has_role_by_userid(user_id=user_id, db=db)
    return user_has_role

@router.post("/add-user-has-role")
async def post(user_id: UUID4, role_id : UUID4 ,db: Session = Depends(deps.get_db)):
    obj = User_has_RoleCreate(user_id=user_id, role_id=role_id)
    crud.crud_user_has_role.create(obj_in=obj, db=db)
    return {"message":"success"}


@router.delete("/delete-role-user")
async def delete(user_id: UUID4, role_id: UUID4, db: Session = Depends(deps.get_db)):
    user_role= crud.crud_user_has_role.get_user_role(user_id=user_id, role_id=role_id, db=db)
    return  {"message":"success"}
