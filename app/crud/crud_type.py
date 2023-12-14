from app.crud.base import CRUDBase
from app.models.type import type
from app.schemas.type import typeupdate, typecreate
from sqlalchemy.orm import Session
class CRUDType(CRUDBase[type, typecreate, typeupdate]):
    def get_type_by_id(self, id: int, db: Session):
        return db.query(type).filter(type.id==id).first()

crud_type= CRUDType(type)