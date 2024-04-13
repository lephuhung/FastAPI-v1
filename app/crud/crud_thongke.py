from app.crud.base import CRUDBase
from app.models.tinhchat import tinhchat
from app.models.donvi import Donvi
from app.models.donvi_hoinhom import donvi_hoinhom
from app.models.doituong_donvi import Doituong_Donvi
from app.models.tinhchat_hoinhom import tinhchat_hoinhom
from app.models.uid import uid
from app.models.ctnv import ctnv
from app.models.trangthai import trangthai
from app.models.doituong import Doituong
from app.models.doituong_donvi import Doituong_Donvi
from app.schemas.tinhchat import tinhchatcreate, tinhchatupdate
from sqlalchemy.orm import Session
from pydantic import UUID4
from fastapi.responses import JSONResponse
from sqlalchemy import desc, func, String, select, sql, func
from sqlalchemy.orm import joinedload


class CRUDThongKe(CRUDBase[tinhchat, tinhchatcreate, tinhchatupdate]):
    # thống kê uid thuộc đơn vị
    def thongkedonvi_uid(self, donvi_id: UUID4, db: Session):
        donvihoinhom_details = (
            db.query(
                donvi_hoinhom.uid.label("uid"),
                uid.name.label("uid_name"),
                ctnv.name.label("ctnv_name"),
                ctnv.id.label("ctnv_id"),
                uid.Vaiao.label("Vaiao"),
            )
            .join(uid, donvi_hoinhom.uid == uid.uid)
            .join(ctnv, ctnv.id == donvi_hoinhom.CTNV_ID)
            .filter(donvi_hoinhom.donvi_id == donvi_id)
            .distinct(uid.uid)
            .all()
        )
        formatted_result = [
            {
                "uid": row.uid,
                "uid_name": row.uid_name,
                "ctnv_name": row.ctnv_name,
                "ctnv_id": row.ctnv_id,
                "Vaiao": row.Vaiao,
            }
            for row in donvihoinhom_details
        ]
        KOL = sum(item["Vaiao"] for item in formatted_result)
        # Count number of unique ctnv_id
        ctnv_id_count = len(set(item["ctnv_id"] for item in formatted_result))
        # count ctnv_id
        ctnv_id_counts = {}
        for item in formatted_result:
            ctnv_id = item["ctnv_name"]
            ctnv_id_counts[ctnv_id] = ctnv_id_counts.get(ctnv_id, 0) + 1
        # export output
        thongke_counts = {
            "VaiAo": KOL,
            "NVCB": len(formatted_result) - KOL,
            "ctnv": [
                {"ctnv_name": ctnv_id, "count": count}
                for ctnv_id, count in ctnv_id_counts.items()
            ],
        }
        return thongke_counts

    # thống kê đối tượng thuộc đơn vị
    def thongkedonvi_doituong(self, donvi_id: UUID4, db: Session):
        donvi_doituong = (
            db.query(
                Doituong_Donvi.id.label("id"),
                Doituong.id.label("doituong_id"),
                Doituong.KOL.label("KOL"),
                ctnv.name.label("ctnv_name"),
            )
            .join(Doituong, Doituong.id == Doituong_Donvi.doituong_id)
            .join(ctnv, ctnv.id == Doituong_Donvi.CTNV_ID)
            .filter(Doituong_Donvi.donvi_id == donvi_id)
            .distinct(Doituong.id)
            .all()
        )
        formatted_result = [
            {
                "doituong_id": str(row.doituong_id),
                "KOL": row.KOL,
                "ctnv_name": row.ctnv_name,
            }
            for row in donvi_doituong
        ]
        KOL = sum(item["KOL"] for item in formatted_result)
        ctnv_name_count = len(donvi_doituong)
        # count ctnv_id
        ctnv_id_counts = {}
        for item in formatted_result:
            ctnv_id = item["ctnv_name"]
            ctnv_id_counts[ctnv_id] = ctnv_id_counts.get(ctnv_id, 0) + 1
        # export output
        thongke_counts = {
            "KOL": KOL,
            "THEODOI": ctnv_name_count,
            "ctnv": [
                {"ctnv_name": ctnv_id, "count": count}
                for ctnv_id, count in ctnv_id_counts.items()
            ],
        }
        return thongke_counts

    # thống kê đơn vị
    def thongkedonvi(self, db: Session):
        json_data = []
        donvi_list = db.query(Donvi).all()
        for donvi in donvi_list:
            doituong = crud_thongke.thongkedonvi_doituong(db=db, donvi_id=donvi.id)
            hoinhom = crud_thongke.thongkedonvi_uid(db=db, donvi_id=donvi.id)
            output = {
                "donvi": donvi.name,
                "id": donvi.id,
                "hoinhom": hoinhom,
                "doituong": doituong,
            }
            json_data.append(output)
        return json_data

    # thống kê tính chất theo đonq vị
    def thongketinhchat(self, db: Session):
        data = (
            db.query(
                tinhchat.id.label("id"),
                tinhchat.name.label("name"),
                func.count(tinhchat.id).label("count"),
                tinhchat_hoinhom.uid.label("uid"),
                uid.name.label("uid_name"),
            )
            .join(tinhchat_hoinhom, tinhchat_hoinhom.tinhchat_id == tinhchat.id)
            .join(uid, uid.uid == tinhchat_hoinhom.uid)
            .filter(uid.Vaiao == False)
            .group_by(tinhchat.id, tinhchat_hoinhom.uid, uid.name)
            .all()
        )
        formatted_result = [
            {
                "id": row.id,
                "name": row.name,
                "count": row.count,
                "uid": row.uid,
                "uid_name": row.uid_name,
            }
            for row in data
        ]
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
                result.append(
                    {
                        "id": key[0],
                        "name": key[1],
                        "count": entry["count"],
                        "uids": [entry["uid_name"]],
                    }
                )
        return JSONResponse(content=result)

    # thongke by phanloai
    def thongkephanloai(self, db: Session):
        grouped_uid_names = (
            db.query(
                trangthai.id,
                trangthai.name,
                func.array_agg(uid.name),
                func.count(uid.trangthai_id).label("count"),
            )
            .join(uid, uid.trangthai_id == trangthai.id)
            .filter(uid.Vaiao == False)
            .group_by(trangthai.id, trangthai.name)
            .all())
        # Transforming results to JSON serializable format
        formatted_results = [
            {
                "trangthai_id": trangthai_id,
                "trangthai_name": trangthai_name,
                "uid_names": uid_names,
                "count": count,
            }
            for trangthai_id, trangthai_name, uid_names, count in grouped_uid_names
        ]

        return JSONResponse(content=formatted_results)
    def thongkectnv(self, db: Session):
        result = (db.query(donvi_hoinhom.CTNV_ID, ctnv.name.label('name') ,func.array_agg(uid.name).label('uid_name'),func.count(donvi_hoinhom.CTNV_ID).label('count_ctnv'))
                .join(ctnv, ctnv.id == donvi_hoinhom.CTNV_ID)
                .join(uid, donvi_hoinhom.uid==uid.uid)
                .group_by(donvi_hoinhom.CTNV_ID, ctnv.name)
                .filter(uid.Vaiao ==False)
                .all())
        formatted_results = [
            {
                "ctnv_id": row.CTNV_ID,
                "ctnv_name": row.name,
                "uid_name": row.uid_name,
                "count": row.count_ctnv,
            }
            for row in result
        ]

        return JSONResponse(content=formatted_results)
    
    def thongkedoituongctnv(self, db: Session):
        result = (db.query(Doituong_Donvi.CTNV_ID, ctnv.name.label('name') ,func.array_agg(Doituong.client_name).label('doituong_name'),func.count(Doituong_Donvi.CTNV_ID).label('count_ctnv'))
                .join(ctnv, ctnv.id == Doituong_Donvi.CTNV_ID)
                .join(Doituong, Doituong.id==Doituong_Donvi.doituong_id)
                .group_by(Doituong_Donvi.CTNV_ID, ctnv.name)
                .all())
        formatted_results = [
            {
                "ctnv_id": row.CTNV_ID,
                "ctnv_name": row.name,
                "doituong_name": row.doituong_name,
                "count": row.count_ctnv,
            }
            for row in result
        ]

        return JSONResponse(content=formatted_results)


            #  liệt kê uid thuộc đơn vị
    def details_uid(self, donvi_id: UUID4, db: Session):
        subquery = (
            db.query(uid.uid, func.max(uid.updated_at).label("max_updated_at"))
            .group_by(uid.uid)
            .subquery()
        )
        data = (
            (
                db.query(
                    uid.uid.label("uid"),
                    uid.name.label("name"),
                    uid.reaction.label("reaction"),
                    uid.SDT.label("SDT"),
                    uid.trangthai_id.label("trangthai_id"),
                    uid.type_id.label("type_id"),
                    uid.ghichu.label("ghichu"),
                    uid.Vaiao.label("Vaiao"),
                    uid.updated_at.label("updated_at"),
                    trangthai.name.label("trangthai_name"),
                    trangthai.color.label("trangthai_color"),
                    Donvi.name.label("donvi_name"),
                    ctnv.name.label("ctnv_name"),
                ).join(
                    subquery,
                    (uid.uid == subquery.c.uid)
                    & (uid.updated_at == subquery.c.max_updated_at),
                )
            )
            .join(trangthai, trangthai.id == uid.trangthai_id)
            .join(donvi_hoinhom, donvi_hoinhom.uid == uid.uid)
            .join(ctnv, donvi_hoinhom.CTNV_ID == ctnv.id)
            .join(Donvi, donvi_hoinhom.donvi_id == Donvi.id)
            .filter(donvi_hoinhom.donvi_id == donvi_id)
            .all()
        )
        formatted_result = [
            {
                "uid": row.uid,
                "name": row.name,
                "reaction": row.reaction,
                "SDT": row.SDT,
                "trangthai_id": row.trangthai_id,
                "type_id": row.type_id,
                "ghichu": row.ghichu,
                "Vaiao": row.Vaiao,
                "updated_at": str(row.updated_at),
                "trangthai_name": row.trangthai_name,
                "trangthai_color": row.trangthai_color,
                "donvi_name": row.donvi_name,
                "ctnv_name": row.ctnv_name,
            }
            for row in data
        ]
        formatted_result_as_dict = [dict(item) for item in formatted_result]
        return JSONResponse(content=formatted_result_as_dict)

    # liet ke doituong thuoc don vi

    def deatails_doituong(self, donvi_id: UUID4, db: Session):
        result = (
            db.query(Doituong)
            .join(Doituong_Donvi, Doituong.id == Doituong_Donvi.doituong_id)
            .filter(Doituong_Donvi.donvi_id == donvi_id)
            .all()
        )
        return result


crud_thongke = CRUDThongKe(tinhchat)
