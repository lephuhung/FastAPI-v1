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
    
    # Gộp thống kê theo task name
    combined_task_stats = []
    task_map = {}
    
    # Xử lý individual task stats
    for stat in task_stats.get('individual_task_stats', []):
        task_map[stat['name']] = {
            'name': stat['name'],
            'individual_count': stat['count'],
            'social_account_count': 0
        }
    
    # Cập nhật social account stats
    for stat in task_stats.get('social_account_task_stats', []):
        if stat['name'] in task_map:
            task_map[stat['name']]['social_account_count'] = stat['count']
        else:
            task_map[stat['name']] = {
                'name': stat['name'],
                'individual_count': 0,
                'social_account_count': stat['count']
            }
    
    # Chuyển đổi map thành list
    combined_task_stats = list(task_map.values())
    
    # Lấy số lượng social_account có type_id = 4
    type_4_social_accounts = dashboard.get_social_accounts_by_type(db, type_id=4)
    
    return {
        "account_type_stats": account_type_stats,
        "task_stats": {
            "combined_task_stats": combined_task_stats
        },
        "type_4_social_accounts": type_4_social_accounts
    }

