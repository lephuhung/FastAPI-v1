from fastapi import APIRouter, Depends, HTTPException, Security
from typing import List
from app.schemas.characteristic import CharacteristicCreate, CharacteristicUpdate, Characteristic
from app.crud.crud_characteristic import characteristic
from app.Routes import deps
from sqlalchemy.orm import Session

router = APIRouter(prefix="/characteristics", tags=["Characteristics"])

@router.get("/", response_model=List[Characteristic])
async def get_characteristics(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Retrieve characteristics.
    """
    characteristics = characteristic.get_multi(db, skip=skip, limit=limit)
    return characteristics

@router.post("/", response_model=Characteristic)
async def create_characteristic(
    *,
    db: Session = Depends(deps.get_db),
    characteristic_in: CharacteristicCreate,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Create new characteristic.
    """
    characteristic_obj = characteristic.create(db=db, obj_in=characteristic_in)
    return characteristic_obj

@router.put("/{id}", response_model=Characteristic)
async def update_characteristic(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    characteristic_in: CharacteristicUpdate,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Update a characteristic.
    """
    characteristic_obj = characteristic.get(db=db, id=id)
    if not characteristic_obj:
        raise HTTPException(status_code=404, detail="Characteristic not found")
    characteristic_obj = characteristic.update(db=db, db_obj=characteristic_obj, obj_in=characteristic_in)
    return characteristic_obj

@router.get("/{id}", response_model=Characteristic)
async def get_characteristic(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Get characteristic by ID.
    """
    characteristic_obj = characteristic.get(db=db, id=id)
    if not characteristic_obj:
        raise HTTPException(status_code=404, detail="Characteristic not found")
    return characteristic_obj

@router.delete("/{id}", response_model=Characteristic)
async def delete_characteristic(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Delete a characteristic.
    """
    characteristic_obj = characteristic.get(db=db, id=id)
    if not characteristic_obj:
        raise HTTPException(status_code=404, detail="Characteristic not found")
    characteristic_obj = characteristic.remove(db=db, id=id)
    return characteristic_obj 