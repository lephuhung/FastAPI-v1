from fastapi import APIRouter, Body, Depends, HTTPException, Security
from typing import Annotated
from app.Routes import deps
from sqlalchemy.orm import Session
from pydantic import UUID4
from app import crud
from app.schemas.model_has_tags import model_has_tagscreate
from fastapi import Form

router = APIRouter(prefix="/model_has_tags", tags=["Model has tags"])

@router.get("/get-tags-by-model-id/{model_id}")
async def get(model_id:str, db: Session = Depends(deps.get_db)):
    return crud.crud_model_has_tags.get_tags_by_model_id(model_id=model_id, db= db)

@router.post("/create_tags_model")
async def create_tags_model(model_id: Annotated[str, Form()], tags_id_list: Annotated[list[int], Form()] ,db: Session = Depends(deps.get_db)):
    for item in tags_id_list:
        model_has_tags_instance = model_has_tagscreate(model_id= model_id, tags_id= item)
        crud.crud_model_has_tags.create(db= db,  obj_in=model_has_tags_instance)
    return {"success": True}

