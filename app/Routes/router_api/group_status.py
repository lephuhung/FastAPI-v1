from fastapi import APIRouter, Depends, HTTPException, Security
from typing import List
from app.schemas.group_status import GroupStatusCreate, GroupStatusUpdate, GroupStatus
from app.crud.crud_group_status import group_status
from app.Routes import deps
from sqlalchemy.orm import Session

router = APIRouter(prefix="/group-statuses", tags=["Group Statuses"])

@router.get("/", response_model=List[GroupStatus])
async def get_group_statuses(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Retrieve group statuses.
    """
    group_statuses = group_status.get_multi(db, skip=skip, limit=limit)
    return group_statuses

@router.post("/", response_model=GroupStatus)
async def create_group_status(
    *,
    db: Session = Depends(deps.get_db),
    group_status_in: GroupStatusCreate,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Create new group status.
    """
    group_status_obj = group_status.create(db=db, obj_in=group_status_in)
    return group_status_obj

@router.put("/{id}", response_model=GroupStatus)
async def update_group_status(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    group_status_in: GroupStatusUpdate,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Update a group status.
    """
    group_status_obj = group_status.get(db=db, id=id)
    if not group_status_obj:
        raise HTTPException(status_code=404, detail="Group status not found")
    group_status_obj = group_status.update(db=db, db_obj=group_status_obj, obj_in=group_status_in)
    return group_status_obj

@router.get("/{id}", response_model=GroupStatus)
async def get_group_status(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Get group status by ID.
    """
    group_status_obj = group_status.get(db=db, id=id)
    if not group_status_obj:
        raise HTTPException(status_code=404, detail="Group status not found")
    return group_status_obj

@router.delete("/{id}", response_model=GroupStatus)
async def delete_group_status(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Delete a group status.
    """
    group_status_obj = group_status.get(db=db, id=id)
    if not group_status_obj:
        raise HTTPException(status_code=404, detail="Group status not found")
    group_status_obj = group_status.remove(db=db, id=id)
    return group_status_obj 