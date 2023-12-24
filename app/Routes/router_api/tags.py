from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.Routes import deps
from app import crud
from app.schemas.tags import tagscreate
router = APIRouter(prefix='/tags', tags=['tags'])

@router.get('/get-all')
def get_tags_all(db: Session = Depends(deps.get_db)):
    return crud.crud_tags.get_multi(db=db)

@router.post('/create-tags')
def create_tags(tagscreate_instance: tagscreate,db: Session = Depends(deps.get_db)):
    return crud.crud_tags.create(db=db, obj_in=tagscreate_instance)