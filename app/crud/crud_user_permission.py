from typing import Any, Dict, Optional, Union, List
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.user_permission import UserPermission
from app.schemas.user_permission import UserPermissionCreate, UserPermissionUpdate
from pydantic import UUID4


class CRUDUserPermission(CRUDBase[UserPermission, UserPermissionCreate, UserPermissionUpdate]):
    def get_by_user_id(self, db: Session, *, user_id: UUID4) -> List[UserPermission]:
        return db.query(UserPermission).filter(UserPermission.user_id == user_id).all()

    def get_by_permission_id(
        self, db: Session, *, permission_id: int
    ) -> List[UserPermission]:
        return db.query(UserPermission).filter(UserPermission.permission_id == permission_id).all()

    def get_by_user_and_permission(
        self, db: Session, *, user_id: UUID4, permission_id: int
    ) -> Optional[UserPermission]:
        return (
            db.query(UserPermission)
            .filter(UserPermission.user_id == user_id, UserPermission.permission_id == permission_id)
            .first()
        )


user_permission = CRUDUserPermission(UserPermission) 