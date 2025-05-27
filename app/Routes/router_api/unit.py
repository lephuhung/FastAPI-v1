from fastapi import APIRouter, Depends, HTTPException, Security
from typing import List
from app.schemas.unit import UnitCreate, UnitUpdate, Unit
from app.crud.crud_unit import unit
from app.Routes import deps
from sqlalchemy.orm import Session
from app import models
from pydantic import BaseModel
from sqlalchemy import func
from sqlalchemy.orm import aliased
from uuid import UUID

router = APIRouter(prefix="/units", tags=["Units"])

class UnitWithCount(BaseModel):
    id: UUID
    name: str
    user_count: int

@router.get("/", response_model=List[UnitWithCount])
def get_units_with_user_count(
    db: Session = Depends(deps.get_db),
):
    UserUnit = models.user_unit.UserUnit
    Unit = models.unit.Unit

    results = (
        db.query(
            Unit.id,
            Unit.name,
            func.count(UserUnit.user_id).label("user_count")
        )
        .outerjoin(UserUnit, UserUnit.unit_id == Unit.id)
        .group_by(Unit.id, Unit.name)
        .all()
    )
    return [
        {"id": r.id, "name": r.name, "user_count": r.user_count}
        for r in results
    ]

@router.post("/", response_model=Unit)
def create_unit(
    *,
    db: Session = Depends(deps.get_db),
    unit_in: UnitCreate,
    current_user = Security(deps.get_current_superadmin, scopes=[]),
):
    """
    Create new unit.
    """
    unit_obj = unit.create(db=db, obj_in=unit_in)
    return unit_obj

@router.put("/{id}", response_model=Unit)
def update_unit(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
    unit_in: UnitUpdate,
    current_user = Security(deps.get_current_superadmin, scopes=[]),
):
    """
    Update unit.
    """
    unit_obj = unit.get(db=db, id=id)
    if not unit_obj:
        raise HTTPException(status_code=404, detail="Unit not found")
    unit_obj = unit.update(db=db, db_obj=unit_obj, obj_in=unit_in)
    return unit_obj

@router.get("/{id}", response_model=Unit)
def get_unit(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
):
    """
    Get unit by ID.
    """
    unit_obj = unit.get(db=db, id=id)
    if not unit_obj:
        raise HTTPException(status_code=404, detail="Unit not found")
    return unit_obj

@router.delete("/{id}", response_model=Unit)
def delete_unit(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
    current_user = Security(deps.get_current_superadmin, scopes=[]),
):
    """
    Delete unit.
    """
    unit_obj = unit.get(db=db, id=id)
    if not unit_obj:
        raise HTTPException(status_code=404, detail="Unit not found")
    unit_obj = unit.remove(db=db, id=id)
    return unit_obj 