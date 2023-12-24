from fastapi import APIRouter, Body, Depends, HTTPException, Security
from typing import Annotated
from app.schemas.quantrivien import quantriviencreate, quantrivienupdate
from app.crud.crud_quantrivien import crud_quantrivien
from app.Routes import deps
from sqlalchemy.orm import Session
router = APIRouter(prefix="/quantrivien", tags=["Quản trị viên"])


# @router.get('/')
# async def getAll(db: Session = Depends(deps.get_db)):
#     return crud_quantrivien.get_multi(db)

@router.post("/create")
async def create(quantrivien: quantriviencreate, db: Session = Depends(deps.get_db)):
    return crud_quantrivien.create(db=db, obj_in=quantrivien)

