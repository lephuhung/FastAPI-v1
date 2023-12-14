from app.crud.base import CRUDBase
from app.models.trangthai import trangthai
from app.schemas.trangthai import trangthaicreate, trangthaiupdate
from sqlalchemy.orm import Session
class CRUDTrangthai(CRUDBase[trangthai, trangthaicreate, trangthaiupdate]):
    def get_trangthai_by_id(self, db: Session, id: int):
        return db.query(trangthai).filter(trangthai.id ==id).first()

crud_trangthai= CRUDTrangthai(trangthai)