from fastapi import APIRouter, Body, Depends, HTTPException, Security, Response
from typing import Annotated
from app.schemas.social_account import SocialAccountCreate, SocialAccountUpdate, SocialAccount
from app.schemas.unit_group import UnitGroupCreate
from app.schemas.group_characteristic import GroupCharacteristicCreate
from app.crud.crud_social_account import social_account
from app.crud.crud_unit_group import unit_group
from app.crud.crud_group_characteristic import group_characteristic
from app.Routes import deps
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from pydantic import UUID4

router = APIRouter(prefix="/uid", tags=["UID"])


@router.get("/get-last/{id}")
async def getlast(id: str, db: Session = Depends(deps.get_db)):
    data = social_account.get_last_by_id(id=id, db=db)
    return data


@router.get("/get-history/{uid_uid}")
async def gethistory(uid_uid: str, db: Session = Depends(deps.get_db)):
    data = social_account.get_all_by_uid(uid_uid=uid_uid, db=db)
    return data


@router.post("/create")
async def create(data: SocialAccountCreate, response: Response, db: Session = Depends(deps.get_db)):
    try:
        social_account_format = data.get_social_account_instance()
        checker = social_account.get_by_uid(db=db, uid=social_account_format.uid)
        if checker is not None:
            response.status_code = 444
            return {"message": "uid already exists"}
        else:
            social_account_result = social_account.create(db=db, obj_in=social_account_format)
            instance = UnitGroupCreate(
                social_account_uid=social_account_result.uid,
                unit_id=data.unit_id,
                task_id=data.task_id
            )
            result = unit_group.create(db=db, obj_in=instance)
            characteristic_instance = GroupCharacteristicCreate(
                social_account_uid=social_account_result.uid,
                characteristic_id=data.characteristic_id
            )
            result2 = group_characteristic.create(db=db, obj_in=characteristic_instance)
            db.commit()
            return result2
    except Exception as e:
        db.rollback()
        response.status_code = 444
        return {"message": "fail to created"}


@router.put("/update/{id}")
async def update(id: str, social_account_data: SocialAccountUpdate, response: Response, db: Session = Depends(deps.get_db)):
    try:
        social_account_format = social_account_data.get_social_account_instance()
        social_account_has_update = social_account.get_by_uid(uid=id, db=db)
        data = social_account.update(obj_in=social_account_format, db_obj=social_account_has_update, db=db)
        unit_group_obj = unit_group.find_by_social_account_uid(
            db=db, social_account_uid=id
        )

        update_unit_group = UnitGroupCreate(
            social_account_uid=id,
            unit_id=str(social_account_data.unit_id),
            task_id=int(social_account_data.task_id),
        )
        unit_group_update = unit_group.update(obj_in=update_unit_group, db_obj=unit_group_obj, db=db)
        db.commit()
        return unit_group_update
    except Exception as e:
        db.rollback()
        response.status_code = 444
        return {"message": "fail to created"}


@router.delete("/delete/{id}")
async def delete(id: str, db: Session = Depends(deps.get_db)):
    try:
        social_account_has_delete = social_account.delete_by_uid(uid=id, db=db)
        social_account.remove(id=social_account_has_delete.id, db=db)
        return {"message": "successfully deleted"}
    except Exception as e:
        return {"message": e}


@router.get("/get-facebook")
async def get_facebook(
    type_id: int = 2,
    db: Session = Depends(deps.get_db),
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    facebook_data = social_account.get_all_by_type_id(type_id=type_id, db=db)
    return facebook_data


@router.get("/get-groups")
async def get_groups(
    type_id: int = 1,
    db: Session = Depends(deps.get_db),
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    facebook_data = social_account.get_all_by_type_id(type_id=type_id, db=db)
    return facebook_data


@router.get("/get-pages")
async def get_pages(
    type_id: int = 3,
    db: Session = Depends(deps.get_db),
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    facebook_data = social_account.get_all_by_type_id(type_id=type_id, db=db)
    return facebook_data


@router.get("/get-vaiao")
async def get_vaiao(
    db: Session = Depends(deps.get_db),
    vaiao: bool = True,
):
    vaiao_data = social_account.get_by_is_active(is_active=vaiao, db=db)
    return vaiao_data


@router.get("/get-uid")
async def get_uid(
    db: Session = Depends(deps.get_db),
    vaiao: bool = False,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    vaiao_data = social_account.get_by_is_active(is_active=vaiao, db=db)
    return vaiao_data


@router.get("/get-page-group")
async def get_pages(
    db: Session = Depends(deps.get_db),
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    page_group_data = social_account.get_all_by_page_group(db=db, type_group=0, type_page=3)
    return page_group_data