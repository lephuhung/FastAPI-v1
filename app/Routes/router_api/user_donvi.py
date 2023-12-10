from fastapi import APIRouter, Body, Depends, HTTPException, Security
from typing import Annotated
from sqlalchemy.orm import Session
from app.Routes import deps
from app.core.Utils import return_json_data
from app.crud.crud_user_donvi import crud_user_donvi
from pydantic import UUID4
from app.schemas.user_donvi import userdonvioutDB, UserDonviCreate
from fastapi.security import (
    OAuth2PasswordBearer,
    OAuth2PasswordRequestForm,
    SecurityScopes,
)
router = APIRouter(prefix="/usr-dvi", tags=["usr-dvi"])

# @router.get("")
# async def get():
#     return {'123':'123'}

# Get All users in Don vi
@router.get("/get-all-in-donvi")
async def get_all_in_donvi(uuid: UUID4, db: Session = Depends(deps.get_db)):
    return crud_user_donvi.get_user_by_uid_donvi(uuid, db)

# Get donvi of user id
@router.get("/get-donvi-user")
async def get_donvi_user(uuid: UUID4, db:Session = Depends(deps.get_db)):
    data=crud_user_donvi.get_donvi_by_user_id(uuid, db)
    return return_json_data(data)

#Count user in donvi group
@router.get("/count-user-by-donvi")
async def count_user_by_donvi(uuid: UUID4, db: Session = Depends(deps.get_db)):
    data= crud_user_donvi.count_users_in_donvi(uuid, db)
    return return_json_data(data)

# Count all users in donvi 
@router.get("/count-all-users-donvi")
async def count_all_user_by_donvi(db: Session = Depends(deps.get_db)):
    data= crud_user_donvi.count_all_user_in_donvi(db)
    return return_json_data(data)

#create new user donvi
@router.post("/create-new-user")
async def create_new_user(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session= Depends(deps.get_db)):
    data = UserDonviCreate(
        user_id= form_data.user_id,
        donvi_id=form_data.donvi_id
    )
    return crud_user_donvi.create_user(data)