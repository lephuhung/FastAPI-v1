from app.crud.base import CRUDBase
from app.models.Role import Role
from sqlalchemy.orm import Session
from app.schemas.role import RoleCreate, RoleUpdate
class CRUDRole(CRUDBase[Role, RoleCreate, RoleUpdate]):
    def get_roleid_by_name(self, db: Session, *,name: str):
        return db.query(Role).filter(Role.name==name).first()
    

CURD_Role= CRUDRole(Role)