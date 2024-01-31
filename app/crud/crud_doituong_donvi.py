from  app.crud.base import CRUDBase
from app.models.doituong_donvi import Doituong_Donvi
from app.schemas.doituong_donvi import doituong_donvicreate, doituong_donviupdate
from pydantic import UUID4
from sqlalchemy.orm import Session
class CRUD_DOITUONG_DONVI (CRUDBase[Doituong_Donvi, doituong_donvicreate, doituong_donviupdate]):
    def get_doituong_by_donvi_id(self, donviid:UUID4, db: Session):
        return db.query(Doituong_Donvi).filter(Doituong_Donvi.donvi_id == donviid).first()
    
crud_doituong_donvi = CRUD_DOITUONG_DONVI(Doituong_Donvi)