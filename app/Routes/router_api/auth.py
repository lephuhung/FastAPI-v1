from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from app import schemas, models, crud 
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
    # Get role id by user id
    role_user_id = crud.crud_user_has_role.get_user_has_role_by_userid(user_id=user.id, db=db)
    # Get Donvi id of User
    donvi = crud.crud_user_donvi.get_donvi_by_user_id(user_id=user.id, db=db)
    # Get Permission id by user id
    permision= crud.crud_user_has_permission.get_permission_user(user_id=user.id, db=db)
    # Create access token
    access_token = sercurity.create_access_token(
        subject={"id": str(user.id), "username": user.username, "donvi_id": str(donvi[0]['donvi_id']) ,"role": [f'{role_user_id.role_id}'], "permission":permision},
        expires_delta=access_token_expires,
    )
    return {"access_token": access_token, "token_type": "bearer"}