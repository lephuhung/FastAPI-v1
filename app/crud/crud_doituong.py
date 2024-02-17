from  app.crud.base import CRUDBase
from pydantic import UUID4
from app.models.doituong import Doituong
from app.models.doituong_uid import Doituong_UID
from app.models.trichtin import trichtin
from app.models.doituong_donvi import Doituong_Donvi
from app.models.moiquanhe import moiquanhe
from app.models.uid import uid
from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from app.schemas.doituong import doituongcreate, doituongupdate
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
class CRUD_DOITUONG (CRUDBase[Doituong, doituongcreate, doituongupdate]):
    def get_doituong_by_id(self, doituong_id: UUID4, db: Session):
        return db.query(Doituong).filter(Doituong.id == doituong_id).first()

    def get_doituong_by_donvi_id(self, donvi_id: UUID4, db:Session):
        result = db.query(Doituong).join(Doituong_Donvi, Doituong.id == Doituong_Donvi.doituong_id ).filter(Doituong_Donvi.donvi_id==donvi_id).all()
        return result
        
    def get_details(self, doituong_id: UUID4, db:Session):
        details_uid = (
            db.query(
                Doituong_UID.doituong_id.label('id'),
                Doituong.client_name.label('name'),
                moiquanhe.name.label('moiquanhe_name'),
                uid.uid.label('uid'),
                uid.type_id.label('type_id'),
                uid.name.label('uid_name')
            )
            .filter(Doituong_UID.doituong_id == doituong_id)
            .join(Doituong, Doituong_UID.doituong_id == Doituong.id)
            .join(moiquanhe, moiquanhe.id == Doituong_UID.Moiquanhe_id)
            .join(uid, uid.uid == Doituong_UID.uid)
            .distinct(uid.uid)
            )
        formatted_result = [
        {
            'id': str(row.id),
            'name': row.name,
            'uid': row.uid,
            'type_id': row.type_id,
            'uid_name': row.uid_name,
            'moiquanhe_name': row.moiquanhe_name
        }
        for row in details_uid
        ]
        count_trichtin = (db.query(func.count(trichtin.uid).label('count')).filter(trichtin.uid == str(doituong_id)).all())
        details_trichtin = (db.query(trichtin).filter(trichtin.uid == str(doituong_id)).order_by(desc(trichtin.updated_at))).limit(5).all()
        # return JSONResponse(content=formatted_result)
        count = [{'doituong_id': str(doituong_id),'count': row.count} for row in count_trichtin]
        return JSONResponse(content={'trichtin_count': count, 'hoinhom_details': formatted_result, 'trichtin_details': jsonable_encoder(details_trichtin)})
crud_doituong = CRUD_DOITUONG(Doituong)