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
    def get_by_name(self, db: Session, *,name: str):
        return db.query(self.model).filter(self.model.name==name).first()


user = CRUDUser(User)