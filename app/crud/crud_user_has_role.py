from app.crud.base import CRUDBase
from app.models.user_has_role import user_has_role
from sqlalchemy.orm import Session
from pydantic import UUID4
from app.schemas.user_has_role import User_has_RoleCreate, User_has_RoleUpdate

class CRUD_user_has_role (CRUDBase[user_has_role, User_has_RoleCreate, User_has_RoleUpdate]):
    def get_user_has_role_by_userid(self, user_id: UUID4 ,db: Session):
        return db.query(user_has_role).filter(user_has_role.user_id==user_id).first()


crud_user_has_role = CRUD_user_has_role(user_has_role)