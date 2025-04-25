from typing import Any, Dict, List, Optional, Union

from app.core.security import get_password_hash, verify_password
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
    
    # get current user
    # def get_current_user(self, db: Session, *, id: UUID4):
    #     current_user = db.get(User).filter(
    # def get_multiple_users_withid(self, db: Session, *,id: int):
    #     return db.query(User).filter(User.id==id).

    def get_by_username(self, db: Session, *, username: str) -> Optional[User]:
        return db.query(User).filter(User.username == username).first()

    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        db_obj = User(
            username=obj_in.username,
            password=get_password_hash(obj_in.password),
            salt=obj_in.salt,
            is_active=obj_in.is_active,
            unit_id=obj_in.unit_id,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: User, obj_in: Union[UserUpdate, Dict[str, Any]]
    ) -> User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if update_data.get("password"):
            hashed_password = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def authenticate(self, db: Session, *, username: str, password: str) -> Optional[User]:
        user = self.get_by_username(db, username=username)
        if not user:
            return None
        if not verify_password(password, user.password):
            return None
        return user

crud_user = CRUDUser(User)