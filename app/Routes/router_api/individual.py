from fastapi import APIRouter, Depends, HTTPException, Security
from typing import List
from app.schemas.individual import IndividualCreate, IndividualUpdate, Individual
from app.crud.crud_individual import individual
from app.Routes import deps
from sqlalchemy.orm import Session

router = APIRouter(prefix="/individuals", tags=["Individuals"])


@router.get("/", response_model=List[Individual])
async def get_individuals(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Retrieve individuals.
    """
    individuals = individual.get_multi(db, skip=skip, limit=limit)
    return individuals


@router.post("/", response_model=Individual)
async def create_individual(
    *,
    db: Session = Depends(deps.get_db),
    individual_in: IndividualCreate,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Create new individual.
    """
    individual_obj = individual.create(db=db, obj_in=individual_in)
    return individual_obj


@router.put("/{id}", response_model=Individual)
async def update_individual(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    individual_in: IndividualUpdate,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Update an individual.
    """
    individual_obj = individual.get(db=db, id=id)
    if not individual_obj:
        raise HTTPException(status_code=404, detail="Individual not found")
    individual_obj = individual.update(db=db, db_obj=individual_obj, obj_in=individual_in)
    return individual_obj


@router.get("/{id}", response_model=Individual)
async def get_individual(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Get individual by ID.
    """
    individual_obj = individual.get(db=db, id=id)
    if not individual_obj:
        raise HTTPException(status_code=404, detail="Individual not found")
    return individual_obj


@router.delete("/{id}", response_model=Individual)
async def delete_individual(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Delete an individual.
    """
    individual_obj = individual.get(db=db, id=id)
    if not individual_obj:
        raise HTTPException(status_code=404, detail="Individual not found")
    individual_obj = individual.remove(db=db, id=id)
    return individual_obj 