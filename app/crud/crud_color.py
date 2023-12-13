from app.crud.base import CRUDBase
from app.models.color import color
from app.schemas.color import colorcreate, colorupdate
from sqlalchemy.orm import Session
class CRUDColor(CRUDBase[color, colorcreate, colorupdate]):

    def get_color_by_name(self, name: str ,db: Session):
       return db.query(color).filter(color.name ==name).first()
    

    def get_color_by_hex(self, color: str ,db: Session):
        return db.query(color).filter(color.color ==color).first()
    

    
crud_color= CRUDColor(color)