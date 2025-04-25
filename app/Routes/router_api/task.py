from fastapi import APIRouter, Depends, HTTPException, Security
from typing import List
from app.schemas.task import TaskCreate, TaskUpdate, Task
from app.crud.crud_task import task
from app.Routes import deps
from sqlalchemy.orm import Session

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("/", response_model=List[Task])
async def get_tasks(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Retrieve tasks.
    """
    tasks = task.get_multi(db, skip=skip, limit=limit)
    return tasks

@router.post("/", response_model=Task)
async def create_task(
    *,
    db: Session = Depends(deps.get_db),
    task_in: TaskCreate,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Create new task.
    """
    task_obj = task.create(db=db, obj_in=task_in)
    return task_obj

@router.put("/{id}", response_model=Task)
async def update_task(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    task_in: TaskUpdate,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Update a task.
    """
    task_obj = task.get(db=db, id=id)
    if not task_obj:
        raise HTTPException(status_code=404, detail="Task not found")
    task_obj = task.update(db=db, db_obj=task_obj, obj_in=task_in)
    return task_obj

@router.get("/{id}", response_model=Task)
async def get_task(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Get task by ID.
    """
    task_obj = task.get(db=db, id=id)
    if not task_obj:
        raise HTTPException(status_code=404, detail="Task not found")
    return task_obj

@router.delete("/{id}", response_model=Task)
async def delete_task(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Delete a task.
    """
    task_obj = task.get(db=db, id=id)
    if not task_obj:
        raise HTTPException(status_code=404, detail="Task not found")
    task_obj = task.remove(db=db, id=id)
    return task_obj 