from fastapi import APIRouter, Depends, Security
from sqlalchemy.orm import Session
from app.Routes import deps
from app.crud.crud_dashboard import dashboard
from app.schemas.dashboard import DashboardStats

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.get("/stats", response_model=DashboardStats)
def get_dashboard_stats(
    db: Session = Depends(deps.get_db),
    current_user=Security(deps.get_current_active_user, scopes=[]),
):
    """
    Lấy thống kê cho dashboard
    """
    account_type_stats = dashboard.get_account_type_stats(db)
    task_stats = dashboard.get_task_stats(db)
    
    return {
        "account_type_stats": account_type_stats,
        "task_stats": task_stats
    }

