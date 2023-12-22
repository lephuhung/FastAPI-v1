from fastapi import APIRouter, Body, Depends, HTTPException, Security
from typing import Annotated
from app.schemas.ctnv import ctnvcreate, ctnvupdate
from app.crud.crud_ctnv import crud_ctnv
from app.Routes import deps
from sqlalchemy.orm import Session
router = APIRouter(prefix="/ctnv", tags=["ctnv"])


@router.post("/create")
async def create(ctnv: ctnvcreate, db: Session = Depends(deps.get_db)):
    return crud_ctnv.create(db= db, obj_in = ctnv)

