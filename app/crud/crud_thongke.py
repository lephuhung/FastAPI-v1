from app.crud.base import CRUDBase
from app.models.tinhchat import tinhchat
from app.models.donvi import Donvi
from app.models.donvi_hoinhom import donvi_hoinhom
from app.models.doituong_donvi import Doituong_Donvi
from app.models.tinhchat_hoinhom import tinhchat_hoinhom
from app.models.uid import uid
from app.models.ctnv import ctnv
from app.models.doituong import Doituong
from app.schemas.tinhchat import tinhchatcreate, tinhchatupdate
from sqlalchemy.orm import Session
from pydantic import UUID4
from fastapi.responses import JSONResponse
from sqlalchemy import desc, func, String
from sqlalchemy.orm import joinedload 
class CRUDThongKe(CRUDBase[tinhchat, tinhchatcreate, tinhchatupdate]):
    def thongkedonvi_uid(self, donvi_id: UUID4 ,db: Session):
        donvihoinhom_details = (db.query(donvi_hoinhom.uid.label('uid'), uid.name.label('uid_name'), ctnv.name.label('ctnv_name'), ctnv.id.label('ctnv_id'), uid.Vaiao.label('Vaiao'))
        .join(uid, donvi_hoinhom.uid == uid.uid)
        .join(ctnv, ctnv.id == donvi_hoinhom.CTNV_ID)
        .filter(donvi_hoinhom.donvi_id==donvi_id)
        .distinct(uid.uid)
        .all())
        formatted_result = [{'uid':row.uid, 'uid_name': row.uid_name, 'ctnv_name':row.ctnv_name, 'ctnv_id': row.ctnv_id, 'Vaiao': row.Vaiao} for row  in donvihoinhom_details]
        vaiao_count = sum(item["Vaiao"] for item in formatted_result)
        # Count number of unique ctnv_id
        ctnv_id_count = len(set(item["ctnv_id"] for item in formatted_result))
        # count ctnv_id
        ctnv_id_counts = {}
        for item in formatted_result:
            ctnv_id = item["ctnv_name"]
            ctnv_id_counts[ctnv_id] = ctnv_id_counts.get(ctnv_id, 0) + 1
        # export output
        thongke_counts ={
            'VaiAo': vaiao_count,
            'NVCB': ctnv_id_count - vaiao_count,
            'ctnv':[
                {'ctnv_name':ctnv_id, 'count':count} for ctnv_id, count in ctnv_id_counts.items()
            
            ]
        }
        return thongke_counts
    def thongkedonvi_doituong(self, donvi_id: UUID4, db: Session):
        donvi_doituong = (db.query(Doituong_Donvi.id.label('id'),Doituong.id.label('doituong_id'), Doituong.KOL.label('KOL'), ctnv.name.label('ctnv_name'))
        .join(Doituong, Doituong.id == Doituong_Donvi.doituong_id)
        .join(ctnv, ctnv.id == Doituong_Donvi.CTNV_ID)
        .filter(Doituong_Donvi.donvi_id == donvi_id)
        .distinct(Doituong.id)
        .all())
        formatted_result =[{'doituong_id': str(row.doituong_id), 'KOL': row.KOL, 'ctnv_name': row.ctnv_name} for row in donvi_doituong]
        vaiao_count = sum(item["KOL"] for item in formatted_result)
        ctnv_name_count = len(set(item["ctnv_name"] for item in formatted_result))
        # count ctnv_id
        ctnv_id_counts = {}
        for item in formatted_result:
            ctnv_id = item["ctnv_name"]
            ctnv_id_counts[ctnv_id] = ctnv_id_counts.get(ctnv_id, 0) + 1
        # export output
        thongke_counts ={
            'KOL': vaiao_count,
            'THEODOI': ctnv_name_count - vaiao_count,
            'ctnv':[
                {'ctnv_name':ctnv_id, 'count':count} for ctnv_id, count in ctnv_id_counts.items()
            
            ]
        }
        return thongke_counts
    def thongkedonvi(self, db: Session):
        json_data= []
        donvi_list = db.query(Donvi).all()
        for donvi in donvi_list:
            doituong = crud_thongke.thongkedonvi_doituong(db = db, donvi_id = donvi.id)
            hoinhom = crud_thongke.thongkedonvi_uid(db = db, donvi_id= donvi.id)
            output ={'donvi': donvi.name, 'id': donvi.id, 'hoinhom': hoinhom, 'doituong': doituong}
            json_data.append(output)
        return json_data
    def thongketinhchat(self, db: Session):
        data = (
        db.query(
        tinhchat.id.label('id'),
        tinhchat.name.label('name'),
        func.count(tinhchat.id).label('count'),
        tinhchat_hoinhom.uid.label('uid'),
        uid.name.label('uid_name'),
        )
        .join(tinhchat_hoinhom, tinhchat_hoinhom.tinhchat_id == tinhchat.id)
        .join(uid, uid.uid == tinhchat_hoinhom.uid)
        .group_by(tinhchat.id, tinhchat_hoinhom.uid, uid.name)
        .all()
)
        formatted_result = [{'id':row.id, 'name':row.name, 'count':row.count, 'uid': row.uid, 'uid_name': row.uid_name} for row in data]
        result = []

        for entry in formatted_result:
            key = (entry["id"], entry["name"])
            found = False

            for item in result:
                if item["id"] == key[0] and item["name"] == key[1]:
                    item["count"] += entry["count"]
                    item["uids"].append(entry["uid_name"])
                    found = True
                    break
            if not found:
                result.append({"id": key[0], "name": key[1], "count": entry["count"], "uids": [entry["uid_name"]]})
        return JSONResponse(content=result)
crud_thongke=CRUDThongKe(tinhchat)