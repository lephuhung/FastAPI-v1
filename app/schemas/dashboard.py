from typing import List, Dict
from pydantic import BaseModel

class AccountTypeStat(BaseModel):
    name: str
    count: int

class AccountTypeStats(BaseModel):
    total_individuals: int
    total_social_accounts: int
    account_type_stats: List[AccountTypeStat]

class TaskStat(BaseModel):
    name: str
    count: int

class TaskStats(BaseModel):
    individual_task_stats: List[TaskStat]
    social_account_task_stats: List[TaskStat]

class DashboardStats(BaseModel):
    account_type_stats: AccountTypeStats
    task_stats: TaskStats 