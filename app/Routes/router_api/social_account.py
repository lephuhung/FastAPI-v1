from fastapi import APIRouter, Depends, HTTPException, Security, Response
from typing import List, Any, Dict
from app.schemas.social_account import SocialAccountCreate, SocialAccountUpdate, SocialAccount, SocialAccountWithRelations
from app.crud.crud_social_account import social_account
from app.Routes import deps
from sqlalchemy.orm import Session
from app.crud.crud_unit import unit
from app.crud.crud_task import task
from app.models.unit import Unit
from app.models.task import Task
from app.models.account_type import AccountType
from app.models.social_account import SocialAccount as SocialAccountModel
from app.models.status import Status

router = APIRouter(prefix="/social-accounts", tags=["Social Accounts"])

def get_social_account_with_relations(account: SocialAccountModel, db: Session) -> Dict[str, Any]:
    """Get social account with related unit and task information."""
    account_dict = {
        'id': account.id,
        'uid': account.uid,
        'name': account.name,
        'reaction_count': account.reaction_count,
        'phone_number': account.phone_number,
        'status_id': account.status_id,
        'type_id': account.type_id,
        'note': account.note,
        'is_active': account.is_active,
        'created_at': account.created_at,
        'updated_at': account.updated_at
    }
    
    # Get status name
    status = db.query(Status).filter(Status.id == account.status_id).first()
    if status:
        account_dict['status_name'] = status.name
    
    # Get unit and task information from unit_groups
    if account.unit_groups:
        for unit_group in account.unit_groups:
            unit_data = unit.get(db=db, id=unit_group.unit_id)
            task_data = task.get(db=db, id=unit_group.task_id)
            if unit_data:
                account_dict['unit'] = {
                    'id': str(unit_data.id),
                    'name': unit_data.name
                }
            if task_data:
                account_dict['task'] = {
                    'id': task_data.id,
                    'name': task_data.name
                }
    
    return account_dict

