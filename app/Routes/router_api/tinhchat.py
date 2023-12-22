from fastapi import APIRouter, Body, Depends, HTTPException, Security
from typing import Annotated
from app.schemas.tinhchat import tinhchatcreate, tinhchatupdate
from app.crud.crud_tinhchat import crud_tinhchat
from app.Routes import deps
from sqlalchemy.orm import Session
router = APIRouter(prefix="/tinhchat", tags=["tinchat"])


@router.post("/create")
async def create(tinhchat: tinhchatcreate, db: Session = Depends(deps.get_db)):
    return crud_tinhchat.create(db=db, obj_in=tinhchat)

@router.put("/update/{uid}")
async def update():
    return {'123':'123'}

@router.delete("/{uid}")
async def delete(uid: Annotated[int, 0]):
    return {'123':uid}