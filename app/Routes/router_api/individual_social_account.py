from fastapi import APIRouter, Depends, HTTPException, Security
from typing import List
from app.schemas.individual_social_account import IndividualSocialAccountCreate, IndividualSocialAccountUpdate, IndividualSocialAccount
from app.crud.crud_individual_social_account import individual_social_account
from app.Routes import deps
from sqlalchemy.orm import Session

router = APIRouter(prefix="/individual-social-accounts", tags=["Individual Social Accounts"])

@router.get("/", response_model=List[IndividualSocialAccount])
async def get_individual_social_accounts(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Retrieve individual social accounts.
    """
    individual_social_accounts = individual_social_account.get_multi(db, skip=skip, limit=limit)
    return individual_social_accounts

@router.post("/", response_model=IndividualSocialAccount)
async def create_individual_social_account(
    *,
    db: Session = Depends(deps.get_db),
    individual_social_account_in: IndividualSocialAccountCreate,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Create new individual social account.
    """
    individual_social_account_obj = individual_social_account.create(db=db, obj_in=individual_social_account_in)
    return individual_social_account_obj

@router.put("/{id}", response_model=IndividualSocialAccount)
async def update_individual_social_account(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    individual_social_account_in: IndividualSocialAccountUpdate,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Update an individual social account.
    """
    individual_social_account_obj = individual_social_account.get(db=db, id=id)
    if not individual_social_account_obj:
        raise HTTPException(status_code=404, detail="Individual social account not found")
    individual_social_account_obj = individual_social_account.update(db=db, db_obj=individual_social_account_obj, obj_in=individual_social_account_in)
    return individual_social_account_obj

@router.get("/{id}", response_model=IndividualSocialAccount)
async def get_individual_social_account(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Get individual social account by ID.
    """
    individual_social_account_obj = individual_social_account.get(db=db, id=id)
    if not individual_social_account_obj:
        raise HTTPException(status_code=404, detail="Individual social account not found")
    return individual_social_account_obj

@router.delete("/{id}", response_model=IndividualSocialAccount)
async def delete_individual_social_account(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Delete an individual social account.
    """
    individual_social_account_obj = individual_social_account.get(db=db, id=id)
    if not individual_social_account_obj:
        raise HTTPException(status_code=404, detail="Individual social account not found")
    individual_social_account_obj = individual_social_account.remove(db=db, id=id)
    return individual_social_account_obj 