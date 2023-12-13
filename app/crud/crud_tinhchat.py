from app.crud.base import CRUDBase
from app.models.tinhchat import tinhchat
from app.schemas.tinhchat import tinhchatcreate, tinhchatupdate
from sqlalchemy.orm import Session

class CRUDTinhchat(CRUDBase[tinhchat, tinhchatcreate, tinhchatupdate]):
    def find_tinhchat_byid (self, id: int, db: Session):
        return db.query(tinhchat).filter(tinhchat.id ==id).first()
    
crud_tinhchat=CRUDTinhchat(tinhchat)

    