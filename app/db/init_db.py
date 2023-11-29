from app import crud, schemas, models
from app.core.sercurity import get_salt, get_password_hash
from app.constants.role import Role
from app.core.config import settings
from sqlalchemy.orm import Session
from datetime import datetime

def init_db(db: Session)-> None:
    username_pao5=["Luongvinhlong", "Nguyendangphi", "Dangdonthang"]
    # Create superadmin PA05
    user = crud.crud_user.get_by_name(db=db, username=settings.FIRST_SUPER_ADMIN_ACCOUNT_NAME)
    salt= get_salt()
    if user is None:
        model_user_admin= schemas.user.UserCreate(
            username= settings.FIRST_SUPER_ADMIN_ACCOUNT_NAME,
            active= True,
            salt= salt,
            password= get_password_hash(f'lph77{salt}'),
        )
        crud.crud_user.create(db, obj_in=model_user_admin) 
        for item in username_pao5:
            user_pa05= schemas.user.UserCreate(
                username= item,
                active= True,
                salt= get_salt(),
                password= get_password_hash(f'123456{salt}')
            )
            crud.crud_user.create(db, obj_in= user_pa05)
    # Create user for Phong PA05 

    # Create Role

    # Create donvi
    donvi_list= ["PA05", "PA02", "PA03", "PA04", "PA06", "PA09", "PA08", "PA01"]
    donvi= crud.crud_donvi.get_donvi_by_name(db=db, name="PA05")
    if donvi is None:
        for item in donvi_list:
            donviinDB= schemas.donvi.DonviCreate(name= item)
            crud.crud_donvi.create(db, obj_in=donviinDB)
    # Create Permission