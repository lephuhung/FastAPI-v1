from fastapi import APIRouter, Body, Depends, HTTPException, Security
from typing import Annotated
from sqlalchemy.orm import Session
from app.Routes import deps
from pydantic import UUID4
from app import crud
router = APIRouter(prefix="/user-has-role", tags=["User has Role"])

@router.get("")
async def get():
    return {'123':'123'}

@router.post("/get-my-role")
async def post(user_id: UUID4, db: Session = Depends(deps.get_db)):
    return {}

@router.put("/{uid}")
async def update():
    return {'123':'123'}

@router.delete("/{uid}")
async def delete(uid: Annotated[int, 0]):
    return {'123':uid}
