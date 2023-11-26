from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.Routes.api import api_router
from app.db.init_db import init_db
from sqlalchemy.orm import Session
from app.Routes import deps
from app.core import sercurity, config
from typing import Annotated
from app import models, schemas
from datetime import timedelta
from fastapi.security import (
    OAuth2PasswordBearer,
    OAuth2PasswordRequestForm,
    SecurityScopes,
)
app = FastAPI(title="FastAPI, Docker, and Traefik")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_router, prefix='/api')


