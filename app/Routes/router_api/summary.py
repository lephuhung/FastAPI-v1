from fastapi import APIRouter, Depends, Security
from typing import Dict, Any, List
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.Routes import deps
from app.models.unit import Unit
from app.models.characteristic import Characteristic
from app.models.task import Task
from app.models.social_account import SocialAccount
from app.models.unit_group import UnitGroup
from app.models.account_type import AccountType
from app.models.group_characteristic import GroupCharacteristic

router = APIRouter(prefix="/summary", tags=["Summary"])

@router.get("/unit/{unit_id}", response_model=Dict[str, Any])
async def get_unit_summary(
    *,
    db: Session = Depends(deps.get_db),
    unit_id: int,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Get summary statistics for a specific unit including:
    - Characteristics by characteristic_id with names
    - Tasks by task_id with names
    - Social accounts by type with names
    """
    # Get unit information
    unit = db.query(Unit).filter(Unit.id == unit_id).first()
    if not unit:
        return {"error": "Unit not found"}

    # Get characteristics count by characteristic_id with names
    characteristics_by_id = db.query(
        Characteristic.id,
        Characteristic.name,
        func.count(Characteristic.id).label('count')
    )\
        .join(GroupCharacteristic, GroupCharacteristic.characteristic_id == Characteristic.id)\
        .join(UnitGroup, UnitGroup.social_account_uid == GroupCharacteristic.social_account_uid)\
        .filter(UnitGroup.unit_id == unit_id)\
        .group_by(Characteristic.id, Characteristic.name)\
        .all()

    # Get tasks count by task_id with names
    tasks_by_id = db.query(
        Task.id,
        Task.name,
        func.count(Task.id).label('count')
    )\
        .join(UnitGroup, UnitGroup.task_id == Task.id)\
        .filter(UnitGroup.unit_id == unit_id)\
        .group_by(Task.id, Task.name)\
        .all()

    # Get social accounts by type with names
    social_accounts_by_type = db.query(
        SocialAccount.type_id,
        AccountType.name,
        func.count(SocialAccount.id).label('count')
    )\
        .join(UnitGroup, UnitGroup.social_account_uid == SocialAccount.uid)\
        .join(AccountType, AccountType.id == SocialAccount.type_id)\
        .filter(UnitGroup.unit_id == unit_id)\
        .group_by(SocialAccount.type_id, AccountType.name)\
        .all()

    # Format social accounts by type
    social_accounts_summary = {}
    for type_id, name, count in social_accounts_by_type:
        social_accounts_summary[f"type_{type_id}"] = {
            "name": name,
            "count": count
        }

    return {
        "unit": {
            "id": unit.id,
            "name": unit.name
        },
        "statistics": {
            "characteristics": {
                str(cid): {
                    "name": name,
                    "count": count
                } for cid, name, count in characteristics_by_id
            },
            "tasks": {
                str(tid): {
                    "name": name,
                    "count": count
                } for tid, name, count in tasks_by_id
            },
            "social_accounts": social_accounts_summary
        }
    }

@router.get("/units", response_model=List[Dict[str, Any]])
async def get_all_units_summary(
    db: Session = Depends(deps.get_db),
    # current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Get summary statistics for all units
    """
    units = db.query(Unit).all()
    summaries = []

    for unit in units:
        # Get characteristics count by characteristic_id with names
        characteristics_by_id = db.query(
            Characteristic.id,
            Characteristic.name,
            func.count(Characteristic.id).label('count')
        )\
            .join(GroupCharacteristic, GroupCharacteristic.characteristic_id == Characteristic.id)\
            .join(UnitGroup, UnitGroup.social_account_uid == GroupCharacteristic.social_account_uid)\
            .filter(UnitGroup.unit_id == unit.id)\
            .group_by(Characteristic.id, Characteristic.name)\
            .all()

        # Get tasks count by task_id with names
        tasks_by_id = db.query(
            Task.id,
            Task.name,
            func.count(Task.id).label('count')
        )\
            .join(UnitGroup, UnitGroup.task_id == Task.id)\
            .filter(UnitGroup.unit_id == unit.id)\
            .group_by(Task.id, Task.name)\
            .all()

        # Get social accounts by type with names
        social_accounts_by_type = db.query(
            SocialAccount.type_id,
            AccountType.name,
            func.count(SocialAccount.id).label('count')
        )\
            .join(UnitGroup, UnitGroup.social_account_uid == SocialAccount.uid)\
            .join(AccountType, AccountType.id == SocialAccount.type_id)\
            .filter(UnitGroup.unit_id == unit.id)\
            .group_by(SocialAccount.type_id, AccountType.name)\
            .all()

        # Format social accounts by type
        social_accounts_summary = {}
        for type_id, name, count in social_accounts_by_type:
            social_accounts_summary[f"type_{type_id}"] = {
                "name": name,
                "count": count
            }

        summaries.append({
            "unit": {
                "id": unit.id,
                "name": unit.name
            },
            "statistics": {
                "characteristics": {
                    str(cid): {
                        "name": name,
                        "count": count
                    } for cid, name, count in characteristics_by_id
                },
                "tasks": {
                    str(tid): {
                        "name": name,
                        "count": count
                    } for tid, name, count in tasks_by_id
                },
                "social_accounts": social_accounts_summary
            }
        })

    return summaries 