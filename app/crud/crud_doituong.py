from app.crud.base import CRUDBase
from pydantic import UUID4
from app.models.doituong import Doituong
from app.models.doituong_uid import Doituong_UID
from app.models.ctnv import ctnv
from app.models.trichtin import trichtin
from app.models.donvi import Donvi
from app.models.doituong_donvi import Doituong_Donvi
from app.models.moiquanhe import moiquanhe
from app.models.uid import uid
from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from app.schemas.doituong import doituongcreate, doituongupdate
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


class CRUD_DOITUONG(CRUDBase[Doituong, doituongcreate, doituongupdate]):
    def get_doituong_by_id(self, doituong_id: UUID4, db: Session):
        return db.query(Doituong).filter(Doituong.id == doituong_id).first()

    def get_doituong_by_donvi_id(self, donvi_id: UUID4, db: Session):
        result = (
            db.query(Doituong)
            .join(Doituong_Donvi, Doituong.id == Doituong_Donvi.doituong_id)
            .filter(Doituong_Donvi.donvi_id == donvi_id)
            .all()
        )
        return result

    def get_doituong_with_ctnv(self, db: Session):
        result = (
            db.query(Doituong.id.label('id'), Doituong.client_name.label('client_name'), Doituong.CCCD.label('CCCD'), Doituong.CMND.label('CMND'), 
            Doituong.Thongtinbosung.label('Thongtinbosung'), Doituong.Ngaysinh.label('Ngaysinh'), Doituong.Gioitinh.label('Gioitinh'), Doituong.Image.label('Image'),
            Doituong.Quequan.label('Quequan'), Doituong.SDT.label('SDT'), Doituong.KOL.label('KOL'), Donvi.name.label('donvi_name'), Donvi.id.label('donvi_id'),
            ctnv.id.label('ctnv_id') ,ctnv.name.label('ctnv_name'), Doituong.created_at.label('created_at'), Doituong.updated_at.label('updated_at'))
            .join(Doituong_Donvi, Doituong.id == Doituong_Donvi.doituong_id)
            .join (ctnv, ctnv.id== Doituong_Donvi.CTNV_ID)
            .join(Donvi, Donvi.id == Doituong_Donvi.donvi_id)
            .order_by(Doituong_Donvi.updated_at.desc())
            .all()
        )
        formatted_result = [
            {
                "id": str(row.id),
                "client_name": row.client_name,
                "CCCD": row.CCCD,
                "CMND": row.CMND,
                "KOL": row.KOL,
                "Ngaysinh": str(row.Ngaysinh),
                "Thongtinbosung": row.Thongtinbosung,
                "ctnv_name": row.ctnv_name,
                "SDT": row.SDT,
                "Gioitinh": row.Gioitinh,
                "Quequan": row.Quequan,
                "ctnv_name": row.ctnv_name,
                "donvi_id": str(row.donvi_id),
                "donvi_name": row.donvi_name,
                "ctnv_id": row.ctnv_id,
                "updated_at":str(row.updated_at),
                "created_at":str(row.created_at),
                "Image": row.Image,

            }
            for row in result
        ]

        formatted_result_as_dict = [dict(item) for item in formatted_result]
        return JSONResponse(content=formatted_result_as_dict)
    def get_details(self, doituong_id: UUID4, db: Session):
        details_uid = (
            db.query(
                Doituong_UID.doituong_id.label("id"),
                Doituong.client_name.label("name"),
                moiquanhe.name.label("moiquanhe_name"),
                uid.uid.label("uid"),
                uid.type_id.label("type_id"),
                uid.name.label("uid_name"),
            )
            .filter(Doituong_UID.doituong_id == doituong_id)
            .join(Doituong, Doituong_UID.doituong_id == Doituong.id)
            .join(moiquanhe, moiquanhe.id == Doituong_UID.moiquanhe_id)
            .join(uid, uid.uid == Doituong_UID.uid)
            .distinct(uid.uid)
        )
        formatted_result = [
            {
                "id": str(row.id),
                "name": row.name,
                "uid": row.uid,
                "type_id": row.type_id,
                "uid_name": row.uid_name,
                "moiquanhe_name": row.moiquanhe_name,
            }
            for row in details_uid
        ]
        count_trichtin = (
            db.query(func.count(trichtin.uid).label("count"))
            .filter(trichtin.uid == str(doituong_id))
            .all()
        )
        details_trichtin = (
            (
                db.query(trichtin)
                .filter(trichtin.uid == str(doituong_id))
                .order_by(desc(trichtin.updated_at))
            )
            .limit(5)
            .all()
        )
        # return JSONResponse(content=formatted_result)
        count = [
            {"doituong_id": str(doituong_id), "count": row.count}
            for row in count_trichtin
        ]
        return JSONResponse(
            content={
                "trichtin_count": count,
                "hoinhom_details": formatted_result,
                "trichtin_details": jsonable_encoder(details_trichtin),
            }
        )


crud_doituong = CRUD_DOITUONG(Doituong)
