from app.crud.base import CRUDBase
from app.models.ctnv import ctnv
from app.schemas.ctnv import ctnvcreate, ctnvupdate
from sqlalchemy.orm import Session
class CRUDCtnv(CRUDBase[ctnv, ctnvcreate, ctnvupdate]):
    def get_ctnv_by_id(self, id: int, db: Session):
        db.query(ctnv).filter(ctnv.id == id).first()

crud_ctnv = CRUDCtnv(ctnv)