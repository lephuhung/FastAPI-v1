from fastapi import APIRouter, Depends, HTTPException, Security
from typing import List
from app.schemas.report import ReportCreate, ReportUpdate, Report
from app.crud.crud_report import report
from app.Routes import deps
from sqlalchemy.orm import Session

router = APIRouter(prefix="/reports", tags=["Reports"])

@router.get("/", response_model=List[Report])
async def get_reports(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Retrieve reports.
    """
    reports = report.get_multi(db, skip=skip, limit=limit)
    return reports

@router.post("/", response_model=Report)
async def create_report(
    *,
    db: Session = Depends(deps.get_db),
    report_in: ReportCreate,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Create new report.
    """
    report_obj = report.create(db=db, obj_in=report_in)
    return report_obj

@router.put("/{id}", response_model=Report)
async def update_report(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    report_in: ReportUpdate,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Update a report.
    """
    report_obj = report.get(db=db, id=id)
    if not report_obj:
        raise HTTPException(status_code=404, detail="Report not found")
    report_obj = report.update(db=db, db_obj=report_obj, obj_in=report_in)
    return report_obj

@router.get("/{id}", response_model=Report)
async def get_report(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Get report by ID.
    """
    report_obj = report.get(db=db, id=id)
    if not report_obj:
        raise HTTPException(status_code=404, detail="Report not found")
    return report_obj

@router.delete("/{id}", response_model=Report)
async def delete_report(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Delete a report.
    """
    report_obj = report.get(db=db, id=id)
    if not report_obj:
        raise HTTPException(status_code=404, detail="Report not found")
    report_obj = report.remove(db=db, id=id)
    return report_obj 