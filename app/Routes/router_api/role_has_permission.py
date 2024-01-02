from fastapi import APIRouter, Body, Depends, HTTPException, Security
from typing import Annotated
from app.Routes import deps
from sqlalchemy.orm import Session
from pydantic import UUID4
from app import crud
from fastapi import Form

router = APIRouter(prefix="/role-has-permission", tags=["Role has Permission"])

# @router.get("/get-all-by-roleid")
# async def get():
#     return {'123':'123'}

@router.post("/get-all-by-roleid")
async def get_all_permission_by_role(uid: Annotated[UUID4, Form()] ,db: Session = Depends(deps.get_db)):
    return crud.CrudRole_has_Permission.get_all_permission_in_role(role_id=uid, db=db)

