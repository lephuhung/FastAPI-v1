from fastapi import APIRouter, Body, Depends, HTTPException, Security
from typing import Annotated
from app.schemas.donvi import DonviCreate, DonviUpdate
from app.crud.crud_donvi import crud_donvi
from app.Routes import deps
from pydantic import UUID4
from sqlalchemy.orm import Session
router = APIRouter(prefix="/donvi", tags=["Đơn vị"])


@router.get('/getAll')
async def getAll(db: Session = Depends(deps.get_db)):
    return crud_donvi.get_multi(db)
@router.get('/get/{id}')
async def get(id: UUID4, db: Session = Depends(deps.get_db)):
    return crud_donvi.get_donvi_by_id(db=db, id=id)
    
@router.post("/create")
async def create(donvi: DonviCreate, db: Session = Depends(deps.get_db)):
    return crud_donvi.create(db=db, obj_in=donvi)

