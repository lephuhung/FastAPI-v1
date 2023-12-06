from app.crud.base import CRUDBase
from app.models.Permission import Permission
from sqlalchemy.orm import Session
from app.schemas.permission import PermissionCreate, PermissionUpdate
class CRUDPermission(CRUDBase[Permission, PermissionCreate, PermissionUpdate]):
    def get_permission_by_name(self, name: str, * ,db: Session):
        return db.query(Permission).filter(Permission.name==name).first()
        
CURD_Permission = CRUDPermission(Permission)