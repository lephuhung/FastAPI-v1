from fastapi import APIRouter, Depends, HTTPException, Security
from typing import List
from app.schemas.status import StatusCreate, StatusUpdate, Status
from app.crud.crud_status import status
from app.Routes import deps
from sqlalchemy.orm import Session

router = APIRouter(prefix="/statuses", tags=["Statuses"])

@router.get("/", response_model=List[Status])
async def get_statuses(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Retrieve statuses.
    """
    statuses = status.get_multi(db, skip=skip, limit=limit)
    return statuses

@router.post("/", response_model=Status)
async def create_status(
    *,
    db: Session = Depends(deps.get_db),
    status_in: StatusCreate,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Create new status.
    """
    status_obj = status.create(db=db, obj_in=status_in)
    return status_obj

@router.put("/{id}", response_model=Status)
async def update_status(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    status_in: StatusUpdate,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Update a status.
    """
    status_obj = status.get(db=db, id=id)
    if not status_obj:
        raise HTTPException(status_code=404, detail="Status not found")
    status_obj = status.update(db=db, db_obj=status_obj, obj_in=status_in)
    return status_obj

@router.get("/{id}", response_model=Status)
async def get_status(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Get status by ID.
    """
    status_obj = status.get(db=db, id=id)
    if not status_obj:
        raise HTTPException(status_code=404, detail="Status not found")
    return status_obj

@router.delete("/{id}", response_model=Status)
async def delete_status(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Delete a status.
    """
    status_obj = status.get(db=db, id=id)
    if not status_obj:
        raise HTTPException(status_code=404, detail="Status not found")
    status_obj = status.remove(db=db, id=id)
    return status_obj 