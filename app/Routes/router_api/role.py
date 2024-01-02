from fastapi import APIRouter, Body, Depends, HTTPException, Security
from typing import Annotated
from app.schemas.role import RoleCreate, RoleUpdate
from app.crud.crud_role import CURD_Role
from app.Routes import deps
from sqlalchemy.orm import Session
router = APIRouter(prefix="/role", tags=["Role"])

@router.get('/getAll')
async def getAll(db: Session = Depends(deps.get_db)):
    return CURD_Role.get_multi(db)

@router.post("/create")
async def create(role: RoleCreate, db: Session = Depends(deps.get_db)):
    return CURD_Role.create(db=db, obj_in=role)

