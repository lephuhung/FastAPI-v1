from app.crud.base import CRUDBase
from app.models.user_has_perrmisson import user_has_permissions
from app.schemas.user_has_permissions import userhaspermissionCreate, userhaspermissionUpdate
from sqlalchemy.orm import Session
from pydantic import UUID4
class CRUD_User_has_permission(CRUDBase[user_has_permissions,userhaspermissionCreate, userhaspermissionUpdate]):
    def get_permission_user(self, user_id: UUID4 ,db: Session):
        user_permissions = (
        db.query(user_has_permissions.permission_id)
        .filter(user_has_permissions.user_id == user_id)
        .all()
        )
        return [str(permission[0]) for permission in user_permissions]

crud_user_has_permission = CRUD_User_has_permission(user_has_permissions)


