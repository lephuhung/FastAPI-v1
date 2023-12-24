from fastapi import APIRouter, Body, Depends, HTTPException, Security
from typing import Annotated
from app.schemas.permission import PermissionCreate, PermissionUpdate
from app.crud.crud_permission import CURD_Permission
from app.Routes import deps
from sqlalchemy.orm import Session
router = APIRouter(prefix="/permission", tags=["Permission"])

@router.get('/')
async def getAll(db: Session = Depends(deps.get_db)):
    return CURD_Permission.get_multi(db)

@router.post("/create")
async def create(permissioncreate: PermissionCreate, db: Session = Depends(deps.get_db)):
    return CURD_Permission.create(db=db, obj_in=permissioncreate)

