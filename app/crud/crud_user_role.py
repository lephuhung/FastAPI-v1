from typing import Any, Dict, Optional, Union, List
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.user_role import UserRole
from app.schemas.user_role import UserRoleCreate, UserRoleUpdate
from pydantic import UUID4


class CRUDUserRole(CRUDBase[UserRole, UserRoleCreate, UserRoleUpdate]):
    def get_by_user_id(self, db: Session, *, user_id: UUID4) -> List[UserRole]:
        return db.query(UserRole).filter(UserRole.user_id == user_id).all()

    def get_by_role_id(self, db: Session, *, role_id: UUID4) -> List[UserRole]:
        return db.query(UserRole).filter(UserRole.role_id == role_id).all()

    def get_by_user_and_role(
        self, db: Session, *, user_id: UUID4, role_id: UUID4
    ) -> Optional[UserRole]:
        return (
            db.query(UserRole)
            .filter(UserRole.user_id == user_id, UserRole.role_id == role_id)
            .first()
        )


user_role = CRUDUserRole(UserRole) 