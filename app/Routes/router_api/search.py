import uuid
import logging
from typing import List, Any, Union, Optional 
from fastapi import FastAPI, APIRouter, Body, Depends, HTTPException, Security, Query 
from sqlalchemy.orm import Session
from pydantic import UUID4

from app.Routes import deps
from app.db.session import SessionLocal
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

# --- API Endpoints Tìm kiếm, Lọc, Sắp xếp ---

# --- Định nghĩa các trường được phép sắp xếp cho mỗi index (để validation) ---
ALLOWED_SORT_INDIVIDUAL = {'created_at', 'updated_at', 'full_name'}
ALLOWED_SORT_SOCIAL = {'created_at', 'updated_at', 'name', 'reaction_count'}
ALLOWED_SORT_REPORT = {'created_at', 'updated_at'}

# --- Endpoint tìm kiếm Individuals
@router.get("/individual", response_model=List[individual_schema.Individual])
# search/individual?query=văn a&is_kol=true&sort=updated_at:desc,full_name:asc
async def search_individuals_endpoint(
    query: str,
    # --- Tham số Filter ---
    is_kol: Optional[bool] = Query(None, description="Lọc theo trạng thái KOL (true/false)"),
    # --- Tham số phân trang ---
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0),
    # --- Tham số Sort ---
    sort: Optional[str] = Query(
        None,
        description=f"Sắp xếp kết quả. Cú pháp: 'field:asc' hoặc 'field:desc', cách nhau bởi dấu phẩy (,). Các trường hợp lệ: {', '.join(ALLOWED_SORT_INDIVIDUAL)}",
        example="full_name:asc,created_at:desc" # Ví dụ cho Swagger UI
    ),
    # --------------------------
    db: Session = Depends(deps.get_db)
):
    """
    Tìm kiếm Individuals, hỗ trợ filter, sort và phân trang.
    """

    # --- Filter ---
    filters = []
    if is_kol is not None: filters.append(f"is_kol = {'true' if is_kol else 'false'}")
    filter_string = " AND ".join(filters) if filters else None
    # ---------------------------------

    # --- Phân tích và kiểm tra tham số sort ---
    sort_criteria = [] # List chứa các chuỗi sort hợp lệ cho Meilisearch
    if sort:
        allowed_fields = ALLOWED_SORT_INDIVIDUAL
        sort_parts = [part.strip() for part in sort.split(',')] # Tách các phần sort theo dấu phẩy
        for part in sort_parts:
            if ':' not in part or part.count(':') != 1:
                raise HTTPException(
                    status_code=400, 
                    detail=f"Sai định dạng sort: '{part}'. Phải là 'field:asc' hoặc 'field:desc'."
                )
            field, direction = part.split(':')
            direction = direction.lower() # Chuẩn hóa asc/desc thành chữ thường
            if direction not in ['asc', 'desc']:
                 raise HTTPException(
                    status_code=400,
                    detail=f"Hướng sắp xếp không hợp lệ: '{direction}' trong '{part}'. Phải là 'asc' hoặc 'desc'."
                 )
            if field not in allowed_fields:
                 raise HTTPException(
                    status_code=400,
                    detail=f"Không thể sắp xếp theo trường '{field}'. Các trường hợp lệ: {', '.join(allowed_fields)}"
                 )
            sort_criteria.append(f"{field}:{direction}") # Thêm tiêu chí hợp lệ vào list
    logger.debug(f"Parsed Meilisearch sort criteria: {sort_criteria}")
    # -----------------------------------------

    # --- Chuẩn bị options cho Meilisearch (bao gồm cả sort) ---
    search_options = {
        "limit": limit,
        "offset": offset,
    }
    if filter_string:
        search_options["filter"] = filter_string
    if sort_criteria: # Chỉ thêm key 'sort' nếu có tiêu chí sắp xếp
        search_options["sort"] = sort_criteria # Giá trị là một list các chuỗi
    # ---------------------------------------------------------

    # Gọi hàm tìm kiếm Meilisearch với options đã bao gồm sort
    search_result = search_individuals_meili(query, options=search_options)

    # --- Phần xử lý kết quả và lấy dữ liệu từ DB giữ nguyên ---
    # Việc sắp xếp lại theo thứ tự 'hits' trả về từ Meilisearch là TRUE
    # vì Meilisearch đã trả về 'hits' theo đúng thứ tự sort yêu cầu.
    hits = search_result.get("hits", [])
    individual_ids = [hit['id'] for hit in hits]
    logger.debug(f"Meilisearch found individual IDs with filter/sort: {individual_ids}")

    if not individual_ids: return []
    db_results = await get_results_from_db(db, Individual, individual_ids)
    logger.debug(f"DB returned {len(db_results)} individuals for filtered/sorted IDs")
    try:
        id_map = {str(item.id): item for item in db_results}
        ordered_results = [id_map[id_str] for id_str in individual_ids if id_str in id_map]
    except Exception as e:
        logger.error(f"Error reordering individual results: {e}", exc_info=True)
        ordered_results = db_results # Fallback có thể mất thứ tự sort mong muốn
    logger.info(f"Returning {len(ordered_results)} ordered individuals for query '{query}' with filters/sort")
    return ordered_results


