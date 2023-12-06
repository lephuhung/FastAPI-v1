from app.crud.base import CRUDBase
from pydantic import UUID4
from sqlalchemy.orm import Session
from app.models.role_has_permission import Role_has_permission
from app.schemas.role_has_permission import Role_has_PermissionUpdate, Role_has_PermissionCreate

class CURDRole_has_Permission(CRUDBase[Role_has_permission, Role_has_PermissionCreate, Role_has_PermissionUpdate]):
    def get_all_permission_in_role(self, role_id: UUID4, *, db: Session):
        role_permissions = (
        db.query(Role_has_permission.permission_id)
        .filter(Role_has_permission.role_id == role_id)
        .all()
        )
        return [str(permission[0]) for permission in role_permissions]


CrudRole_has_Permission = CURDRole_has_Permission(Role_has_permission)
