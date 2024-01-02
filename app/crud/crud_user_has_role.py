from app.crud.base import CRUDBase
from app.models.user_has_role import user_has_role
from sqlalchemy.orm import Session
from pydantic import UUID4
from app.schemas.user_has_role import User_has_RoleCreate, User_has_RoleUpdate

class CRUD_user_has_role (CRUDBase[user_has_role, User_has_RoleCreate, User_has_RoleUpdate]):
    def get_user_has_role_by_userid(self, user_id: UUID4 ,db: Session):
        return db.query(user_has_role).filter(user_has_role.user_id==user_id).first()
    def get_user_role(self, user_id: UUID4, role_id: UUID4 ,db: Session):
        user_role= db.query(user_has_role).filter(user_has_role.role_id==role_id).filter(user_has_role.user_id==user_id).first()
        db.delete(user_role)
        db.commit()
        return True

crud_user_has_role = CRUD_user_has_role(user_has_role)