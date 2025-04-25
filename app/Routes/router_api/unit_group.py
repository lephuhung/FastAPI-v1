from fastapi import APIRouter, Depends, HTTPException, Security
from typing import List
from app.schemas.unit_group import UnitGroupCreate, UnitGroupUpdate, UnitGroup
from app.crud.crud_unit_group import unit_group
from app.Routes import deps
from sqlalchemy.orm import Session

router = APIRouter(prefix="/unit-groups", tags=["Unit Groups"])

@router.get("/", response_model=List[UnitGroup])
async def get_unit_groups(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Retrieve unit groups.
    """
    unit_groups = unit_group.get_multi(db, skip=skip, limit=limit)
    return unit_groups

@router.post("/", response_model=UnitGroup)
async def create_unit_group(
    *,
    db: Session = Depends(deps.get_db),
    unit_group_in: UnitGroupCreate,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Create new unit group.
    """
    unit_group_obj = unit_group.create(db=db, obj_in=unit_group_in)
    return unit_group_obj

@router.put("/{id}", response_model=UnitGroup)
async def update_unit_group(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    unit_group_in: UnitGroupUpdate,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Update a unit group.
    """
    unit_group_obj = unit_group.get(db=db, id=id)
    if not unit_group_obj:
        raise HTTPException(status_code=404, detail="Unit group not found")
    unit_group_obj = unit_group.update(db=db, db_obj=unit_group_obj, obj_in=unit_group_in)
    return unit_group_obj

@router.get("/{id}", response_model=UnitGroup)
async def get_unit_group(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Get unit group by ID.
    """
    unit_group_obj = unit_group.get(db=db, id=id)
    if not unit_group_obj:
        raise HTTPException(status_code=404, detail="Unit group not found")
    return unit_group_obj

@router.delete("/{id}", response_model=UnitGroup)
async def delete_unit_group(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Delete a unit group.
    """
    unit_group_obj = unit_group.get(db=db, id=id)
    if not unit_group_obj:
        raise HTTPException(status_code=404, detail="Unit group not found")
    unit_group_obj = unit_group.remove(db=db, id=id)
    return unit_group_obj 