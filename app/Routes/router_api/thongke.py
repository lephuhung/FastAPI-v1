from fastapi import APIRouter, Depends, Security
from sqlalchemy.orm import Session
from app.Routes import deps
from app import crud
from app.schemas.tags import tagscreate
from pydantic import UUID4
router = APIRouter(prefix='/thongke', tags=['Thống kê'])

@router.get('/donvi/uid/{donvi_id}')
def get_tags_all(donvi_id: UUID4, db: Session = Depends(deps.get_db)):
    return crud.crud_thongke.thongkedonvi_uid(db=db, donvi_id = donvi_id)

@router.get('/donvi/doituong/{donvi_id}')
def get_tags_all(donvi_id: UUID4, db: Session = Depends(deps.get_db)):
    return crud.crud_thongke.thongkedonvi_doituong(db=db, donvi_id = donvi_id)

@router.get('/thongkedonvi/')
def create_tags(db: Session = Depends(deps.get_db)):
    return crud.crud_thongke.thongkedonvi(db=db)

@router.get('/thongketinhchat/')
def create_tags(db: Session = Depends(deps.get_db), current_user = Security(deps.get_current_active_user, scopes=[])):
    return crud.crud_thongke.thongketinhchat(db)

@router.get('/thongkephanloai/')
def create_tags(db: Session = Depends(deps.get_db)):
    return crud.crud_thongke.thongkephanloai(db)

@router.get('/thongkectnv/')
def create_tags(db: Session = Depends(deps.get_db)):
    return crud.crud_thongke.thongkectnv(db)

@router.get('/thongkedoituongctnv/')
def create_tags(db: Session = Depends(deps.get_db)):
    return crud.crud_thongke.thongkedoituongctnv(db)

@router.get('/details/donvi/{donvi_id}')
def create_tags(donvi_id: UUID4, db: Session = Depends(deps.get_db), current_user = Security(deps.get_current_active_user, scopes=[])):
    return crud.crud_thongke.details_uid(donvi_id=donvi_id, db=db)

@router.get('/details/doituong/{donvi_id}')
def create_tags(donvi_id: UUID4, db: Session = Depends(deps.get_db), current_user = Security(deps.get_current_active_user, scopes=[])):
    return crud.crud_thongke.deatails_doituong(donvi_id=donvi_id, db=db)



