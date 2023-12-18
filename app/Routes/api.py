from fastapi import APIRouter
from app.Routes.router_api import uid, user, auth, user_donvi, donvi_hoinhom ,trichtin,role_has_permission, user_has_permission, doituong,tags, model_has_tags, doituong_donvi, tinhchat_hoinhom, doituong_uid
api_router = APIRouter()

api_router.include_router(uid.router)
api_router.include_router(user.router)
api_router.include_router(auth.router)
api_router.include_router(user_donvi.router)
api_router.include_router(role_has_permission.router)
api_router.include_router(user_has_permission.router)
api_router.include_router(doituong.router)
api_router.include_router(tags.router)
api_router.include_router(model_has_tags.router)
api_router.include_router(doituong_donvi.router)
api_router.include_router(donvi_hoinhom.router)
api_router.include_router(trichtin.router)
api_router.include_router(tinhchat_hoinhom.router)
api_router.include_router(doituong_uid.router)