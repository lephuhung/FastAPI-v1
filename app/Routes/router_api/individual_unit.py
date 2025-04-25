from fastapi import APIRouter, Depends, HTTPException, Security
from typing import List
from app.schemas.individual_unit import IndividualUnitCreate, IndividualUnitUpdate, IndividualUnit
from app.crud.crud_individual_unit import individual_unit
from app.Routes import deps
from sqlalchemy.orm import Session

router = APIRouter(prefix="/individual-units", tags=["Individual Units"])

@router.get("/", response_model=List[IndividualUnit])
async def get_individual_units(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Retrieve individual units.
    """
    individual_units = individual_unit.get_multi(db, skip=skip, limit=limit)
    return individual_units

@router.post("/", response_model=IndividualUnit)
async def create_individual_unit(
    *,
    db: Session = Depends(deps.get_db),
    individual_unit_in: IndividualUnitCreate,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Create new individual unit.
    """
    individual_unit_obj = individual_unit.create(db=db, obj_in=individual_unit_in)
    return individual_unit_obj

@router.put("/{id}", response_model=IndividualUnit)
async def update_individual_unit(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    individual_unit_in: IndividualUnitUpdate,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Update an individual unit.
    """
    individual_unit_obj = individual_unit.get(db=db, id=id)
    if not individual_unit_obj:
        raise HTTPException(status_code=404, detail="Individual unit not found")
    individual_unit_obj = individual_unit.update(db=db, db_obj=individual_unit_obj, obj_in=individual_unit_in)
    return individual_unit_obj

@router.get("/{id}", response_model=IndividualUnit)
async def get_individual_unit(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Get individual unit by ID.
    """
    individual_unit_obj = individual_unit.get(db=db, id=id)
    if not individual_unit_obj:
        raise HTTPException(status_code=404, detail="Individual unit not found")
    return individual_unit_obj

@router.delete("/{id}", response_model=IndividualUnit)
async def delete_individual_unit(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Delete an individual unit.
    """
    individual_unit_obj = individual_unit.get(db=db, id=id)
    if not individual_unit_obj:
        raise HTTPException(status_code=404, detail="Individual unit not found")
    individual_unit_obj = individual_unit.remove(db=db, id=id)
    return individual_unit_obj 