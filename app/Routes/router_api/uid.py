from fastapi import APIRouter, Body, Depends, HTTPException, Security
from typing import Annotated
from app.schemas.uid import uidCreate, uidUpdate
from app.crud import crud_uid
from app.Routes import deps
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
router = APIRouter(prefix="/uid", tags=["UID"])

@router.get("/get-last/{id}")
async def getlast(id: str, db: Session = Depends(deps.get_db)):
    data = crud_uid.get_last_uid_by_id( id=id, db=db)
    return data

@router.get("/get-history/{uid_uid}")
async def gethistory(uid_uid: str, db: Session = Depends(deps.get_db)):
    data = crud_uid.get_all_by_uid( uid_uid=uid_uid, db=db)
    return data

@router.post("/create")
async def create(uid: uidCreate, db: Session = Depends(deps.get_db)):
    return crud_uid.create(db=db, obj_in=uid)

@router.put("/update/{id}")
async def update(id: int, uid_data: uidUpdate  ,db: Session = Depends(deps.get_db)):
    uid_has_update = crud_uid.get_uid_by_id(id= id, db=db)
    data = crud_uid.update(obj_in=uid_data, db_obj=uid_has_update, db=db)
    return data

@router.get("/get-facebook")
async def get_facebook(type_id:int =1, db: Session = Depends(deps.get_db), current_user=Security(deps.get_current_active_user, scopes=[])):
    facebook_data = crud_uid.get_all_by_type_id(type_id=type_id, db=db)
    return facebook_data

@router.get("/get-groups")
async def get_groups(type_id:int =0, db: Session = Depends(deps.get_db), current_user=Security(deps.get_current_active_user, scopes=[])):
    facebook_data = crud_uid.get_all_by_type_id(type_id=type_id, db=db)
    return facebook_data

@router.get("/get-pages")
async def get_groups(type_id:int =2, db: Session = Depends(deps.get_db), current_user=Security(deps.get_current_active_user, scopes=[])):
    facebook_data = crud_uid.get_all_by_type_id(type_id=type_id, db=db)
    return facebook_data