from fastapi import APIRouter, Body, Depends, HTTPException, Security
from typing import Annotated
from app.schemas.vaiao import vaiaocreate
from app.crud.crud_vaiao import crud_vaiao
from app.Routes import deps
from sqlalchemy.orm import Session
router = APIRouter(prefix="/vaiao", tags=["Vai ảo"])


@router.post("/create")
async def create(vaiao: vaiaocreate, db: Session = Depends(deps.get_db)):
    return crud_vaiao.create(db=db, obj_in=vaiao)

@router.get("/")
async def getall(db: Session= Depends(deps.get_db)):
    return crud_vaiao.get_all(db=db)
