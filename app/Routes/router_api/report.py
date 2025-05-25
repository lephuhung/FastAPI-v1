from fastapi import APIRouter, Depends, HTTPException, Security
from typing import List
from app.schemas.report import ReportCreate, ReportUpdate, Report
from app.crud.crud_report import report as report_crud
from app.Routes import deps
from sqlalchemy.orm import Session
from app.models.user import User
from sqlalchemy import select
import logging

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
    reports = report_crud.get_multi(db, skip=skip, limit=limit)
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
    try:
        logging.info(f"Current user: {current_user}")
        logging.info(f"Current user id: {current_user.id}")
        report_data = report_in.dict()
        report_data["user_id"] = current_user.id
        logging.info(f"Report data: {report_data}")
        
        # Create report
        report_obj = report_crud.create(db=db, obj_in=ReportCreate(**report_data))
        
        # Get user information using relationship
        response_data = {
            "id": report_obj.id,
            "social_account_uid": report_obj.social_account_uid,
            "content_note": report_obj.content_note,
            "comment": report_obj.comment,
            "action": report_obj.action,
            "related_social_account_uid": report_obj.related_social_account_uid,
            "user_id": report_obj.user_id,
            "created_at": report_obj.created_at,
            "updated_at": report_obj.updated_at,
        }
        
        return response_data
    except Exception as e:
        logging.error(f"Error creating report: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/{id}", response_model=Report)
async def update_report(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
    report_in: ReportUpdate,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Update a report.
    """
    report_obj = report_crud.get_by_social_account_uid(db=db, social_account_uid=id)
    if not report_obj:
        raise HTTPException(status_code=404, detail="Report not found")
    report_obj = report_crud.update(db=db, db_obj=report_obj, obj_in=report_in)
    return report_obj

@router.get("/{id}", response_model=Report)
async def get_report(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Get report by ID.
    """
    report_obj = report_crud.get_by_social_account_uid(db=db, social_account_uid=id)
    if not report_obj:
        raise HTTPException(status_code=404, detail="Report not found")
    return report_obj

@router.delete("/{id}", response_model=Report)
async def delete_report(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Delete a report.
    """
    report_obj = report_crud.get(db=db, id=id)
    if not report_obj:
        raise HTTPException(status_code=404, detail="Report not found")
    report_obj = report_crud.remove(db=db, id=id)
    return report_obj

@router.get("/social-account/{uid}")
async def get_reports_by_social_account(
    *,
    db: Session = Depends(deps.get_db),
    uid: str,
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Get reports by social account UID with user information.
    """
    try:
        logging.info(f"Fetching reports for social account UID: {uid}")
        reports = report_crud.get_by_social_account_uid(db=db, social_account_uid=uid)
        
        # Get user information for each report using relationship
        result = []
        for report in reports:
            try:
                report_dict = {
                    "id": report.id,
                    "social_account_uid": report.social_account_uid,
                    "content_note": report.content_note,
                    "comment": report.comment,
                    "action": report.action,
                    "related_social_account_uid": report.related_social_account_uid,
                    "created_at": report.created_at,
                    "updated_at": report.updated_at,
                    "user": {
                        "id": str(report.user.id),
                        "name": report.user.username
                    } if report.user else None
                }
                result.append(report_dict)
            except Exception as e:
                logging.error(f"Error processing report {report.id}: {str(e)}")
                continue
        
        logging.info(f"Found {len(result)} reports")
        return result
    except Exception as e:
        logging.error(f"Error fetching reports: {str(e)}")
        return [] 