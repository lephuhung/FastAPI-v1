import uuid
import logging
from typing import List, Any, Union, Optional 
from fastapi import FastAPI, APIRouter, Body, Depends, HTTPException, Security
from sqlalchemy.orm import Session
from pydantic import UUID4

from app.Routes import deps
from app.db.session import SessionLocal #
from app.schemas import individual as individual_schema
from app.schemas import social_account as social_account_schema
from app.schemas import report as report_schema

from app.models.individual import Individual
from app.models.social_account import SocialAccount
from app.models.report import Report

from app.search import ( # Các hàm tương tác với Meilisearch
    search_individuals_meili,
    search_social_accounts_meili,
    search_reports_meili,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/search", tags=["Tìm kiếm"])


async def get_results_from_db(db: Session, model: Any, ids: List[Union[str, int]]) -> List[Any]:
    if not ids:
        return []
    logger.debug(f"Fetching {model.__name__} from DB with IDs: {ids}")
    try:
        if model == Individual:
            # Chuyển đổi string UUIDs từ Meili về UUID objects
            try:
                # uuid_ids = [UUID4(id_str) for id_str in ids]
                uuid_ids = [uuid.UUID(id_str) for id_str in ids]
                return db.query(Individual).filter(Individual.id.in_(uuid_ids)).all()
            except ValueError as e:
                 logger.error(f"Error converting one or more IDs to UUID: {ids} - {e}")
                 return [] # Hoặc raise lỗi nếu muốn dừng hẳn
        elif model == SocialAccount:
            # ID của social account trong Meili là 'uid' (string)
            return db.query(SocialAccount).filter(SocialAccount.uid.in_(ids)).all()
        elif model == Report:
             # ID của report trong Meili là 'id' (integer)
            int_ids = [int(id_val) for id_val in ids] # Đảm bảo là integer => Đổi khi cập nhật lại uuid
            return db.query(Report).filter(Report.id.in_(int_ids)).all()
        else:
             logger.warning(f"Unsupported model type for DB fetching: {model}")
             return []
    except Exception as e:
         logger.error(f"Error fetching data from DB for model {model.__name__} with IDs {ids}: {e}")
         return [] 

# --- API Endpoints Tìm kiếm ---

# Endpoint tìm kiếm Individuals
@router.get("/individual", response_model=List[individual_schema.Individual])
async def search_individuals_endpoint(
    query: str,
    db: Session = Depends(deps.get_db)
):
    """
    Tìm kiếm Individuals sử dụng Meilisearch, lấy ID và truy vấn dữ liệu đầy đủ từ DB.
    """
    logger.info(f"API search request for individuals: query='{query}'")
    search_result = search_individuals_meili(query) # Gọi hàm search Meili
    hits = search_result.get("hits", [])
    # ID trong Meili cho individual là UUID dạng string
    individual_ids = [hit['id'] for hit in hits]
    logger.debug(f"Meilisearch found individual IDs: {individual_ids}")

    if not individual_ids:
        return []

    # Lấy dữ liệu đầy đủ từ DB bằng IDs
    db_results = await get_results_from_db(db, Individual, individual_ids)
    logger.debug(f"DB returned {len(db_results)} individuals for IDs: {individual_ids}")

    # Sắp xếp lại kết quả từ DB theo thứ tự trả về của Meilisearch 
    try:
        id_map = {str(item.id): item for item in db_results}
        ordered_results = [id_map[id_str] for id_str in individual_ids if id_str in id_map]
    except Exception as e:
        logger.error(f"Error reordering individual results: {e}")
        # Fallback: Trả về kết quả không theo thứ tự nếu lỗi mapping
        ordered_results = db_results

    logger.info(f"Returning {len(ordered_results)} ordered individuals for query '{query}'")
    return ordered_results

# Endpoint tìm kiếm Social Accounts
@router.get("/social-account", response_model=List[social_account_schema.SocialAccount])
async def search_social_accounts_endpoint(
    query: str,
    db: Session = Depends(deps.get_db)
):
    """
    Tìm kiếm Social Accounts sử dụng Meilisearch, lấy ID (UID) và truy vấn dữ liệu đầy đủ từ DB.
    """
    logger.info(f"API search request for social accounts: query='{query}'")
    search_result = search_social_accounts_meili(query)
    hits = search_result.get("hits", [])
    # ID trong Meili cho social_account là 'uid' (string)
    social_account_uids = [hit['id'] for hit in hits]
    logger.debug(f"Meilisearch found social account UIDs: {social_account_uids}")

    if not social_account_uids:
        return []

    db_results = await get_results_from_db(db, SocialAccount, social_account_uids)
    logger.debug(f"DB returned {len(db_results)} social accounts for UIDs: {social_account_uids}")

    try:
        uid_map = {item.uid: item for item in db_results}
        ordered_results = [uid_map[uid] for uid in social_account_uids if uid in uid_map]
    except Exception as e:
         logger.error(f"Error reordering social account results: {e}")
         ordered_results = db_results

    logger.info(f"Returning {len(ordered_results)} ordered social accounts for query '{query}'")
    return ordered_results

# Endpoint tìm kiếm Trích tin
@router.get("/report", response_model=List[report_schema.Report])
async def search_reports_endpoint(
    query: str,
    db: Session = Depends(deps.get_db)
):
    """
    Tìm kiếm Reports sử dụng Meilisearch, lấy ID và truy vấn dữ liệu đầy đủ từ DB.
    """
    logger.info(f"API search request for reports: query='{query}'")
    search_result = search_reports_meili(query)
    hits = search_result.get("hits", [])
    # ID trong Meili cho report là 'id' (integer)
    report_ids = [hit['id'] for hit in hits]
    logger.debug(f"Meilisearch found report IDs: {report_ids}")

    if not report_ids:
        return []

    db_results = await get_results_from_db(db, Report, report_ids)
    logger.debug(f"DB returned {len(db_results)} reports for IDs: {report_ids}")

    try:
        id_map = {item.id: item for item in db_results}
        # Convert id_val từ Meili (có thể là string) sang int để khớp key của id_map
        ordered_results = [id_map[int(id_val)] for id_val in report_ids if int(id_val) in id_map]
    except Exception as e:
         logger.error(f"Error reordering report results: {e}")
         ordered_results = db_results

    logger.info(f"Returning {len(ordered_results)} ordered reports for query '{query}'")
    return ordered_results

