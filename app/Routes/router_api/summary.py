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
from app.models.individual import Individual
from app.models.individual_unit import IndividualUnit
from app.models.individual_social_account import IndividualSocialAccount

router = APIRouter(prefix="/summary", tags=["Summary"])

@router.get("/social-accounts-unit/{unit_id}", response_model=Dict[str, Any])
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

@router.get("/social-accounts-units", response_model=List[Dict[str, Any]])
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

@router.get("/individuals-units", response_model=List[Dict[str, Any]])
async def get_all_individuals_summary(
    db: Session = Depends(deps.get_db),
    # current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Get summary statistics for all units showing:
    - Number of individuals by task_id
    - Number of individuals by characteristic_id
    - Number of KOLs
    """
    units = db.query(Unit).all()
    summaries = []

    for unit in units:
        # Get individuals count by task_id for this unit
        tasks_by_id = db.query(
            Task.id,
            Task.name,
            func.count(Individual.id).label('count')
        )\
            .join(IndividualUnit, IndividualUnit.task_id == Task.id)\
            .join(Individual, Individual.id == IndividualUnit.individual_id)\
            .filter(IndividualUnit.unit_id == unit.id)\
            .group_by(Task.id, Task.name)\
            .all()

        # Get individuals count by characteristic_id for this unit
        characteristics_by_id = db.query(
            Characteristic.id,
            Characteristic.name,
            func.count(Individual.id).label('count')
        )\
            .join(GroupCharacteristic, GroupCharacteristic.characteristic_id == Characteristic.id)\
            .join(IndividualSocialAccount, IndividualSocialAccount.social_account_uid == GroupCharacteristic.social_account_uid)\
            .join(Individual, Individual.id == IndividualSocialAccount.individual_id)\
            .join(IndividualUnit, IndividualUnit.individual_id == Individual.id)\
            .filter(IndividualUnit.unit_id == unit.id)\
            .group_by(Characteristic.id, Characteristic.name)\
            .all()

        # Get KOL count for this unit
        kol_count = db.query(func.count(Individual.id))\
            .join(IndividualUnit, IndividualUnit.individual_id == Individual.id)\
            .filter(IndividualUnit.unit_id == unit.id, Individual.is_kol == True)\
            .scalar()

        summaries.append({
            "unit": {
                "id": unit.id,
                "name": unit.name
            },
            "statistics": {
                "tasks": {
                    str(tid): {
                        "name": name,
                        "count": count
                    } for tid, name, count in tasks_by_id
                },
                "characteristics": {
                    str(cid): {
                        "name": name,
                        "count": count
                    } for cid, name, count in characteristics_by_id
                },
                "kols": {
                    "name": "KOL",
                    "count": kol_count
                }
            }
        })

    return summaries

@router.get("/individual-unit/{individual_id}", response_model=Dict[str, Any])
async def get_individual_summary(
    *,
    db: Session = Depends(deps.get_db),
    individual_id: int,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Get summary statistics for a specific individual including:
    - Number of individuals by task_id for each unit
    - Number of individuals by characteristic_id for each unit
    - Number of KOLs
    """
    # Get individual information
    individual = db.query(Individual).filter(Individual.id == individual_id).first()
    if not individual:
        return {"error": "Individual not found"}

    # Get units that this individual belongs to
    units = db.query(Unit).join(IndividualUnit, IndividualUnit.unit_id == Unit.id)\
        .filter(IndividualUnit.individual_id == individual_id)\
        .distinct()\
        .all()

    unit_summaries = []
    for unit in units:
        # Get individuals count by task_id for this unit
        tasks_by_id = db.query(
            Task.id,
            Task.name,
            func.count(Individual.id).label('count')
        )\
            .join(IndividualUnit, IndividualUnit.task_id == Task.id)\
            .join(Individual, Individual.id == IndividualUnit.individual_id)\
            .filter(IndividualUnit.unit_id == unit.id)\
            .group_by(Task.id, Task.name)\
            .all()

        # Get individuals count by characteristic_id for this unit
        characteristics_by_id = db.query(
            Characteristic.id,
            Characteristic.name,
            func.count(Individual.id).label('count')
        )\
            .join(GroupCharacteristic, GroupCharacteristic.characteristic_id == Characteristic.id)\
            .join(IndividualSocialAccount, IndividualSocialAccount.social_account_uid == GroupCharacteristic.social_account_uid)\
            .join(Individual, Individual.id == IndividualSocialAccount.individual_id)\
            .join(IndividualUnit, IndividualUnit.individual_id == Individual.id)\
            .filter(IndividualUnit.unit_id == unit.id)\
            .group_by(Characteristic.id, Characteristic.name)\
            .all()

        # Get KOL count for this unit
        kol_count = db.query(func.count(Individual.id))\
            .join(IndividualUnit, IndividualUnit.individual_id == Individual.id)\
            .filter(IndividualUnit.unit_id == unit.id, Individual.is_kol == True)\
            .scalar()

        unit_summaries.append({
            "unit": {
                "id": unit.id,
                "name": unit.name
            },
            "statistics": {
                "tasks": {
                    str(tid): {
                        "name": name,
                        "count": count
                    } for tid, name, count in tasks_by_id
                },
                "characteristics": {
                    str(cid): {
                        "name": name,
                        "count": count
                    } for cid, name, count in characteristics_by_id
                },
                "kols": {
                    "name": "KOL",
                    "count": kol_count
                }
            }
        })

    return {
        "individual": {
            "id": individual.id,
            "name": individual.name
        },
        "unit_summaries": unit_summaries
    } 