# --- Endpoint tìm kiếm Social Accounts  ---
#search/social-account?query=&status_id=1&type_id=1&sort=updated_at:desc,full_name:asc
@router.get("/social-account", response_model=List[social_account_schema.SocialAccount])
async def search_social_accounts_endpoint(
    query: str,
    # --- Tham số phân trang ---
    status_id: Optional[int] = Query(None),
    type_id: Optional[int] = Query(None),
    is_linked: Optional[bool] = Query(None),
    # --- Tham số phân trang ---
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0),
    # --- Tham số sort ---
    sort: Optional[str] = Query(
        None,
        description=f"Sắp xếp kết quả. Cú pháp: 'field:asc|desc', cách nhau bởi dấu phẩy. Trường hợp lệ: {', '.join(ALLOWED_SORT_SOCIAL)}",
        example="reaction_count:desc"
    ),
    # --------------------------
    db: Session = Depends(deps.get_db)
):
    logger.info(f"API search social accounts: query='{query}', filters=..., sort={sort}, limit={limit}, offset={offset}")

    # --- Filter ---
    filters = []
    if status_id is not None: filters.append(f"status_id = {status_id}")
    if type_id is not None: filters.append(f"type_id = {type_id}")
    if is_linked is not None: filters.append(f"is_linked = {'true' if is_linked else 'false'}")
    filter_string = " AND ".join(filters) if filters else None
    # ---------------------------------

    # --- Phân trang và kiểm tra sort ---
    sort_criteria = []
    if sort:
        allowed_fields = ALLOWED_SORT_SOCIAL
        sort_parts = [part.strip() for part in sort.split(',')]
        for part in sort_parts:
            if ':' not in part or part.count(':') != 1: raise HTTPException(status_code=400, detail=f"Sai định dạng sort: '{part}'.")
            field, direction = part.split(':')
            direction = direction.lower()
            if direction not in ['asc', 'desc']: raise HTTPException(status_code=400, detail=f"Hướng sắp xếp không hợp lệ: '{direction}'.")
            if field not in allowed_fields: raise HTTPException(status_code=400, detail=f"Không thể sắp xếp theo trường '{field}'.")
            sort_criteria.append(f"{field}:{direction}")
    logger.debug(f"Parsed Meilisearch sort criteria: {sort_criteria}")
    # ---------------------------------

    # --- Chuẩn bị options ---
    search_options = {"limit": limit, "offset": offset}
    if filter_string: search_options["filter"] = filter_string
    if sort_criteria: search_options["sort"] = sort_criteria
    # -----------------------

    search_result = search_social_accounts_meili(query, options=search_options)

    # --- Xử lý kết quả (giữ nguyên logic reorder) ---
    hits = search_result.get("hits", [])
    social_account_uids = [hit['id'] for hit in hits]
    logger.debug(f"Meilisearch found social account UIDs with filter/sort: {social_account_uids}")
    if not social_account_uids: return []
    db_results = await get_results_from_db(db, SocialAccount, social_account_uids)
    logger.debug(f"DB returned {len(db_results)} social accounts for filtered/sorted UIDs")
    try:
        uid_map = {item.uid: item for item in db_results}
        ordered_results = [uid_map[uid] for uid in social_account_uids if uid in uid_map]
    except Exception as e:
        logger.error(f"Error reordering social account results: {e}", exc_info=True)
        ordered_results = db_results
    logger.info(f"Returning {len(ordered_results)} ordered social accounts for query '{query}' with filters/sort")
    return ordered_results


