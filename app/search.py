# app/search.py (Ví dụ)
import meilisearch
import os
import logging
from typing import List, Dict, Any, Union, Optional 
from app.db.session import SessionLocal 
from app.models.individual import Individual
from app.models.social_account import SocialAccount
from app.models.report import Report


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

MEILI_HOST = os.getenv("MEILI_HOST", "http://localhost:7700") # Lấy từ env var, fallback localhost
MEILI_MASTER_KEY = os.getenv("MEILI_MASTER_KEY", None) # Lấy từ env var


try:
    client = meilisearch.Client(MEILI_HOST, MEILI_MASTER_KEY)
    client.health()
    logger.info(f"Meilisearch client initialized successfully for host: {MEILI_HOST}")
except Exception as e:
    logger.error(f"Failed to initialize Meilisearch client: {e}", exc_info=True)

    client = None

INDEX_INDIVIDUALS = "individuals"
INDEX_SOCIAL_ACCOUNTS = "social_accounts"
INDEX_REPORTS = "reports"

# --- Cấu hình các trường có thể tìm kiếm và lọc ---
# Xem thêm: https://docs.meilisearch.com/learn/configuration/settings.html

# --- HÀM KIỂM TRA HEALTH VÀO  ---
def is_meilisearch_available():
    """Kiểm tra nhanh xem Meilisearch có đang hoạt động không."""
    if client is None: # Nếu client khởi tạo thất bại
        logger.warning("Meilisearch client is not initialized.")
        return False
    try:
        health = client.health()
        is_avail = health.get('status') == 'available'
        logger.debug(f"Meilisearch health check result: {is_avail}")
        return is_avail
    except Exception as e:
        logger.warning(f"Meilisearch health check failed: {e}")
        return False
# ---------------------------------------

def setup_meilisearch_indexes():
    """Khởi tạo index và cài đặt cơ bản nếu chưa có"""
    try:
        # Index Individuals
        index_individuals = client.index(INDEX_INDIVIDUALS)
        index_individuals.update_settings({
            'searchableAttributes': [ # Các trường tìm kiếm full-text
                'full_name',
                'id_number', # CCCD / CMND trong model
                'additional_info',
                'phone_number',
                'hometown' # Thêm quê quán vào tìm kiếm
            ],
            'filterableAttributes': [ # Các trường filter
                'is_kol',
            ],
            'sortableAttributes': [ # Các trường có thể sắp xếp
                'created_at',
                'updated_at',
                'full_name'
            ]
            # primaryKey mặc định là 'id' nếu có, nếu không Meili sẽ tự tìm
        })
        logger.info(f"Index '{INDEX_INDIVIDUALS}' setup complete.")

        # Index Social Accounts
        index_social_accounts = client.index(INDEX_SOCIAL_ACCOUNTS)
        index_social_accounts.update_settings({
            'searchableAttributes': [
                'uid',
                'name',
                'phone_number',
                'note' 
            ],
            'filterableAttributes': [
                'status_id',
                'account_type_id',
                'is_linked',
            ],
            'sortableAttributes': [
                'created_at',
                'updated_at',
                'name',
                'reaction_count'
            ]
            # primaryKey uid có unique constraint nên Meili có thể tự nhận diện
        })
        logger.info(f"Index '{INDEX_SOCIAL_ACCOUNTS}' setup complete.")

        # Index Reports
        index_reports = client.index(INDEX_REPORTS)
        index_reports.update_settings({
            'searchableAttributes': [
                'social_account_uid',
                'content_note',
                'comment',
                'action',
                'linked_social_account_uid'
            ],
            'filterableAttributes': [
                'social_account_uid',
                'user_id',
                'linked_social_account_uid'
            ],
            'sortableAttributes': [
                'created_at',
                'updated_at'
            ]
            # primaryKey là 'id' (SERIAL)
        })
        logger.info(f"Index '{INDEX_REPORTS}' setup complete.")

    except Exception as e:
        logger.error(f"Error setting up Meilisearch indexes: {e}")

