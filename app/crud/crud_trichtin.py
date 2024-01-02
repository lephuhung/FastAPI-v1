from app.crud.base import CRUDBase
from app.models.trichtin import trichtin
from app.schemas.trichtin import trichtinCreate, trichtinUpdate
from sqlalchemy.orm import Session
class CRUD_Trichtin(CRUDBase[trichtin, trichtinCreate, trichtinUpdate]):
    def get_all_by_uid(self,uid: str, db: Session):
        return db. query(trichtin).filter(trichtin.uid == uid).all()
    def get_trichtin_by_id(self,id: int, db: Session):
        return db.query(trichtin).filter(trichtin.id == id).first()

crud_trichtin = CRUD_Trichtin(trichtin)