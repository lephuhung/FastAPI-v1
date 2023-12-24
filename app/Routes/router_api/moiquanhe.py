from fastapi import APIRouter, Body, Depends, HTTPException, Security
from typing import Annotated
from app.schemas.moiquanhe import moiquanhecreate, moiquanheupdate
from app.crud.crud_moiquanhe import crud_moiquanhe
from app.Routes import deps
from sqlalchemy.orm import Session
router = APIRouter(prefix="/moiquanhe", tags=["Mối quan hệ"])

@router.get('/')
async def getAll(db: Session = Depends(deps.get_db)):
    return crud_moiquanhe.get_multi(db)

@router.post("/create")
async def create(moiquanhe: moiquanhecreate, db: Session = Depends(deps.get_db)):
    return crud_moiquanhe.create(db=db, obj_in=moiquanhe)

