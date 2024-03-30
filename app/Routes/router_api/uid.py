from fastapi import APIRouter, Body, Depends, HTTPException, Security, Response
from typing import Annotated
from app.schemas.uid import uidCreate, uidUpdate, uid
from app.schemas.donvi_hoinhom import hoinhom_donvicreate
from app.schemas.tinhchat_hoinhom import tinhchat_hoinhomcreate
from app.crud.crud_hoinhom_donvi import crud_donvihoinhom
from app.crud.crud_tinhchat_hoinhom import crud_tinhchat_hoinhom
from app.crud import crud_uid
from app.crud import crud_uid
from app.Routes import deps
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from pydantic import UUID4

router = APIRouter(prefix="/uid", tags=["UID"])


@router.get("/get-last/{id}")
async def getlast(id: str, db: Session = Depends(deps.get_db)):
    data = crud_uid.get_last_uid_by_id(id=id, db=db)
    return data


@router.get("/get-history/{uid_uid}")
async def gethistory(uid_uid: str, db: Session = Depends(deps.get_db)):
    data = crud_uid.get_all_by_uid(uid_uid=uid_uid, db=db)
    return data


@router.post("/create")
async def create(data: uidCreate, response: Response,db: Session = Depends(deps.get_db)):
    try:
        uid_format = data.get_uid_instance()
        checker = crud_uid.get_uid_by_uid(db=db, uid_id= uid_format.uid)
        if checker != None:
            response.status_code = 444
            return {"message": "uid already exists"}
        else:
            uid_result = crud_uid.create(db=db, obj_in=uid_format)
            instance = hoinhom_donvicreate(
                uid=uid_result.uid, donvi_id=data.donvi_id, CTNV_ID=data.ctnv_id
            )
            result = crud_donvihoinhom.create(db=db, obj_in=instance)
            tinchathoinhom_ins= tinhchat_hoinhomcreate(uid = uid_result.uid, tinhchat_id=data.tinhchat_id)
            result2 = crud_tinhchat_hoinhom.create(db=db, obj_in=tinchathoinhom_ins)
            return resul2
    except Exception as e:
        db.rollback()
        # response.status_code=444
        # print(e)
        # return {"message": "fail to created"}
        raise HTTPException(status_code=400, details=e)


@router.put("/update/{id}")
async def update(id: str, uid_data: uidUpdate, db: Session = Depends(deps.get_db)):
    try:
        uid_format = uid_data.get_uid_instance()
        uid_has_update = crud_uid.get_uid_by_uid(uid_id=id, db=db)
        data = crud_uid.update(obj_in=uid_format, db_obj=uid_has_update, db=db)
        donvihoinhom = crud_donvihoinhom.find_donvi_hoinhom(
            db=db, id= uid_data.id_hoinhomdonvi
        )

        update_donvihoinhom = hoinhom_donvicreate(
            uid=id,
            donvi_id=str(uid_data.donvi_id),
            CTNV_ID=int(uid_data.ctnv_id),
        )
        print(donvihoinhom)
        print(update_donvihoinhom)
        donvihoinhom_update = crud_donvihoinhom.update(obj_in=update_donvihoinhom, db_obj=donvihoinhom, db=db)
        return {}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=e)


@router.delete("/delete/{id}")
async def delete(id: str, db: Session = Depends(deps.get_db)):
    try:
        uid_has_delete = crud_uid.delete_uid(id=id, db=db)
        crud_uid.remove(id=uid_has_delete.id, db=db)
        return {"message": "successfully deleted"}
    except Exception as e:
        return {"message": e}


@router.get("/get-facebook")
async def get_facebook(
    type_id: int = 4,
    db: Session = Depends(deps.get_db),
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    facebook_data = crud_uid.get_all_by_type_id(type_id=type_id, db=db)
    return facebook_data


@router.get("/get-groups")
async def get_groups(
    type_id: int = 0,
    db: Session = Depends(deps.get_db),
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    facebook_data = crud_uid.get_all_by_type_id(type_id=type_id, db=db)
    return facebook_data


@router.get("/get-pages")
async def get_pages(
    type_id: int = 3,
    db: Session = Depends(deps.get_db),
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    facebook_data = crud_uid.get_all_by_type_id(type_id=type_id, db=db)
    return facebook_data
