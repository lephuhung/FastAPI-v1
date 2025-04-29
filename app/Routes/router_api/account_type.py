from fastapi import APIRouter, Depends, HTTPException, Security
from typing import List
from app.schemas.account_type import AccountTypeCreate, AccountTypeUpdate, AccountType
from app.crud.crud_account_type import account_type
from app.Routes import deps
from sqlalchemy.orm import Session

router = APIRouter(prefix="/account-types", tags=["Account Types"])

@router.get("/public", response_model=List[AccountType])
async def get_public_account_types(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
):
    """
    Retrieve public account types without authentication.
    """
    account_types = account_type.get_multi(db, skip=skip, limit=limit)
    return account_types

@router.get("/", response_model=List[AccountType])
async def get_account_types(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Retrieve account types.
    """
    account_types = account_type.get_multi(db, skip=skip, limit=limit)
    return account_types

@router.post("/", response_model=AccountType)
async def create_account_type(
    *,
    db: Session = Depends(deps.get_db),
    account_type_in: AccountTypeCreate,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Create new account type.
    """
    account_type_obj = account_type.create(db=db, obj_in=account_type_in)
    return account_type_obj

@router.put("/{id}", response_model=AccountType)
async def update_account_type(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    account_type_in: AccountTypeUpdate,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Update an account type.
    """
    account_type_obj = account_type.get(db=db, id=id)
    if not account_type_obj:
        raise HTTPException(status_code=404, detail="Account type not found")
    account_type_obj = account_type.update(db=db, db_obj=account_type_obj, obj_in=account_type_in)
    return account_type_obj

@router.get("/{id}", response_model=AccountType)
async def get_account_type(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Get account type by ID.
    """
    account_type_obj = account_type.get(db=db, id=id)
    if not account_type_obj:
        raise HTTPException(status_code=404, detail="Account type not found")
    return account_type_obj

@router.delete("/{id}", response_model=AccountType)
async def delete_account_type(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Delete an account type.
    """
    account_type_obj = account_type.get(db=db, id=id)
    if not account_type_obj:
        raise HTTPException(status_code=404, detail="Account type not found")
    account_type_obj = account_type.remove(db=db, id=id)
    return account_type_obj 