from fastapi import APIRouter
from app.Routes.router_api.administrator import router as administrator
from app.Routes.router_api.status import router as status
from app.Routes.router_api.tag import router as tag
from app.Routes.router_api.task import router as task
from app.Routes.router_api.permission import router as permission
from app.Routes.router_api.relationship import router as relationship
from app.Routes.router_api.role import router as role
from app.Routes.router_api.unit import router as unit
from app.Routes.router_api.individual import router as individual
from app.Routes.router_api.characteristic import router as characteristic
from app.Routes.router_api.group_characteristic import router as group_characteristic
from app.Routes.router_api.group_status import router as group_status
from app.Routes.router_api.individual_unit import router as individual_unit
from app.Routes.router_api.report import router as report
from app.Routes.router_api.unit_group import router as unit_group
from app.Routes.router_api.social_account_link import router as social_account_link
from app.Routes.router_api.individual_social_account import router as individual_social_account
from app.Routes.router_api.individual_tag import router as individual_tag
from app.Routes.router_api.social_account import router as social_account
from app.Routes.router_api.auth import router as auth
from app.Routes.router_api.user import router as user
from app.Routes.router_api.search import router as search
from app.Routes.router_api.dashboard import router as dashboard
from app.Routes.router_api.account_type import router as account_type
from app.Routes.router_api.user_role import router as user_role
from app.Routes.router_api.user_permission import router as user_permission
from app.Routes.router_api.role_permission import router as role_permission
from app.Routes.router_api.summary import router as summary

api_router = APIRouter()
api_router.include_router(auth)
api_router.include_router(user)
api_router.include_router(unit)
api_router.include_router(characteristic)
api_router.include_router(task)
api_router.include_router(social_account)
api_router.include_router(summary)
api_router.include_router(administrator)
api_router.include_router(status)
api_router.include_router(tag)
api_router.include_router(permission)
api_router.include_router(relationship)
api_router.include_router(role)
api_router.include_router(individual)
api_router.include_router(group_characteristic)
api_router.include_router(group_status)
api_router.include_router(individual_unit)
api_router.include_router(report)
api_router.include_router(unit_group)
api_router.include_router(social_account_link)
api_router.include_router(individual_social_account)
api_router.include_router(individual_tag)
api_router.include_router(search)
api_router.include_router(dashboard)
api_router.include_router(account_type)
api_router.include_router(user_role)
api_router.include_router(user_permission)
api_router.include_router(role_permission)
