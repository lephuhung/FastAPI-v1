import meilisearch
import os
import logging
from typing import List, Dict, Any, Union, Optional
from sqlalchemy.orm import Session 

from app.db.session import SessionLocal 
from app.models.individual import Individual
from app.models.social_account import SocialAccount
from app.models.report import Report
from app.models.user import User 

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

MEILI_HOST = os.getenv("MEILI_HOST", "http://meilisearch:7700")
MEILI_MASTER_KEY = os.getenv("MEILI_MASTER_KEY", "TODO_SECURE_MASTER_KEY")

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
def setup_meilisearch_indexes():
    if not client:
        logger.error("Meilisearch client not available. Skipping index setup.")
        return
    try:
        # Index Individuals
     
        client.create_index(INDEX_INDIVIDUALS, {'primaryKey': 'id'})
        client.index(INDEX_INDIVIDUALS).update_settings({
            'searchableAttributes': ['full_name', 'national_id', 'citizen_id', 'additional_info', 'phone_number', 'hometown'],
            'filterableAttributes': ['is_kol', 'created_at', 'updated_at'],
            'sortableAttributes': ['created_at', 'updated_at', 'full_name']
        })
        logger.info(f"Index '{INDEX_INDIVIDUALS}' setup complete.")

        # Index Social Accounts
        client.create_index(INDEX_SOCIAL_ACCOUNTS, {'primaryKey': 'id'})
        client.index(INDEX_SOCIAL_ACCOUNTS).update_settings({
            'searchableAttributes': ['uid', 'name', 'phone_number', 'note'],
            'filterableAttributes': ['status_id', 'type_id', 'is_active', 'created_at', 'updated_at'],
            'sortableAttributes': ['created_at', 'updated_at', 'reaction_count', 'name']
        })
        logger.info(f"Index '{INDEX_SOCIAL_ACCOUNTS}' setup complete.")

        # Index Reports
        client.create_index(INDEX_REPORTS, {'primaryKey': 'id'})
        client.index(INDEX_REPORTS).update_settings({
            'searchableAttributes': ['social_account_uid', 'content_note', 'comment', 'action', 'related_social_account_uid', 'username'],
            'filterableAttributes': ['social_account_uid', 'user_id', 'username', 'related_social_account_uid', 'created_at', 'updated_at'],
            'sortableAttributes': ['created_at', 'updated_at']
        })
        logger.info(f"Index '{INDEX_REPORTS}' setup complete.")
    except Exception as e:
        logger.error(f"Error setting up Meilisearch indexes: {e}")

def convert_to_searchable_dict(obj: Any, db: Session) -> Dict[str, Any]:
    """Chuyển đổi SQLAlchemy object thành dict phù hợp cho Meilisearch, sử dụng db session được cung cấp."""
    if isinstance(obj, Individual):
        return {
            "id": str(obj.id), 
            "full_name": obj.full_name,
            "national_id": obj.national_id,
            "citizen_id": obj.citizen_id,
            "image_url": obj.image_url,
            "date_of_birth": obj.date_of_birth.isoformat() if obj.date_of_birth else None,
            "is_male": obj.is_male,
            "hometown": obj.hometown,
            "additional_info": obj.additional_info,
            "phone_number": obj.phone_number,
            "is_kol": obj.is_kol,
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
            "type_id": obj.type_id,
            "note": obj.note,
            "is_active": obj.is_active,
            "created_at": int(obj.created_at.timestamp()) if obj.created_at else None,
            "updated_at": int(obj.updated_at.timestamp()) if obj.updated_at else None,
        }
    elif isinstance(obj, Report):
        user_username = None
        if obj.user_id: 
            user = db.query(User).filter(User.id == obj.user_id).first()
            if user:
                user_username = user.username
        return {
            "id": obj.id, 
            "social_account_uid": obj.social_account_uid,
            "content_note": obj.content_note,
            "comment": obj.comment,
            "action": obj.action,
            "related_social_account_uid": obj.related_social_account_uid,
            "user_id": str(obj.user_id) if obj.user_id else None,
            "username": user_username,
            "created_at": int(obj.created_at.timestamp()) if obj.created_at else None,
            "updated_at": int(obj.updated_at.timestamp()) if obj.updated_at else None,
        }

    logger.warning(f"Unsupported object type for Meilisearch conversion: {type(obj)}")
    return {}


