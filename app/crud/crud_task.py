from typing import Any, Dict, Optional, Union, List
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate


class CRUDTask(CRUDBase[Task, TaskCreate, TaskUpdate]):
    def get_by_name(self, db: Session, *, name: str) -> Optional[Task]:
        return db.query(Task).filter(Task.name == name).first()


task = CRUDTask(Task) 