from fastapi import APIRouter, Body, Depends, HTTPException, Security
from typing import Annotated
from app.schemas.type import typecreate
from app.crud.crud_type import crud_type
from app.Routes import deps
from sqlalchemy.orm import Session
router = APIRouter(prefix="/type", tags=["type"])

@router.get('/')
async def getAll(db: Session = Depends(deps.get_db)):
    return crud_type.get_multi(db)

    
@router.post("/create")
async def create(typedata: typecreate, db: Session = Depends(deps.get_db)):
    return crud_type.create(db=db, obj_in=typedata)

