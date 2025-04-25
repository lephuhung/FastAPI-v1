from typing import Any, Dict, Optional, Union, List
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.role_permission import RolePermission
from app.schemas.role_permission import RolePermissionCreate, RolePermissionUpdate
from pydantic import UUID4


class CRUDRolePermission(CRUDBase[RolePermission, RolePermissionCreate, RolePermissionUpdate]):
    def get_by_role_id(self, db: Session, *, role_id: UUID4) -> List[RolePermission]:
        return db.query(RolePermission).filter(RolePermission.role_id == role_id).all()

    def get_by_permission_id(
        self, db: Session, *, permission_id: int
    ) -> List[RolePermission]:
        return db.query(RolePermission).filter(RolePermission.permission_id == permission_id).all()

    def get_by_role_and_permission(
        self, db: Session, *, role_id: UUID4, permission_id: int
    ) -> Optional[RolePermission]:
        return (
            db.query(RolePermission)
            .filter(RolePermission.role_id == role_id, RolePermission.permission_id == permission_id)
            .first()
        )


role_permission = CRUDRolePermission(RolePermission)
