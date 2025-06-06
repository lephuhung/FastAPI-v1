from fastapi import APIRouter, Body, Depends, HTTPException, Security, Response
from typing import Annotated
from app.Routes import deps
from sqlalchemy.orm import Session
from pydantic import UUID4
from app.schemas.doituong_donvi import doituong_donviupdate, doituong_donvicreate
from app import crud
from app.crud.crud_doituong_donvi import crud_doituong_donvi
from app.models.doituong import Doituong
from app.schemas.doituong import doituongcreate, doituongupdate
from fastapi import Form

router = APIRouter(prefix="/doituong", tags=["Đối tượng"])


# get all doituong
@router.get("")
async def get_all(
    db: Session = Depends(deps.get_db),
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    data = crud.crud_doituong.get_doituong_with_ctnv(db=db)
    return data


# create a new Doituong
@router.post("/create")
async def create_doituong(data: doituongcreate,response: Response ,db: Session = Depends(deps.get_db)):
    try:
        doituong_format = data.get_doituong_instance()
        doituongoutDB = crud.crud_doituong.create(db=db, obj_in=doituong_format)
        doituong_donvi_instance = doituong_donvicreate(
            doituong_id=doituongoutDB.id,
            donvi_id=data.donvi_id,
            CTNV_ID=data.ctnv_id,
        )
        data = crud_doituong_donvi.create(db=db, obj_in=doituong_donvi_instance)
        db.commit()
        return doituongoutDB
    except Exception as e:
        db.rollback()
        response.status_code=444
        return {"message": "fail to created"}


@router.get("/view/{doituong_id}")
async def view_doituong(
    doituong_id: UUID4,
    db: Session = Depends(deps.get_db),
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    doituong = crud.crud_doituong.get_doituong_by_id(doituong_id=doituong_id, db=db)
    return doituong


# update not work yet
@router.post("/update/{doituong_id}")
async def update_doituong(
    doituong_id: UUID4,
    doituonginupdate: doituongupdate,
    response: Response,
    db: Session = Depends(deps.get_db),
):
    try:
        doituong_format = doituonginupdate.get_doituong_instance()
        doituong_donvi_result = crud.crud_doituong_donvi.get_doituong_by_doituong_id(doituong_id=doituong_id, db=db)
        update_doituong_donvi = doituong_donvicreate(
            doituong_id= doituong_id,
            CTNV_ID= doituonginupdate.ctnv_id,
            donvi_id = doituonginupdate.donvi_id
        )
        # Cập nhật lại code bổ sung thêm tách ctnv_id để cập nhập bảng donvi_doituong
        crud.crud_doituong_donvi.update(db=db, db_obj= doituong_donvi_result, obj_in=update_doituong_donvi)
        doituong = crud.crud_doituong.get_doituong_by_id(doituong_id=doituong_id, db=db)
        crud.crud_doituong.update(db=db, db_obj=doituong, obj_in=doituong_format)
        db.commit()
        return {"message": "success to updated"}
    except Exception as e:
        # raise HTTPException(status_code=500, detail= e)
        # print(e)
        db.rollback()
        response.status_code=444
        return {"message": "fail to updated"}


# get details doituong
@router.get("/details/{doituong_id}")
async def get_details(
    doituong_id: UUID4,
    db: Session = Depends(deps.get_db),
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    data = crud.crud_doituong.get_details(db=db, doituong_id=doituong_id)
    return data

@router.delete("/delete/{doituong_id}")
async def delete_doituongs(doituong_id: UUID4, response: Response ,db: Session = Depends(deps.get_db), current_user=Security(deps.get_current_active_user, scopes=[])):
    try:
        uid_has_delete = crud.crud_doituong.get_doituong_by_id(doituong_id=doituong_id, db=db)
        crud.crud_doituong.remove(id=uid_has_delete.id, db=db)
        return {"message": "successfully deleted"}
    except Exception as e:
        response.status_code=444
        return {"message": e}

@router.get("/test")
async def test_doituongs(db: Session = Depends(deps.get_db)):
    return crud.crud_doituong.get_doituong_with_ctnv(db=db)