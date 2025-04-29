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
        total_individuals = db.query(func.count(Individual.id)).scalar()
        
        # Tổng số social_account
        total_social_accounts = db.query(func.count(SocialAccount.id)).scalar()
        
        # Số lượng social_account theo account_type
        account_type_stats = db.query(
            AccountType.name,
            func.count(SocialAccount.id).label('count')
        ).join(
            SocialAccount,
            SocialAccount.type_id == AccountType.id
        ).group_by(
            AccountType.name
        ).all()
        
        return {
            "total_individuals": total_individuals,
            "total_social_accounts": total_social_accounts,
            "account_type_stats": [
                {"name": name, "count": count}
                for name, count in account_type_stats
            ]
        }
    
    def get_task_stats(self, db: Session) -> Dict:
        """
        Thống kê individual và social_account theo task
        """
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
        
        return {
            "individual_task_stats": [
                {"name": name, "count": count}
                for name, count in individual_task_stats
            ],
            "social_account_task_stats": [
                {"name": name, "count": count}
                for name, count in social_account_task_stats
            ]
        }

dashboard = CRUDDashboard() 