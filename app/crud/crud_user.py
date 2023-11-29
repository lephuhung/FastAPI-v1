from typing import Any, Dict, List, Optional, Union

from app.core.sercurity import get_password_hash, verify_password
from app.crud.base import CRUDBase
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from pydantic.types import UUID4
from sqlalchemy.orm import Session
from app.Routes import deps

class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    # Get User by Name
    def get_by_name(self, db: Session, *,username: str):
        return db.query(User).filter(User.username==username).first()
    #get user active
    def is_active(self, user: User) -> bool:
        return user.active
    # get user by id
    def get_by_id(self, db: Session, *, id: int):
        return db.query(User).filter(User.id==id).first()

    # def get_multiple_users_withid(self, db: Session, *,id: int):
    #     return db.query(User).filter(User.id==id).

crud_user = CRUDUser(User)