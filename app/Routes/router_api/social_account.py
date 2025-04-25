from fastapi import APIRouter, Depends, HTTPException, Security, Response
from typing import List
from app.schemas.social_account import SocialAccountCreate, SocialAccountUpdate, SocialAccount
from app.crud.crud_social_account import social_account
from app.Routes import deps
from sqlalchemy.orm import Session

router = APIRouter(prefix="/social-accounts", tags=["Social Accounts"])


@router.get("/", response_model=List[SocialAccount])
async def get_social_accounts(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Retrieve social accounts.
    """
    social_accounts = social_account.get_multi(db, skip=skip, limit=limit)
    return social_accounts


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


@router.get("/{uid}", response_model=SocialAccount)
async def get_social_account(
    *,
    db: Session = Depends(deps.get_db),
    uid: str,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Get social account by UID.
    """
    social_account_obj = social_account.get_by_uid(db=db, uid=uid)
    if not social_account_obj:
        raise HTTPException(status_code=404, detail="Social account not found")
    return social_account_obj


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


@router.get("/type/{type_id}", response_model=List[SocialAccount])
async def get_social_accounts_by_type(
    *,
    db: Session = Depends(deps.get_db),
    type_id: int,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Get social accounts by type ID.
    """
    social_accounts = social_account.get_all_by_type_id(db=db, type_id=type_id)
    return social_accounts


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