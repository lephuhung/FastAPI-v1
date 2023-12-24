from fastapi import APIRouter, Body, Depends, HTTPException, Security
from typing import Annotated
from app.schemas.tinhchat import tinhchatcreate, tinhchatupdate
from app.crud.crud_tinhchat import crud_tinhchat
from app.Routes import deps
from sqlalchemy.orm import Session
router = APIRouter(prefix="/tinhchat", tags=["Tính chất"])

@router.get('/')
async def getAll(db: Session = Depends(deps.get_db)):
    return crud_tinhchat.get_multi(db)

@router.post("/create")
async def create(tinhchat: tinhchatcreate, db: Session = Depends(deps.get_db)):
    return crud_tinhchat.create(db=db, obj_in=tinhchat)
