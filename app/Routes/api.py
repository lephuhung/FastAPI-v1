from fastapi import APIRouter
from app.Routes.pages import page
api_router = APIRouter()

api_router.include_router(page.router)
