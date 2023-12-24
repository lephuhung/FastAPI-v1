from fastapi import APIRouter, Body, Depends, HTTPException, Security
from typing import Annotated
from app.Routes import deps
from sqlalchemy.orm import Session
from pydantic import UUID4
from app import crud
from app.schemas.doituong_uid import doituong_uidcreate
from fastapi import Form

router = APIRouter(prefix="/doituong-uid", tags=["UID liên quan đối tượng"])

@router.get("/get/{model_id}")
async def get(model_id:str, db: Session = Depends(deps.get_db)):
    return crud.crud_model_has_tags.get_tags_by_model_id(model_id=model_id, db= db)

@router.post("/create")
async def create_tags_model(doituong_uid: doituong_uidcreate ,db: Session = Depends(deps.get_db)):
    data = crud.crud_doituong_uid.create(db=db, obj_in=doituong_uid)
    return {"success": True, "data": data}