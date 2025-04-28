from fastapi import APIRouter, Body, Depends, HTTPException, Security
from typing import Annotated
from app.schemas.characteristic import CharacteristicCreate, CharacteristicUpdate
from app.crud.crud_search import individual_search, uid_search, trichtin_search
from app.Routes import deps
from sqlalchemy.orm import Session
router = APIRouter(prefix="/search", tags=["Tìm kiếm"])

@router.post('/individual')
async def search_individual(keyword: str,db: Session = Depends(deps.get_db)):
    return individual_search(keyword)

@router.post('/uid')
async def search_uid(keyword: str,db: Session = Depends(deps.get_db)):
    return uid_search(keyword)

@router.post('/trichtin')
async def search_trichtin(keyword: str,db: Session = Depends(deps.get_db)):
    return trichtin_search(keyword)
