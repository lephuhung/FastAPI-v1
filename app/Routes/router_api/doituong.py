from fastapi import APIRouter, Body, Depends, HTTPException, Security
from typing import Annotated
from app.Routes import deps
from sqlalchemy.orm import Session
from pydantic import UUID4
from app import crud
from app.models.doituong import Doituong
from app.schemas.doituong import doituongcreate, doituongupdate
from app.schemas.doituong_donvi import doituong_donvicreate
from fastapi import Form

router = APIRouter(prefix="/doituong", tags=["Đối tượng"])
# get all doituong
@router.get('')
async def get_all(db: Session = Depends(deps.get_db), current_user=Security(deps.get_current_active_user, scopes=[])):
    data= crud.crud_doituong.get_multi(db)
    return data
# create a new Doituong
@router.post("/create")
async def create_doituong( doituong: doituongcreate,db: Session = Depends(deps.get_db)):
    doituongoutDB = crud.crud_doituong.create(db=db, obj_in=doituong)
    return doituongoutDB

# update not work yet
@router.post("/update/{doituong_id}")
async def update_doituong(doituong_id: UUID4, doituonginupdate: doituongupdate, db: Session = Depends(deps.get_db)):
    doituong = crud.crud_doituong.get_doituong_by_id(doituong_id=doituong_id, db=db)
    return crud.crud_doituong.update(db=db, db_obj=doituong, obj_in=doituonginupdate)
