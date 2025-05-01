from fastapi import APIRouter, Depends, HTTPException, Security
from typing import List, Any
from pydantic import UUID4
from app.schemas.individual import IndividualCreate, IndividualUpdate, Individual, UnitBase, TaskBase
from app.schemas.individual_unit import IndividualUnitCreate
from app.crud.crud_individual import individual
from app.crud.crud_individual_unit import individual_unit
from app.crud.crud_unit import unit
from app.crud.crud_task import task
from app.Routes import deps
from sqlalchemy.orm import Session

router = APIRouter(prefix="/individuals", tags=["Individuals"])


@router.get("/", response_model=List[Individual])
def get_individuals(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Lấy danh sách individuals.
    """
    individuals = individual.get_multi(db, skip=skip, limit=limit)
    result = []
    for ind in individuals:
        # Lấy thông tin individual_units
        individual_units = individual_unit.get_by_individual_id(db=db, individual_id=ind.id)
        if individual_units:
            # Lấy thông tin unit và task từ individual_units đầu tiên
            unit_data = unit.get(db=db, id=individual_units[0].unit_id)
            task_data = task.get(db=db, id=individual_units[0].task_id)
            
            # Tạo đối tượng Individual với thông tin bổ sung
            ind_dict = ind.__dict__
            if unit_data:
                ind_dict["unit"] = UnitBase(id=unit_data.id, name=unit_data.name)
            if task_data:
                ind_dict["task"] = TaskBase(id=task_data.id, name=task_data.name)
            result.append(Individual(**ind_dict))
        else:
            result.append(ind)
    
    return result


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
    # Tách individual_units ra khỏi dữ liệu đầu vào
    individual_units_data = individual_in.individual_units
    individual_data = individual_in.dict(exclude={'individual_units'})
    
    # Tạo individual
    individual_obj = individual.create(db=db, obj_in=individual_data)
    
    # Xử lý thêm thông tin unit và task nếu có
    if individual_units_data:
        for unit_data in individual_units_data:
            admin_data = IndividualUnitCreate(
                unit_id=unit_data.unit_id,
                task_id=unit_data.task_id,
                individual_id=individual_obj.id
            )
            individual_unit.create(db=db, obj_in=admin_data)
    
    # Lấy thông tin individual_units sau khi tạo
    individual_units = individual_unit.get_by_individual_id(db=db, individual_id=individual_obj.id)
    
    # Tạo đối tượng Individual với thông tin bổ sung
    ind_dict = individual_obj.__dict__
    if individual_units:
        unit_data = unit.get(db=db, id=individual_units[0].unit_id)
        task_data = task.get(db=db, id=individual_units[0].task_id)
        if unit_data:
            ind_dict["unit"] = UnitBase(id=unit_data.id, name=unit_data.name)
        if task_data:
            ind_dict["task"] = TaskBase(id=task_data.id, name=task_data.name)
    
    return Individual(**ind_dict)


@router.put("/{id}", response_model=Individual)
async def update_individual(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID4,
    individual_in: IndividualUpdate,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Update an individual.
    """
    individual_obj = individual.get(db=db, id=id)
    if not individual_obj:
        raise HTTPException(status_code=404, detail="Individual not found")
    
    # Update individual
    individual_obj = individual.update(db=db, db_obj=individual_obj, obj_in=individual_in)
    
    # Update administrator if unit_id and task_id are provided
    if hasattr(individual_in, 'unit_id') and individual_in.unit_id:
        admin_data = IndividualUnitCreate(
            individual_id=id,
            unit_id=individual_in.unit_id,
            task_id=individual_in.task_id if hasattr(individual_in, 'task_id') else None
        )
        # Check if administrator record exists
        existing_admin = individual_unit.get_by_unit_and_individual(
            db=db, 
            individual_id=id,
            unit_id=individual_in.unit_id
        )
        if existing_admin:
            individual_unit.update(
                db=db,
                db_obj=existing_admin,
                obj_in=admin_data
            )
        else:
            individual_unit.create(db=db, obj_in=admin_data)
    
    return individual_obj


@router.get("/{id}", response_model=Individual)
async def get_individual(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID4,
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
    id: UUID4,
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