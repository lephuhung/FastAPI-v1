from  app.crud.base import CRUDBase
from pydantic import UUID4
from app.models.doituong import Doituong
from sqlalchemy.orm import Session
from app.schemas.doituong import doituongcreate, doituongupdate
class CRUD_DOITUONG (CRUDBase[Doituong, doituongcreate, doituongupdate]):
    def get_doituong_by_id(self, doituong_id: UUID4, db: Session):
        return db.query(Doituong).filter(Doituong.id == doituong_id).first()

crud_doituong = CRUD_DOITUONG(Doituong)