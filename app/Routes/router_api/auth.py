from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from app import schemas, models
from app.Routes import deps
from sqlalchemy.orm import Session
from app.core import sercurity, config
from datetime import timedelta
from fastapi.security import (
    OAuth2PasswordBearer,
    OAuth2PasswordRequestForm,
    SecurityScopes,
)
router = APIRouter()

@router.post("/login" )
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Annotated[Session, Depends(deps.get_db)]
):
    user = sercurity.authenticate_user(form_data.username, form_data.password, db=db)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=config.settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = sercurity.create_access_token(
        subject={"id": 2, "username": user.username, "Role": ["guest"], "Permission":[]},
        expires_delta=access_token_expires,
    )
    return {"access_token": access_token, "token_type": "bearer"}