from fastapi import APIRouter, Body, Depends, HTTPException, Security
from typing import Annotated
from app.schemas.color import colorcreate, colorupdate
from app.crud.crud_color import crud_color
from app.Routes import deps
from sqlalchemy.orm import Session
router = APIRouter(prefix="/color", tags=["color"])


@router.post("/create")
async def create(color: colorcreate, db: Session = Depends(deps.get_db)):
    return crud_color.create(db=db, obj_in=color)

