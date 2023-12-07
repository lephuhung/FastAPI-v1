from typing import Annotated
from app.Routes import deps
from sqlalchemy.orm import Session
from pydantic import UUID4
from app import crud
from fastapi import APIRouter, Depends
from fastapi import Form

router = APIRouter(prefix="/user-has-permission", tags=["rhp"])

# @router.get("/get-all-by-roleid")
# async def get():
#     return {'123':'123'}

@router.post("/get-all-by-userid")
async def get_all_permission_by_userid(uid: Annotated[UUID4, Form()] ,db: Session = Depends(deps.get_db)):
    return crud.crud_user_has_permission.get_permission_user(user_id=uid, db=db)

@router.put("/{uid}")
async def update():
    return {'123':'123'}

@router.delete("/{uid}")
async def delete(uid: Annotated[int, 0]):
    return {'123':uid}