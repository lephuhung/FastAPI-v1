from app.crud.base import CRUDBase
from app.models.uid import uid
from app.schemas.uid import uidCreate, uidUpdate
from sqlalchemy.orm import Session
from sqlalchemy import desc, func

class CRUDUid (CRUDBase[uid,uidCreate, uidUpdate]):
    def get_uid_by_id(self, id:int, db: Session):
        data = db.query(uid).filter(uid.id == id).first()
        return data 

    def get_last_uid_by_id(self, id:str, db: Session):
        data = db.query(uid).filter(uid.uid == id).order_by(desc(uid.updated_at)).first()
        return data 

    def get_all_by_uid(self, uid_uid: str, db: Session):
        data = db.query(uid).filter(uid.uid == uid_uid).order_by(desc(uid.updated_at)).all()
        return data 
    def get_all_by_type_id(self, type_id: int, db: Session):
        subquery = (db.query(uid.uid, func.max(uid.updated_at).label('max_updated_at')).group_by(uid.uid).subquery())
        data = (db.query(uid).join(subquery, (uid.uid == subquery.c.uid) & (uid.updated_at == subquery.c.max_updated_at))).filter(uid.type_id==type_id).all()
        return data

crud_uid = CRUDUid(uid)