import time
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, SecurityScopes
from fastapi.middleware.cors import CORSMiddleware
from app.Routes.api import api_router
from app.db.init_db import init_db
from sqlalchemy.orm import Session
from app.Routes import deps
from app.core import security, config
from typing import Annotated
from app import models, schemas
from datetime import timedelta
from app.db.session import SessionLocal
import logging

from app.search import setup_meilisearch_indexes, index_all_data

import logging
from sqlalchemy import text

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- IMPORT ĐỂ ĐĂNG KÝ LISTENERS ---
try:
    import app.db.listeners # Chỉ cần import là đủ để decorator @event.listens_for chạy
    logger = logging.getLogger(__name__)
    logger.info("SQLAlchemy event listeners registered successfully.")
except ImportError:
    logging.getLogger(__name__).warning("Could not import app.db.listeners. SQLAlchemy events for Meilisearch sync might not work.")


app = FastAPI(title="FastAPI, Docker, and Traefik")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_router, prefix='/api')

# def init() -> None:
#     db = SessionLocal()
#     # init_db(db)


@app.on_event("startup")
def on_startup():
    print("Application starting up...")
    try:
        # Kiểm tra kết nối DB
        logger.debug("Checking database connection...")
        db = SessionLocal()
        db.execute(text("SELECT 1"))
        db.close()
        logger.info("Database connection successful.")

        # Setup Meilisearch indexes (chạy ngầm)
        print("Setting up Meilisearch indexes...")
        setup_meilisearch_indexes()
        print("Meilisearch setup potentially complete (check logs for details).")

        # Tuỳ chọn: Chạy full index khi khởi động (có thể tốn thời gian)
        # Chỉ chạy nếu cần thiết hoặc trong môi trường dev
  
        logger.info("Starting initial data indexing (BLOCKING)... This might take some time.")
        start_time = time.time() # Đo thời gian (cần import time)
        index_all_data() # Gọi hàm index trực tiếp
        end_time = time.time()
        logger.info(f"Initial data indexing finished in {end_time - start_time:.2f} seconds.")
        # ------------------------------------

    except Exception as e:
        print(f"Error during startup: {e}")

logger.info("Application setup complete (post-startup event). Server ready to accept requests.")
