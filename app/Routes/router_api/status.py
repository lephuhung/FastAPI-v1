from fastapi import APIRouter, Depends, HTTPException, Security
from typing import List
from app.schemas.status import StatusCreate, StatusUpdate, Status
from app.crud.crud_status import status
from app.Routes import deps
from sqlalchemy.orm import Session
from app import crud, schemas

router = APIRouter(prefix="/statuses", tags=["Statuses"])

@router.get("/", response_model=List[Status])
def get_statuses(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
):
    """
    Get all statuses.
    """
    statuses = crud.status.get_multi(db, skip=skip, limit=limit)
    return statuses

@router.post("/", response_model=Status)
def create_status(
    *,
    db: Session = Depends(deps.get_db),
    status_in: StatusCreate,
    current_user = Security(deps.get_current_superadmin, scopes=[]),
):
    """
    Create new status.
    """
    status = crud.status.create(db, obj_in=status_in)
    return status

@router.put("/{id}", response_model=Status)
def update_status(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    status_in: StatusUpdate,
    current_user = Security(deps.get_current_superadmin, scopes=[]),
):
    """
    Update status.
    """
    status = crud.status.get(db, id=id)
    if not status:
        raise HTTPException(status_code=404, detail="Status not found")
    status = crud.status.update(db, db_obj=status, obj_in=status_in)
    return status

@router.get("/{id}", response_model=Status)
def get_status(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
):
    """
    Get status by ID.
    """
    status = crud.status.get(db, id=id)
    if not status:
        raise HTTPException(status_code=404, detail="Status not found")
    return status

@router.delete("/{id}", response_model=Status)
def delete_status(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user = Security(deps.get_current_superadmin, scopes=[]),
):
    """
    Delete status.
    """
    status = crud.status.get(db, id=id)
    if not status:
        raise HTTPException(status_code=404, detail="Status not found")
    status = crud.status.remove(db, id=id)
    return status 