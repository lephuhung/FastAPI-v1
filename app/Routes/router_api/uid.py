from fastapi import APIRouter, Body, Depends, HTTPException, Security
from typing import Annotated
from app.schemas.uid import uidCreate, uidUpdate
from app.crud import crud_uid
from app.Routes import deps
from sqlalchemy.orm import Session
router = APIRouter(prefix="/uid", tags=["UID"])

@router.get("")
async def get():
    return {'123':'123'}

@router.post("/create")
async def create(uid: uidCreate, db: Session = Depends(deps.get_db)):
    return crud_uid.create(db=db, obj_in=uid)

@router.put("/update/{uid}")
async def update():
    return {'123':'123'}

@router.delete("/{uid}")
async def delete(uid: Annotated[int, 0]):
    return {'123':uid}
