from fastapi import APIRouter, Body, Depends, HTTPException, Security
from typing import Annotated
from app.schemas.trichtin import trichtinCreate, trichtinUpdate
from app.crud.crud_trichtin import crud_trichtin
from app.Routes import deps
from sqlalchemy.orm import Session
router = APIRouter(prefix="/trichtin", tags=["Trích tin"])


@router.post("/create")
async def create(trichtin: trichtinCreate, db: Session = Depends(deps.get_db)):
    return crud_trichtin.create(db=db, obj_in=trichtin)

@router.put("/update/{uid}")
async def update():
    return {'123':'123'}

@router.delete("/{uid}")
async def delete(uid: Annotated[int, 0]):
    return {'123':uid}