from typing import Dict, List
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.individual import Individual
from app.models.social_account import SocialAccount
from app.models.account_type import AccountType
from app.models.task import Task
from app.models.individual_social_account import IndividualSocialAccount
from app.models.individual_unit import IndividualUnit

class CRUDDashboard:
    def get_account_type_stats(self, db: Session) -> Dict:
        """
        Thống kê số lượng individual, social_account và số lượng social_account theo account_type
        """
        # Tổng số individual
        total_individuals = db.query(func.count(Individual.id)).scalar() or 0
        
        # Tổng số social_account
        total_social_accounts = db.query(func.count(SocialAccount.id)).scalar() or 0
        
        # Lấy tất cả account types
        all_account_types = db.query(AccountType).all()
        
        # Tạo map để lưu số lượng social_account theo account_type
        account_type_counts = {}
        for acc_type in all_account_types:
            account_type_counts[acc_type.name] = 0
        
        # Cập nhật số lượng social_account theo account_type
        account_type_stats = db.query(
            AccountType.name,
            func.count(SocialAccount.id).label('count')
        ).join(
            SocialAccount,
            SocialAccount.type_id == AccountType.id
        ).group_by(
            AccountType.name
        ).all()
        
        for name, count in account_type_stats:
            account_type_counts[name] = count
        
        return {
            "total_individuals": total_individuals,
            "total_social_accounts": total_social_accounts,
            "account_type_stats": [
                {"name": name, "count": count}
                for name, count in account_type_counts.items()
            ]
        }
    
    def get_task_stats(self, db: Session) -> Dict:
        """
        Thống kê individual và social_account theo task
        """
        # Lấy tất cả tasks
        all_tasks = db.query(Task).all()
        
        # Tạo map để lưu thống kê theo task
        task_stats = {}
        for task in all_tasks:
            task_stats[task.name] = {
                'individual_count': 0,
                'social_account_count': 0
            }
        
        # Thống kê individual theo task
        individual_task_stats = db.query(
            Task.name,
            func.count(Individual.id).label('count')
        ).join(
            IndividualUnit,
            IndividualUnit.task_id == Task.id
        ).join(
            Individual,
            Individual.id == IndividualUnit.individual_id
        ).group_by(
            Task.name
        ).all()
        
        for name, count in individual_task_stats:
            if name in task_stats:
                task_stats[name]['individual_count'] = count
        
        # Thống kê social_account theo task
        social_account_task_stats = db.query(
            Task.name,
            func.count(SocialAccount.id).label('count')
        ).join(
            IndividualUnit,
            IndividualUnit.task_id == Task.id
        ).join(
            Individual,
            Individual.id == IndividualUnit.individual_id
        ).join(
            IndividualSocialAccount,
            IndividualSocialAccount.individual_id == Individual.id
        ).join(
            SocialAccount,
            SocialAccount.uid == IndividualSocialAccount.social_account_uid
        ).group_by(
            Task.name
        ).all()
        
        for name, count in social_account_task_stats:
            if name in task_stats:
                task_stats[name]['social_account_count'] = count
        
        return {
            "individual_task_stats": [
                {"name": name, "count": stats['individual_count']}
                for name, stats in task_stats.items()
            ],
            "social_account_task_stats": [
                {"name": name, "count": stats['social_account_count']}
                for name, stats in task_stats.items()
            ]
        }

    def get_social_accounts_by_type(self, db: Session, type_id: int):
        """
        Lấy số lượng social_account theo type_id
        """
        count = db.query(func.count(SocialAccount.id)).filter(SocialAccount.type_id == type_id).scalar()
        return count or 0

dashboard = CRUDDashboard() 