from fastapi import APIRouter, Depends, HTTPException, Security
from typing import List
from app.schemas.administrator import AdministratorCreate, AdministratorUpdate, Administrator
from app.crud.crud_administrator import administrator
from app.Routes import deps
from sqlalchemy.orm import Session

router = APIRouter(prefix="/administrators", tags=["Administrators"])

@router.get("/", response_model=List[Administrator])
async def get_administrators(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Retrieve administrators.
    """
    administrators = administrator.get_multi(db, skip=skip, limit=limit)
    return administrators

@router.post("/", response_model=Administrator)
async def create_administrator(
    *,
    db: Session = Depends(deps.get_db),
    administrator_in: AdministratorCreate,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Create new administrator.
    """
    administrator_obj = administrator.create(db=db, obj_in=administrator_in)
    return administrator_obj

@router.put("/{id}", response_model=Administrator)
async def update_administrator(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    administrator_in: AdministratorUpdate,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Update an administrator.
    """
    administrator_obj = administrator.get(db=db, id=id)
    if not administrator_obj:
        raise HTTPException(status_code=404, detail="Administrator not found")
    administrator_obj = administrator.update(db=db, db_obj=administrator_obj, obj_in=administrator_in)
    return administrator_obj

@router.get("/{id}", response_model=Administrator)
async def get_administrator(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Get administrator by ID.
    """
    administrator_obj = administrator.get(db=db, id=id)
    if not administrator_obj:
        raise HTTPException(status_code=404, detail="Administrator not found")
    return administrator_obj

@router.delete("/{id}", response_model=Administrator)
async def delete_administrator(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Delete an administrator.
    """
    administrator_obj = administrator.get(db=db, id=id)
    if not administrator_obj:
        raise HTTPException(status_code=404, detail="Administrator not found")
    administrator_obj = administrator.remove(db=db, id=id)
    return administrator_obj 