from app.crud.base import CRUDBase
from app.models.donvi_hoinhom import donvi_hoinhom
from app.schemas.donvi_hoinhom import hoinhom_donvicreate, hoinhom_donviupdate
from pydantic import UUID4
from sqlalchemy.orm import Session
class CRUDHoinhom_donvi(CRUDBase[donvi_hoinhom, hoinhom_donvicreate, hoinhom_donviupdate]):
    def get_hoinhom_by_donvi(self,donvi_id: UUID4, db: Session):
        return db.query(donvi_hoinhom).filter(donvi_hoinhom.donvi_id == donvi_id).all()


    def get_all_hoinhom(self, db: Session):
        return db.query(donvi_hoinhom).all()
    
    def find_donvi_hoinhom(self, id: int, db: Session):
        data = db.query(donvi_hoinhom).filter(donvi_hoinhom.id==id).first()
        return data

crud_donvihoinhom = CRUDHoinhom_donvi(donvi_hoinhom)