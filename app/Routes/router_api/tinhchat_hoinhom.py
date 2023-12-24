from fastapi import APIRouter, Body, Depends, HTTPException, Security
from typing import Annotated
from app.Routes import deps
from sqlalchemy.orm import Session
from pydantic import UUID4
from app import crud
from app.schemas.tinhchat_hoinhom import tinhchat_hoinhomcreate
from fastapi import Form

router = APIRouter(prefix="/tinhchat-hoinhom", tags=["Tính chất của hội nhóm"])

@router.get("/get/{model_id}")
async def get(model_id:str, db: Session = Depends(deps.get_db)):
    return crud.crud_model_has_tags.get_tags_by_model_id(model_id=model_id, db= db)

@router.post("/create")
async def create_tags_model(tinhchat_hoinhom: tinhchat_hoinhomcreate ,db: Session = Depends(deps.get_db)):
    data = crud.crud_tinhchat_hoinhom.create(db=db, obj_in=tinhchat_hoinhom)
    return {"success": True, "data": data}