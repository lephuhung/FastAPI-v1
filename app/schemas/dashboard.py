from typing import List, Dict
from pydantic import BaseModel

class AccountTypeStat(BaseModel):
    name: str
    count: int

class AccountTypeStats(BaseModel):
    total_individuals: int
    total_social_accounts: int
    account_type_stats: List[AccountTypeStat]

class CombinedTaskStat(BaseModel):
    name: str
    individual_count: int
    social_account_count: int

class TaskStats(BaseModel):
    combined_task_stats: List[CombinedTaskStat]

class DashboardStats(BaseModel):
    account_type_stats: AccountTypeStats
    task_stats: TaskStats 