def convert_to_searchable_dict(obj: Any) -> Dict[str, Any]:
    """Chuyển đổi SQLAlchemy object thành dict phù hợp cho Meilisearch"""
    if isinstance(obj, Individual):
        # Chuyển UUID thành string, Date thành string ISO format
        return {
            "id": str(obj.id), # Note: Meilisearch cần ID là string hoặc int
            "full_name": obj.full_name,
            "id_number": obj.id_number,
            "image_url": obj.image_url,
            "date_of_birth": obj.date_of_birth.isoformat() if obj.date_of_birth else None,
            "is_male": obj.is_male,
            "hometown": obj.hometown,
            "additional_info": obj.additional_info,
            "phone_number": obj.phone_number,
            "kols_type": obj.kols_type,
            "is_kol": obj.is_kol,
            # Chuyển đổi DateTime thành Unix timestamp (integer) hoặc ISO string
            "created_at": int(obj.created_at.timestamp()) if obj.created_at else None,
            "updated_at": int(obj.updated_at.timestamp()) if obj.updated_at else None,
        }
    elif isinstance(obj, SocialAccount):
        return {
            "id": str(obj.uid), 
            "uid": obj.uid, 
            "name": obj.name,
            "reaction_count": obj.reaction_count,
            "phone_number": obj.phone_number,
            "status_id": obj.status_id,
            "account_type_id": obj.account_type_id,
            "note": obj.note,
            "is_linked": obj.is_linked,
            "created_at": int(obj.created_at.timestamp()) if obj.created_at else None,
            "updated_at": int(obj.updated_at.timestamp()) if obj.updated_at else None,
        }
    elif isinstance(obj, Report):
         return {
            "id": obj.id, 
            "social_account_uid": obj.social_account_uid,
            "content_note": obj.content_note,
            "comment": obj.comment,
            "action": obj.action,
            "linked_social_account_uid": obj.linked_social_account_uid,
            "user_id": str(obj.user_id) if obj.user_id else None, # Chuyển UUID user_id sang string
            "created_at": int(obj.created_at.timestamp()) if obj.created_at else None,
            "updated_at": int(obj.updated_at.timestamp()) if obj.updated_at else None,
        }

    logger.warning(f"Unsupported object type for Meilisearch conversion: {type(obj)}")
    return {}


def index_all_data():
    """Đọc toàn bộ dữ liệu từ DB và index vào Meilisearch. Chạy một lần hoặc khi cần re-index."""
    logger.info("Starting full data indexing...")
    db = SessionLocal()
    try:
        # Index Individuals
        individuals = db.query(Individual).all()
        individual_docs = [convert_to_searchable_dict(ind) for ind in individuals if ind]
        if individual_docs:
            task = client.index(INDEX_INDIVIDUALS).add_documents(individual_docs, primary_key='id')
            logger.info(f"Sent {len(individual_docs)} individuals to Meilisearch. Task: {task.task_uid}")
        else:
             logger.info("No individuals found to index.")

        # Index Social Accounts
        social_accounts = db.query(SocialAccount).all()
        social_account_docs = [convert_to_searchable_dict(acc) for acc in social_accounts if acc]
        if social_account_docs:
            task = client.index(INDEX_SOCIAL_ACCOUNTS).add_documents(social_account_docs, primary_key='id') # Dùng id (là uid) đã convert
            logger.info(f"Sent {len(social_account_docs)} social accounts to Meilisearch. Task: {task.task_uid}")
        else:
             logger.info("No social accounts found to index.")

        # Index Reports
        reports = db.query(Report).all()
        report_docs = [convert_to_searchable_dict(rep) for rep in reports if rep]
        if report_docs:
            task = client.index(INDEX_REPORTS).add_documents(report_docs, primary_key='id')
            logger.info(f"Sent {len(report_docs)} reports to Meilisearch. Task: {task.task_uid}")
        else:
             logger.info("No reports found to index.")

    except Exception as e:
        logger.error(f"Error during full data indexing: {e}")
    finally:
        db.close()
    logger.info("Full data indexing finished.")


# Cập nhật bổ sung filter

def search_individuals_meili(query: str, options: Optional[Dict] = None) -> Dict:
    """Tìm kiếm individuals trong Meilisearch, hỗ trợ options (filter, limit, etc.)."""
    try:
        search_params = options if options else {} # Dùng options nếu được cung cấp
        logger.info(f"Searching individuals for '{query}' with options: {search_params}")
        # Truyền trực tiếp options vào hàm search của Meilisearch client
        results = client.index(INDEX_INDIVIDUALS).search(query, search_params)
        logger.info(f"Meilisearch returned {len(results.get('hits', []))} hits for individuals.")
        return results
    except Exception as e:
        logger.error(f"Error searching individuals in Meilisearch: {e}", exc_info=True)
        # Trả về thêm thông tin lỗi nếu cần
        return {"hits": [], "error": str(e), "query": query, "options": options}


