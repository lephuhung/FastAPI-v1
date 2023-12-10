from fastapi import APIRouter
from app.Routes.router_api import uid, user, auth, user_donvi, role_has_permission, user_has_permission, doituong,tags
api_router = APIRouter()

api_router.include_router(uid.router)
api_router.include_router(user.router)
api_router.include_router(auth.router)
api_router.include_router(user_donvi.router)
api_router.include_router(role_has_permission.router)
api_router.include_router(user_has_permission.router)
api_router.include_router(doituong.router)
api_router.include_router(tags.router)