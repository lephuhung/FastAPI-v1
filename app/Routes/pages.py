from fastapi import APIRouter, Body, Depends, HTTPException, Security
from typing import Annotated
router = APIRouter(prefix="/uid", tags=["uid"])

@router.get("/")
async def get():
    return {'123':'123'}

@router.post("/")
async def post():
    return {'123':'123'}

@router.put("/{uid}")
async def update():
    return {'123':'123'}

@router.delete("/{uid}")
async def delete(uid: Annotated[int, 0]):
    return {'123':uid}
