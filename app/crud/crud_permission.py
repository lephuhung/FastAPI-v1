from app.crud.base import CRUDBase
from app.models.Permission import Permission
from app.schemas.permission import PermissionCreate, PermissionUpdate
class CRUDPermission(CRUDBase[Permission, PermissionCreate, PermissionUpdate]):
    pass

CURD_Permission = CRUDPermission(Permission)