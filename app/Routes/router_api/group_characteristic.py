from fastapi import APIRouter, Depends, HTTPException, Security
from typing import List
from app.schemas.group_characteristic import GroupCharacteristicCreate, GroupCharacteristicUpdate, GroupCharacteristic
from app.crud.crud_group_characteristic import group_characteristic
from app.Routes import deps
from sqlalchemy.orm import Session

router = APIRouter(prefix="/group-characteristics", tags=["Group Characteristics"])

@router.get("/", response_model=List[GroupCharacteristic])
async def get_group_characteristics(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Retrieve group characteristics.
    """
    group_characteristics = group_characteristic.get_multi(db, skip=skip, limit=limit)
    return group_characteristics

@router.post("/", response_model=GroupCharacteristic)
async def create_group_characteristic(
    *,
    db: Session = Depends(deps.get_db),
    group_characteristic_in: GroupCharacteristicCreate,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Create new group characteristic.
    """
    group_characteristic_obj = group_characteristic.create(db=db, obj_in=group_characteristic_in)
    return group_characteristic_obj

@router.put("/{id}", response_model=GroupCharacteristic)
async def update_group_characteristic(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    group_characteristic_in: GroupCharacteristicUpdate,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Update a group characteristic.
    """
    group_characteristic_obj = group_characteristic.get(db=db, id=id)
    if not group_characteristic_obj:
        raise HTTPException(status_code=404, detail="Group characteristic not found")
    group_characteristic_obj = group_characteristic.update(db=db, db_obj=group_characteristic_obj, obj_in=group_characteristic_in)
    return group_characteristic_obj

@router.get("/{id}", response_model=GroupCharacteristic)
async def get_group_characteristic(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Get group characteristic by ID.
    """
    group_characteristic_obj = group_characteristic.get(db=db, id=id)
    if not group_characteristic_obj:
        raise HTTPException(status_code=404, detail="Group characteristic not found")
    return group_characteristic_obj

@router.delete("/{id}", response_model=GroupCharacteristic)
async def delete_group_characteristic(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Delete a group characteristic.
    """
    group_characteristic_obj = group_characteristic.get(db=db, id=id)
    if not group_characteristic_obj:
        raise HTTPException(status_code=404, detail="Group characteristic not found")
    group_characteristic_obj = group_characteristic.remove(db=db, id=id)
    return group_characteristic_obj 