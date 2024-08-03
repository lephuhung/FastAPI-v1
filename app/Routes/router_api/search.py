from fastapi import APIRouter, Body, Depends, HTTPException, Security
from typing import Annotated
from app.schemas.tinhchat import tinhchatcreate, tinhchatupdate
from app.crud.crud_search import doituong_search, uid_search, trichtin_search
from app.Routes import deps
from sqlalchemy.orm import Session
router = APIRouter(prefix="/search", tags=["Tìm kiếm"])

@router.post('/doituong')
async def search_doituong(keyword: str,db: Session = Depends(deps.get_db)):
    return doituong_search(keyword)

@router.post('/uid')
async def search_uid(keyword: str,db: Session = Depends(deps.get_db)):
    return uid_search(keyword)

@router.post('/trichtin')
async def search_trichtin(keyword: str,db: Session = Depends(deps.get_db)):
    return trichtin_search(keyword)
