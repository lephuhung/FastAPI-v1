from fastapi import APIRouter, Body, Depends, HTTPException, Security
from typing import Annotated
from app.schemas.trichtin import trichtinCreate, trichtinUpdate, trichtin
from app.crud.crud_trichtin import crud_trichtin
from app.Routes import deps
from sqlalchemy.orm import Session
router = APIRouter(prefix="/trichtin", tags=["Trích tin"])


@router.post("/create")
async def create(trichtin: trichtin, db: Session = Depends(deps.get_db), current_user=Security(deps.get_current_active_user, scopes=[])):
    A_dict = trichtin.dict()  # Convert A to a dictionary
    A_dict['user_id'] = current_user.id  # Add 'user_id' field to the dictionary
    A_create = trichtinCreate(**A_dict)
    return crud_trichtin.create(db=db, obj_in=A_create)
    # return current_user.id

@router.get("/get-all-by-uid/{uid}")
async def update(uid: str, db: Session = Depends(deps.get_db)):
    return crud_trichtin.get_all_by_uid(uid=uid, db= db)

@router.get("/get-all-by-vaiao/{uid_vaiao}")
async def update(uid_vaiao: str, db: Session = Depends(deps.get_db)):
    return crud_trichtin.get_trichtin_by_uid_vaiao(uid_vaiao=uid_vaiao, db= db)

@router.put("/update/{trichtin_id}")
async def delete(trichtin_id: int, trichtin: trichtinUpdate ,db: Session = Depends(deps.get_db)):
    trichtin_data = crud_trichtin.get_trichtin_by_id(id=trichtin_id, db=db)
    crud_trichtin.update(db=db, obj_in=trichtin, db_obj= trichtin_data)
    return {"message": "Success"}

@router.get("/get-trichtin/{trichtin_id}")
async def getTrichtin(trichtin_id:int, db: Session = Depends(deps.get_db)):
    trichtin_data = crud_trichtin.get_trichtin_by_id(id=trichtin_id, db=db)
    return trichtin_data