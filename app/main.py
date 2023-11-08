# from fastapi import APIRouter, Depends
from app.Routes.api import api_router
# router= APIRouter()
# router.include_router(api_router)
# router.include_router(page)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from app.api.api_v1.api import api_router
# from app.core.config import settings

app = FastAPI(
    title='123',
    openapi_url=f"/api/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)