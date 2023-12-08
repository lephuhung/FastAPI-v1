from fastapi import APIRouter, Body, Depends, HTTPException, Security
from typing import Annotated
from app.Routes import deps
from sqlalchemy.orm import Session
from pydantic import UUID4
from app import crud
from app.schemas.doituong import doituongcreate
from fastapi import Form

router = APIRouter(prefix="/doituong", tags=["user"])

@router.post("/create")
async def create_doituong( doituong: doituongcreate,db: Session = Depends(deps.get_db)):
    return crud.crud_doituong.create(db=db, obj_in=doituong)