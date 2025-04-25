from fastapi import APIRouter, Depends, HTTPException, Security
from typing import List
from app.schemas.unit import UnitCreate, UnitUpdate, Unit
from app.crud.crud_unit import unit
from app.Routes import deps
from sqlalchemy.orm import Session

router = APIRouter(prefix="/units", tags=["Units"])

@router.get("/", response_model=List[Unit])
async def get_units(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Retrieve units.
    """
    units = unit.get_multi(db, skip=skip, limit=limit)
    return units

@router.post("/", response_model=Unit)
async def create_unit(
    *,
    db: Session = Depends(deps.get_db),
    unit_in: UnitCreate,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Create new unit.
    """
    unit_obj = unit.create(db=db, obj_in=unit_in)
    return unit_obj

@router.put("/{id}", response_model=Unit)
async def update_unit(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    unit_in: UnitUpdate,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Update a unit.
    """
    unit_obj = unit.get(db=db, id=id)
    if not unit_obj:
        raise HTTPException(status_code=404, detail="Unit not found")
    unit_obj = unit.update(db=db, db_obj=unit_obj, obj_in=unit_in)
    return unit_obj

@router.get("/{id}", response_model=Unit)
async def get_unit(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Get unit by ID.
    """
    unit_obj = unit.get(db=db, id=id)
    if not unit_obj:
        raise HTTPException(status_code=404, detail="Unit not found")
    return unit_obj

@router.delete("/{id}", response_model=Unit)
async def delete_unit(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Delete a unit.
    """
    unit_obj = unit.get(db=db, id=id)
    if not unit_obj:
        raise HTTPException(status_code=404, detail="Unit not found")
    unit_obj = unit.remove(db=db, id=id)
    return unit_obj 