def index_all_data():
    """Đọc toàn bộ dữ liệu từ DB và index vào Meilisearch. Chạy một lần hoặc khi cần re-index"""
    if not client:
        logger.error("Meilisearch client not available. Skipping full data indexing.")
        return

    logger.info("Starting full data indexing...")
    db = SessionLocal() 
    try:
        # Index Individuals
        individuals = db.query(Individual).all()

        individual_docs = [convert_to_searchable_dict(ind, db) for ind in individuals if ind]
        if individual_docs:
            task = client.index(INDEX_INDIVIDUALS).add_documents(individual_docs, primary_key='id')
            logger.info(f"Sent {len(individual_docs)} individuals to Meilisearch. Task: {task.task_uid if hasattr(task, 'task_uid') else task['uid']}")
        else:
            logger.info("No individuals found to index.")

        # Index Social Accounts
        social_accounts = db.query(SocialAccount).all()
        social_account_docs = [convert_to_searchable_dict(acc, db) for acc in social_accounts if acc]
        if social_account_docs:
            task = client.index(INDEX_SOCIAL_ACCOUNTS).add_documents(social_account_docs, primary_key='id')
            logger.info(f"Sent {len(social_account_docs)} social accounts to Meilisearch. Task: {task.task_uid if hasattr(task, 'task_uid') else task['uid']}")
        else:
            logger.info("No social accounts found to index.")

        # Index Reports
        reports = db.query(Report).all()
        report_docs = [convert_to_searchable_dict(rep, db) for rep in reports if rep]
        if report_docs:
            task = client.index(INDEX_REPORTS).add_documents(report_docs, primary_key='id')
            logger.info(f"Sent {len(report_docs)} reports to Meilisearch. Task: {task.task_uid if hasattr(task, 'task_uid') else task['uid']}")
        else:
            logger.info("No reports found to index.")

    except Exception as e:
        logger.error(f"Error during full data indexing: {e}", exc_info=True) 
    finally:
        db.close() 
    logger.info("Full data indexing finished.")


def search_individuals_meili(query: str, options: Optional[Dict] = None) -> Dict:
    if not client: return {"hits": [], "error": "Meilisearch client not available."}
    try:
        search_params = options if options else {}
        
        results = client.index(INDEX_INDIVIDUALS).search(query, search_params)
        return results
    except Exception as e:
        logger.error(f"Error searching individuals in Meilisearch: {e}", exc_info=True)
        return {"hits": [], "error": str(e), "query": query, "options": options}

def search_social_accounts_meili(query: str, options: Optional[Dict] = None) -> Dict:
    if not client: return {"hits": [], "error": "Meilisearch client not available."}
    try:
        search_params = options if options else {}
        results = client.index(INDEX_SOCIAL_ACCOUNTS).search(query, search_params)
        return results
    except Exception as e:
        logger.error(f"Error searching social accounts in Meilisearch: {e}", exc_info=True)
        return {"hits": [], "error": str(e), "query": query, "options": options}

def search_reports_meili(query: str, options: Optional[Dict] = None) -> Dict:
    if not client: return {"hits": [], "error": "Meilisearch client not available."}
    try:
        search_params = options if options else {}
        results = client.index(INDEX_REPORTS).search(query, search_params)
        return results
    except Exception as e:
        logger.error(f"Error searching reports in Meilisearch: {e}", exc_info=True)
        return {"hits": [], "error": str(e), "query": query, "options": options}


# --- Các hàm cập nhật Meilisearch (cho đồng bộ hoá) ---
def add_or_update_document(index_name: str, obj: Any, db: Session): 
    if not client:
        logger.error(f"Meilisearch client not available. Cannot add/update document in {index_name}.")
        return

    document = convert_to_searchable_dict(obj, db) 
    if not document or not isinstance(document, dict): # Ensure document is a valid dict
        logger.warning(f"Failed to convert object to a valid searchable dict for index {index_name}. Object: {obj}, Converted: {document}")
        return

    try:
        primary_key_value = document.get('id') 
        if primary_key_value is None:
            logger.error(f"Document missing 'id' field for Meilisearch primary key in index {index_name}: {document}")
            return

        task = client.index(index_name).add_documents([document], primary_key='id')
        logger.info(f"Add/Update task for document id={primary_key_value} in {index_name}. Task: {task.task_uid if hasattr(task, 'task_uid') else task['uid']}")
    except Exception as e:
        logger.error(f"Error adding/updating document id={document.get('id', 'UNKNOWN')} in {index_name}: {e}", exc_info=True)


def delete_document(index_name: str, document_id: Union[str, int]):
    if not client:
        logger.error(f"Meilisearch client not available. Cannot delete document from {index_name}.")
        return
    try:
        str_doc_id = str(document_id) # Ensure ID is string for Meilisearch
        # logger.debug(f"Deleting document id={str_doc_id} from index {index_name}")
        task = client.index(index_name).delete_document(str_doc_id)
        logger.info(f"Delete task for document id={str_doc_id} from {index_name}. Task: {task.task_uid if hasattr(task, 'task_uid') else task['uid']}")
    except Exception as e:
        if "document_not_found" in str(e).lower(): # More robust check for document not found
            logger.warning(f"Document id={str(document_id)} not found in {index_name} for deletion.")
        else:
            logger.error(f"Error deleting document id={str(document_id)} from {index_name}: {e}", exc_info=True)

