# # from fastapi import APIRouter, Depends
# from app.Routes.api import api_router
# # router= APIRouter()
# # router.include_router(api_router)
# # router.include_router(page)
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# # from app.api.api_v1.api import api_router
# # from app.core.config import settings

# app = FastAPI(
#     title='123',
#     openapi_url=f"/api/openapi.json",
# )
# @router('/')
# # app.add_middleware(
# #     CORSMiddleware,
# #     allow_origins=["*"],
# #     allow_credentials=True,
# #     allow_methods=["*"],
# #     allow_headers=["*"],
# # )

# # app.include_router(api_router)
from fastapi import FastAPI

app = FastAPI(title="FastAPI, Docker, and Traefik")


@app.get("/")
async def read_root():
    return {'123':'123'}


# @app.on_event("startup")
# async def startup():
#     if not database.is_connected:
#         await database.connect()
#     # create a dummy entry
#     await User.objects.get_or_create(email="test@test.com")


# @app.on_event("shutdown")
# async def shutdown():
#     if database.is_connected:
#         await database.disconnect()