@router.get("/", response_model=List[SocialAccountWithRelations])
async def get_social_accounts(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Retrieve social accounts with unit and task information.
    """
    social_accounts = social_account.get_multi(db, skip=skip, limit=limit)
    return [get_social_account_with_relations(account, db) for account in social_accounts]

@router.post("/", response_model=SocialAccount)
async def create_social_account(
    *,
    db: Session = Depends(deps.get_db),
    social_account_in: SocialAccountCreate,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Create new social account.
    """
    social_account_obj = social_account.create(db=db, obj_in=social_account_in)
    return social_account_obj

@router.put("/{uid}", response_model=SocialAccount)
async def update_social_account(
    *,
    db: Session = Depends(deps.get_db),
    uid: str,
    social_account_in: SocialAccountUpdate,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Update a social account.
    """
    social_account_obj = social_account.get_by_uid(db=db, uid=uid)
    if not social_account_obj:
        raise HTTPException(status_code=404, detail="Social account not found")
    social_account_obj = social_account.update(db=db, db_obj=social_account_obj, obj_in=social_account_in)
    return social_account_obj

@router.get("/admin-accounts", response_model=Dict[str, Any])
async def get_admin_accounts(
    db: Session = Depends(deps.get_db),
):
    """
    Get all active admin accounts (type 1, 2, 3) with only uid and name.
    Returns empty arrays for types with no accounts.
    """
    try:
        # Get accounts with type_id 1-- Facebook cá nhân
        type1_accounts = social_account.get_all_by_type_id(db=db, type_id=1) or []
        # Get accounts with type_id 2 -- Nhóm Facebook
        type2_accounts = social_account.get_all_by_type_id(db=db, type_id=2) or []
        # Get accounts with type_id 3 -- Fanpage Facebook/KOL
        type3_accounts = social_account.get_all_by_type_id(db=db, type_id=3) or []
        
        # Log the number of accounts found for each type
        print(f"Found {len(type1_accounts)} type 1 accounts")
        print(f"Found {len(type2_accounts)} type 2 accounts")
        print(f"Found {len(type3_accounts)} type 3 accounts")
        
        # Format results with only uid and name, filter active accounts
        all_accounts_type_1 = [{"uid": account.uid, "name": account.name} for account in type1_accounts if account.is_active]
        all_accounts_type_2 = [{"uid": account.uid, "name": account.name} for account in type2_accounts if account.is_active]
        all_accounts_type_3 = [{"uid": account.uid, "name": account.name} for account in type3_accounts if account.is_active]
        
        # Log the number of active accounts for each type
        print(f"Found {len(all_accounts_type_1)} active type 1 accounts")
        print(f"Found {len(all_accounts_type_2)} active type 2 accounts")
        print(f"Found {len(all_accounts_type_3)} active type 3 accounts")
        
        return {
            "data": [
                {"type_id": 1, "type_name": "Facebook cá nhân", "data": all_accounts_type_1},
                {"type_id": 2, "type_name": "Nhóm Facebook", "data": all_accounts_type_2},
                {"type_id": 3, "type_name": "Fanpage Facebook/KOL", "data": all_accounts_type_3}
            ]
        }
    except Exception as e:
        print(f"Error in get_admin_accounts: {str(e)}")
        # Return empty arrays for all types if there's an error
        return {
            "data": [
                {"type_id": 1, "type_name": "Facebook cá nhân", "data": []},
                {"type_id": 2, "type_name": "Nhóm Facebook", "data": []},
                {"type_id": 3, "type_name": "Fanpage Facebook/KOL", "data": []}
            ]
        }

@router.get("/relation-accounts", response_model=Dict[str, Any])
async def get_relation_accounts(
    db: Session = Depends(deps.get_db),
    # current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Get relation accounts (type 2, 3).
    """
    # Get accounts with type_id 2 -- Nhóm Facebook
    type2_accounts = social_account.get_all_by_type_id(db=db, type_id=2) or []
    # Get accounts with type_id 3 -- Fanpage Facebook/KOL
    type3_accounts = social_account.get_all_by_type_id(db=db, type_id=3) or []
    
    # Combine and format the results
    all_accounts_type_2 = []
    all_accounts_type_3 = []

    if type2_accounts:
        for account in type2_accounts:
            account_dict = get_social_account_with_relations(account, db)
            all_accounts_type_2.append(account_dict)
    
    if type3_accounts:
        for account in type3_accounts:
            account_dict = get_social_account_with_relations(account, db)
            all_accounts_type_3.append(account_dict)
    
    return {
        "data": [
            {"type_id": 2, "type_name": "Nhóm Facebook","data": all_accounts_type_2},
            {"type_id": 3, "type_name": "Fanpage Facebook/KOL","data": all_accounts_type_3}
        ]
    }

@router.get("/type/{type_id}", response_model=Dict[str, Any])
async def get_social_accounts_by_type(
    *,
    db: Session = Depends(deps.get_db),
    type_id: int,
    # current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Get social accounts by type ID with unit and task information.
    """
    social_accounts = social_account.get_all_by_type_id(db=db, type_id=type_id)
    
    # Get account type name
    account_type = db.query(AccountType).filter(AccountType.id == type_id).first()
    account_type_name = account_type.name if account_type else ""
    
    return {
        "account_type_name": account_type_name,
        "data": [get_social_account_with_relations(account, db) for account in social_accounts]
    }

@router.get("/status/{status_id}", response_model=List[SocialAccount])
async def get_social_accounts_by_status(
    *,
    db: Session = Depends(deps.get_db),
    status_id: int,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Get social accounts by status ID.
    """
    social_accounts = social_account.get_all_by_status_id(db=db, status_id=status_id)
    return social_accounts

@router.get("/{uid}", response_model=SocialAccountWithRelations)
async def get_social_account(
    *,
    db: Session = Depends(deps.get_db),
    uid: str,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Get social account by UID with unit and task information.
    """
    social_account_obj = social_account.get_by_uid(db=db, uid=uid)
    if not social_account_obj:
        raise HTTPException(status_code=404, detail="Social account not found")
    return get_social_account_with_relations(social_account_obj, db)

@router.delete("/{uid}", response_model=SocialAccount)
async def delete_social_account(
    *,
    db: Session = Depends(deps.get_db),
    uid: str,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Delete a social account.
    """
    social_account_obj = social_account.get_by_uid(db=db, uid=uid)
    if not social_account_obj:
        raise HTTPException(status_code=404, detail="Social account not found")
    social_account_obj = social_account.remove(db=db, id=social_account_obj.id)
    return social_account_obj 
