from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.Routes.api import api_router
from app.db.init_db import init_db
from app.Routes import deps
app = FastAPI(title="FastAPI, Docker, and Traefik")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_router, prefix='/api')


@app.on_event("startup")
async def startup():
   init_db(deps.get_db())


# @app.on_event("shutdown")
# async def shutdown():
#     if database.is_connected:
#         await database.disconnect()