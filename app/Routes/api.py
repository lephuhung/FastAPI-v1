from fastapi import APIRouter
from app.Routes.router_api import uid
from app.Routes.router_api import user
from app.Routes.router_api import auth
from app.Routes.router_api import user_donvi
api_router = APIRouter()

api_router.include_router(uid.router)
api_router.include_router(user.router)
api_router.include_router(auth.router)
api_router.include_router(user_donvi.router)