def search_social_accounts_meili(query: str, options: Optional[Dict] = None) -> Dict:
     """Tìm kiếm social accounts trong Meilisearch, hỗ trợ options."""
     try:
        search_params = options if options else {}
        logger.info(f"Searching social accounts for '{query}' with options: {search_params}")
        results = client.index(INDEX_SOCIAL_ACCOUNTS).search(query, search_params)
        logger.info(f"Meilisearch returned {len(results.get('hits', []))} hits for social accounts.")
        return results
     except Exception as e:
        logger.error(f"Error searching social accounts in Meilisearch: {e}", exc_info=True)
        return {"hits": [], "error": str(e), "query": query, "options": options}

def search_reports_meili(query: str, options: Optional[Dict] = None) -> Dict:
     """Tìm kiếm reports trong Meilisearch, hỗ trợ options."""
     try:
        search_params = options if options else {}
        logger.info(f"Searching reports for '{query}' with options: {search_params}")
        results = client.index(INDEX_REPORTS).search(query, search_params)
        logger.info(f"Meilisearch returned {len(results.get('hits', []))} hits for reports.")
        return results
     except Exception as e:
        logger.error(f"Error searching reports in Meilisearch: {e}", exc_info=True)
        return {"hits": [], "error": str(e), "query": query, "options": options}


# def search_individuals_meili(query: str, options: Dict = None) -> Dict:
#     """Tìm kiếm individuals trong Meilisearch"""
#     try:
#         logger.info(f"Searching individuals for '{query}' with options: {options}")
#         search_params = options if options else {}
#         #NOTE: Giới hạn kết quả: search_params['limit'] = 20
#         results = client.index(INDEX_INDIVIDUALS).search(query, search_params)
#         logger.info(f"Meilisearch returned {len(results.get('hits', []))} hits for individuals.")
#         return results
#     except Exception as e:
#         logger.error(f"Error searching individuals in Meilisearch: {e}")
#         return {"hits": [], "error": str(e)} 

# def search_social_accounts_meili(query: str, options: Dict = None) -> Dict:
#     """Tìm kiếm tài khoản FB trong Meilisearch"""
#     try:
#         logger.info(f"Searching social accounts for '{query}' with options: {options}")
#         search_params = options if options else {}
#         results = client.index(INDEX_SOCIAL_ACCOUNTS).search(query, search_params)
#         logger.info(f"Meilisearch returned {len(results.get('hits', []))} hits for social accounts.")
#         return results
#     except Exception as e:
#         logger.error(f"Error searching social accounts in Meilisearch: {e}")
#         return {"hits": [], "error": str(e)}

# def search_reports_meili(query: str, options: Dict = None) -> Dict:
#     """Tìm kiếm trích tin trong Meilisearch"""
#     try:
#         logger.info(f"Searching reports for '{query}' with options: {options}")
#         search_params = options if options else {}
#         results = client.index(INDEX_REPORTS).search(query, search_params)
#         logger.info(f"Meilisearch returned {len(results.get('hits', []))} hits for reports.")
#         return results
#     except Exception as e:
#         logger.error(f"Error searching reports in Meilisearch: {e}")
#         return {"hits": [], "error": str(e)}

# --- Các hàm cập nhật Meilisearch (cho đồng bộ hoá) ---

def add_or_update_document(index_name: str, document: Dict, pk_field: str = 'id'): 
    """Thêm hoặc cập nhật 1 document trong Meilisearch. Dùng key 'id' làm PK."""
    try:
        primary_key_value = document.get('id') # Luôn lấy giá trị từ key 'id'
        if primary_key_value is None: # Kiểm tra giá trị None thay vì key thiếu
             logger.error(f"Document missing 'id' field for Meilisearch primary key: {document}")
             return
        logger.debug(f"Adding/Updating document id={primary_key_value} in index {index_name}")
        # Chỉ định primary_key='id' cho Meilisearch biết dùng trường nào
        task = client.index(index_name).add_documents([document], primary_key='id')
    except Exception as e:
        logger.error(f"Error adding/updating document id={document.get('id')} in {index_name}: {e}")


def delete_document(index_name: str, document_id: Union[str, int]):
    """Xoá 1 document khỏi Meilisearch bằng ID (luôn convert sang string)."""
    try:
        str_doc_id = str(document_id) # Đảm bảo ID là string
        logger.debug(f"Deleting document id={str_doc_id} from index {index_name}")
        task = client.index(index_name).delete_document(str_doc_id)
    except Exception as e:
        # ... xử lý lỗi document_not_found ... => Xử lý trường hợp 
        if "document_not_found" in str(e).lower():
             logger.warning(f"Document id={str(document_id)} not found in {index_name} for deletion.")
        else:
             logger.error(f"Error deleting document id={str(document_id)} from {index_name}: {e}", exc_info=True)