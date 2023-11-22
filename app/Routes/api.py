from fastapi import APIRouter
from app.Routes.router_api import uid
from apo.Routes.router_api import user
api_router = APIRouter()

api_router.include_router(uid.router)
api_router.include_router(user.router)