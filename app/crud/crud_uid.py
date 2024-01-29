from app.crud.base import CRUDBase
from app.models.uid import uid
from app.models.trangthai import trangthai
from app.models.donvi import Donvi
from app.models.donvi_hoinhom import donvi_hoinhom
from app.models.ctnv import ctnv
from app.schemas.uid import uidCreate, uidUpdate
from sqlalchemy.orm import Session
from sqlalchemy import desc, func
from fastapi.responses import JSONResponse

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
        data = ((db.query(uid.uid.label('uid'),uid.name.label('name'), uid.reaction.label('reaction'),
         uid.SDT.label('SDT'), uid.trangthai_id.label('trangthai_id'), uid.type_id.label('type_id'), uid.ghichu.label('ghichu'),
          uid.Vaiao.label('Vaiao'), uid.updated_at.label('updated_at'), trangthai.name.label('trangthai_name'), trangthai.color.label('trangthai_color') ,Donvi.name.label('donvi_name'), ctnv.name.label('ctnv_name'))
        .join(subquery, (uid.uid == subquery.c.uid) & (uid.updated_at == subquery.c.max_updated_at)))
        .join(trangthai, trangthai.id == uid.trangthai_id)
        .join(donvi_hoinhom, donvi_hoinhom.uid == uid.uid)
        .join(ctnv, donvi_hoinhom.CTNV_ID == ctnv.id)
        .join(Donvi, donvi_hoinhom.donvi_id == Donvi.id)
        .filter(uid.type_id==type_id)
        .all())
        formatted_result = [
        {
            'uid': row.uid,
            'name': row.name,
            'reaction': row.reaction,
            'SDT': row.SDT,
            'trangthai_id': row.trangthai_id,
            'type_id': row.type_id,
            'ghichu_id': row.ghichu,
            'Vaiao': row.Vaiao,
            'updated_at': str(row.updated_at),
            "trangthai_name": row.trangthai_name,
            "trangthai_color": row.trangthai_color,
            'donvi_name': row.donvi_name,
            'ctnv_name': row.ctnv_name,
        }
        for row in data
        ]
        formatted_result_as_dict = [dict(item) for item in formatted_result]
        return JSONResponse(content=formatted_result_as_dict)
        # return data

crud_uid = CRUDUid(uid)