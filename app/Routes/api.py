from fastapi import APIRouter
from app.Routes import pages
api_router = APIRouter()

api_router.include_router(pages.router)
