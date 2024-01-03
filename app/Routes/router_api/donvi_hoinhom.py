from fastapi import APIRouter, Body, Depends, HTTPException, Security
from typing import Annotated
from app.Routes import deps
from sqlalchemy.orm import Session
from pydantic import UUID4
from app import crud
from app.schemas.donvi_hoinhom import hoinhom_donvicreate
from fastapi import Form

router = APIRouter(prefix="/hoinhom-donvi", tags=[" Hội nhóm thuộc đơn vị"])

@router.get("/get-by-donvi/{donvi_id}")
async def get(donvi_id:str, db: Session = Depends(deps.get_db)):
    return crud.crud_donvihoinhom.get_hoinhom_by_donvi(donvi_id=donvi_id, db=db)

@router.get("/get-all-by-admin")
async def get_all(db: Session = Depends(deps.get_db), current_user=Security(deps.get_current_active_user, scopes=['admin'])):
    return crud.crud_donvihoinhom.get_all_hoinhom(db)

@router.post("/create")
async def create_tags_model(hoinhom_donvi: hoinhom_donvicreate ,db: Session = Depends(deps.get_db)):
    data = crud.crud_donvihoinhom.create(db=db, obj_in=hoinhom_donvi)
    return {"success": True, "data": data}