# --- Endpoint Tìm kiếm trích tin ---
#search/report?query=&user_id=uuid-string&social_account_uid=1000021455421&limit=10&sort=updated_at:desc,full_name:asc
@router.get("/report", response_model=List[report_schema.Report])
async def search_reports_endpoint(
    query: str,
    # --- Tham số Filter ---
    user_id: Optional[str] = Query(None),
    social_account_uid: Optional[str] = Query(None),
    # --- Tham số phân trang ---
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0),
     # --- Tham số sort---
    sort: Optional[str] = Query(
        None,
        description=f"Sắp xếp kết quả. Cú pháp: 'field:asc|desc', cách nhau bởi dấu phẩy. Trường hợp lệ: {', '.join(ALLOWED_SORT_REPORT)}",
        example="created_at:desc"
    ),
    # --------------------------
    db: Session = Depends(deps.get_db)
):
    logger.info(f"API search reports: query='{query}', filters=..., sort={sort}, limit={limit}, offset={offset}")

    # --- Filter ---
    filters = []
    if user_id:
        try:
            uuid.UUID(user_id)
            filters.append(f'user_id = "{user_id}"')
        except ValueError: logger.warning(f"Invalid user_id format for filter: {user_id}")
    if social_account_uid: filters.append(f'social_account_uid = "{social_account_uid}"')
    filter_string = " AND ".join(filters) if filters else None
    # ---------------------------------

    # --- Phân trang và kiểm tra sort ---
    sort_criteria = []
    if sort:
        allowed_fields = ALLOWED_SORT_REPORT
        sort_parts = [part.strip() for part in sort.split(',')]
        for part in sort_parts:
            if ':' not in part or part.count(':') != 1: raise HTTPException(status_code=400, detail=f"Sai định dạng sort: '{part}'.")
            field, direction = part.split(':')
            direction = direction.lower()
            if direction not in ['asc', 'desc']: raise HTTPException(status_code=400, detail=f"Hướng sắp xếp không hợp lệ: '{direction}'.")
            if field not in allowed_fields: raise HTTPException(status_code=400, detail=f"Không thể sắp xếp theo trường '{field}'.")
            sort_criteria.append(f"{field}:{direction}")
    logger.debug(f"Parsed Meilisearch sort criteria: {sort_criteria}")
    # ---------------------------------

    # --- Chuẩn bị options ---
    search_options = {"limit": limit, "offset": offset}
    if filter_string: search_options["filter"] = filter_string
    if sort_criteria: search_options["sort"] = sort_criteria
    # -----------------------

    search_result = search_reports_meili(query, options=search_options)

    # --- Xử lý kết quả (giữ nguyên logic reorder) ---
    hits = search_result.get("hits", [])
    report_ids = [hit['id'] for hit in hits]
    logger.debug(f"Meilisearch found report IDs with filter/sort: {report_ids}")
    if not report_ids: return []
    db_results = await get_results_from_db(db, Report, report_ids)
    logger.debug(f"DB returned {len(db_results)} reports for filtered/sorted IDs")
    try:
        id_map = {item.id: item for item in db_results}
        ordered_results = [id_map[int(id_val)] for id_val in report_ids if int(id_val) in id_map]
    except Exception as e:
         logger.error(f"Error reordering report results: {e}", exc_info=True)
         ordered_results = db_results
    logger.info(f"Returning {len(ordered_results)} ordered reports for query '{query}' with filters/sort")
    return ordered_results

