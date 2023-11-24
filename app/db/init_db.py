from app import crud, schemas, models
from app.core.sercurity import get_salt, get_password_hash
from app.constants.role import Role
from app.core.config import settings
from sqlalchemy.orm import Session
from datetime import datetime

def init_db(db: Session)-> None:
    salt= get_salt()
    # crud.crud_user.get_by_name(db=db, username= settings.FIRST_SUPER_ADMIN_ACCOUNT_NAME)
    user= crud.crud_user.get_by_name(db=db, username=settings.FIRST_SUPER_ADMIN_ACCOUNT_NAME)
    if user is None:
        model_user_admin= schemas.user.UserCreate(
            username= settings.FIRST_SUPER_ADMIN_ACCOUNT_NAME,
            active= True,
            salt= salt,
            password= get_password_hash(f'lph77{salt}'),
            created_at= datetime.timestamp(),
            updated_at= datetime.timestamp()
        )
        crud.crud_user.create(model_user_admin) 