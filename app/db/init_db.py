from app import crud, schemas, model
from app.core.sercurity import get_salt, get_password_hash
from app.constants.role import Role
from app.core.config import settings
from sqlalchemy.orm import Session
from datetime import datetime

def init_db(db: Session)-> None:
    salt= get_salt()
    user= crud.curd_user.get_by_name(db, settings.FIRST_SUPER_ADMIN_ACCOUNT_NAME)
    if user is None:
        model_user_admin= schemas.user.UserCreate({
            username: settings.FIRST_SUPER_ADMIN_ACCOUNT_NAME,
            active: True,
            salt: salt,
            password: get_password_hash(f'lph77{salt}'),
            created_at: datetime.timestamp(),
            updated_at: datetime.timestamp()
        })
        curd.curd_user.create(model_user_admin)