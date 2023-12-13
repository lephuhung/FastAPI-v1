from app.crud.base import CRUDBase
from app.models.moiquanhe import moiquanhe
from app.schemas.moiquanhe import moiquanhecreate, moiquanheupdate
from sqlalchemy.orm import Session
class CRUDMoiquanhe (CRUDBase[moiquanhe, moiquanhecreate, moiquanheupdate]):
    
    def get_name_by_id(self, id: int, db: Session):
       return db.query(moiquanhe).filter(moiquanhe.id==id).first()
    
crud_moiquanhe = CRUDMoiquanhe(moiquanhe)