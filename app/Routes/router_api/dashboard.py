from fastapi import APIRouter, Depends, Security
from sqlalchemy.orm import Session
from app.Routes import deps
from app import crud
from app.schemas.tags import tagscreate
from pydantic import UUID4

router = APIRouter(prefix="/dashboard", tags=["Màn hình chính"])


@router.get("/individual")
def get_individual_dashboard(db: Session = Depends(deps.get_db)):
    return crud.crud_thongke.dashboard_individual(db=db)


@router.get("/uid")
def get_uid_dashboard(db: Session = Depends(deps.get_db)):
    return crud.crud_thongke.dashboard_uid(db=db)

@router.get("/trichtin")
def get_uid_dashboard(db: Session = Depends(deps.get_db)):
    return crud.crud_thongke.dashboard_trichtin(db= db)

