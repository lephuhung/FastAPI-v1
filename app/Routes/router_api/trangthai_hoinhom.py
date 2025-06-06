from fastapi import APIRouter, Body, Depends, HTTPException, Security
from typing import Annotated
from app.schemas.trangthai_hoinhom import trangthai_hoinhomcreate
from app.crud.crud_trangthai_hoinhom import crud_trangthai_hoinhom
from app.Routes import deps
from sqlalchemy.orm import Session
router = APIRouter(prefix="/trangthai-hoinhom", tags=["Trạng thái của hội nhóm"])

@router.get("/get-all-by-uid/{uid_id}")
async def get_all_by_uid( uid_id: str, db: Session = Depends(deps.get_db)):
    return crud_trangthai_hoinhom.get_all_trangthai_hoinhom(uid_id, db)
@router.post("/create")
async def create(trangthai_hoinhom: trangthai_hoinhomcreate, db: Session = Depends(deps.get_db)):
    return crud_trangthai_hoinhom.create(db=db, obj_in=trangthai_hoinhom)

