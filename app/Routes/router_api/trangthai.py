from fastapi import APIRouter, Body, Depends, HTTPException, Security
from typing import Annotated
from app.schemas.trangthai import trangthaicreate, trangthaiupdate
from app.crud.crud_trangthai import crud_trangthai
from app.Routes import deps
from sqlalchemy.orm import Session
router = APIRouter(prefix="/trangthai", tags=["Trạng thái"])

@router.get('/')
async def getAll(db: Session = Depends(deps.get_db)):
    return crud_trangthai.get_multi(db)
@router.post("/create")
async def create(trangthai: trangthaicreate, db: Session = Depends(deps.get_db)):
    return crud_trangthai.create(db=db, obj_in=trangthai)

