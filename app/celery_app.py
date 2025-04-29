# app/celery_app.py
import os
from celery import Celery
from kombu import Queue, Exchange 
import logging
import time
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.models.individual import Individual
from app.models.social_account import SocialAccount
from app.models.report import Report

from app.search import (
    add_or_update_document,
    delete_document,
    convert_to_searchable_dict,
    INDEX_INDIVIDUALS,
    INDEX_SOCIAL_ACCOUNTS,
    INDEX_REPORTS,
    is_meilisearch_available 
)

logger = logging.getLogger(__name__)

# Lấy cấu hình từ environment variables
# Sử dụng redis làm broker và result backend
# redis://<hostname>:<port>/<database_number>
broker_url = os.getenv('CELERY_BROKER_URL', 'redis://redis:6379/0')
result_backend = os.getenv('CELERY_RESULT_BACKEND', 'redis://redis:6379/1')

# --- Khởi tạo Celery application ---
celery = Celery(
    __name__, 
    broker=broker_url,
    backend=result_backend,
    include=['app.celery_app'] # List các modules chứa tasks để worker tự động tìm thấy
)

# --- Cấu hình Celery (tùy chọn nâng cao) ---
celery.conf.update(
    task_serializer='json', # Định dạng dữ liệu task
    accept_content=['json'],
    result_serializer='json',
    timezone='Asia/Ho_Chi_Minh',
    enable_utc=True,
    worker_concurrency=4, # Số task chạy đồng thời trên mỗi worker (điều chỉnh theo tài nguyên)
    worker_prefetch_multiplier=1, # Worker lấy 1 task mỗi lần (tốt cho task chạy lâu/không chắc chắn)
    task_acks_late=True, # Worker chỉ xác nhận task hoàn thành sau khi chạy xong (an toàn hơn)
    task_reject_on_worker_lost=True, # Gửi lại task nếu worker bị mất đột ngột
    # Cấu hình retry mặc định (có thể override trong từng task)
    task_publish_retry_policy = {
        'max_retries': 3, # Thử lại tối đa 3 lần
        'interval_start': 0, # Bắt đầu thử lại ngay lập tức
        'interval_step': 0.2, # Tăng thời gian chờ lên 0.2s mỗi lần
        'interval_max': 0.2, # Thời gian chờ tối đa giữa các lần thử lại là 0.2s
    },
    # Định nghĩa queues (giúp phân loại task)
    # task_queues=(
    #     Queue('default', Exchange('default'), routing_key='default'),
    #     Queue('meilisearch_sync', Exchange('meilisearch_sync'), routing_key='meilisearch.#'),
    # ),
    # task_default_queue='default',
    # task_default_exchange='default',
    # task_default_routing_key='default',
)

# --- Định nghĩa Celery Tasks ---

# Mapping từ tên model (string) sang class model thực tế
MODEL_MAP = {
    'Individual': Individual,
    'SocialAccount': SocialAccount,
    'Report': Report,
}

@celery.task(
    bind=True, # Cho phép truy cập task instance (self)
    autoretry_for=(Exception,), # Tự động retry cho các Exception cơ bản
    retry_kwargs={'max_retries': 5, 'countdown': 5}, # Thử lại 5 lần, chờ 5s giữa các lần
    name='tasks.update_meilisearch_document' # Tên task rõ ràng
)
def update_meilisearch_document_task(self, model_name: str, record_id: any):
    """
    Celery task để thêm/cập nhật document trong Meilisearch.
    Task này sẽ fetch lại object từ DB.
    """
    logger.info(f"Task received: Update Meilisearch for {model_name} with ID {record_id}")

    if not is_meilisearch_available():
        logger.warning(f"Meilisearch unavailable. Retrying task for {model_name} ID {record_id}...")
        # `autoretry_for` sẽ tự động retry khi có Exception, nhưng có thể retry thủ công nếu muốn
        # raise ConnectionError("Meilisearch is unavailable")
        # Hoặc sử dụng retry của celery => đang sử dụng Celery
        try:
            # Chờ theo cấp số nhân: 2, 4, 8, 16, 32 giây (tối đa 1 phút)
            countdown = 2 ** self.request.retries
            logger.info(f"Retrying in {countdown} seconds...")
            raise self.retry(countdown=countdown, exc=ConnectionError("Meilisearch unavailable"))
        except self.MaxRetriesExceededError:
            logger.error(f"Max retries exceeded for {model_name} ID {record_id}. Giving up.")
            return 

    ModelClass = MODEL_MAP.get(model_name)
    if not ModelClass:
        logger.error(f"Unknown model name '{model_name}' received in task. Cannot process ID {record_id}.")
        return 

    db: Session = SessionLocal() # Tạo session DB mới cho task này
    record = None
    try:
        logger.debug(f"Fetching {model_name} with ID {record_id} from database...")
        if model_name == 'Individual':
            record = db.query(ModelClass).filter(ModelClass.id == record_id).first()
        elif model_name == 'SocialAccount':
             # ID truyền vào là uid (string)
            record = db.query(ModelClass).filter(ModelClass.uid == str(record_id)).first()
        elif model_name == 'Report':
             # ID truyền vào là id (int) => TODO: Xem lại tại trong DB gốc của anh là Integer
            record = db.query(ModelClass).filter(ModelClass.id == int(record_id)).first()

        if record:
            logger.debug(f"Record found. Converting {model_name} ID {record_id} for Meilisearch.")
            doc = convert_to_searchable_dict(record)
            if doc:
                index_name = ""
                pk_field = 'id'
                if model_name == 'Individual': index_name = INDEX_INDIVIDUALS
                elif model_name == 'SocialAccount': index_name = INDEX_SOCIAL_ACCOUNTS
                elif model_name == 'Report': index_name = INDEX_REPORTS

                if index_name:
                    logger.debug(f"Adding/Updating document in Meilisearch index '{index_name}'...")
                    add_or_update_document(index_name, doc, pk_field=pk_field)
                    logger.info(f"Successfully updated Meilisearch for {model_name} ID {record_id}.")
                else:
                     logger.error(f"No index name configured for model {model_name}.")
            else:
                logger.warning(f"Failed to convert {model_name} ID {record_id} to searchable dict.")
        else:
            # Record không tìm thấy trong DB (có thể đã bị xóa trước khi task chạy)
            logger.warning(f"{model_name} with ID {record_id} not found in DB. It might have been deleted. Skipping Meilisearch update.")

    except Exception as exc:
        logger.error(f"Error processing task for {model_name} ID {record_id}: {exc}", exc_info=True)
        try:
            # Tăng thời gian chờ giữa các lần retry
            countdown = 10 * (self.request.retries + 1)
            logger.info(f"Retrying task due to error in {countdown} seconds...")
            raise self.retry(exc=exc, countdown=countdown)
        except self.MaxRetriesExceededError:
            logger.error(f"Max retries exceeded for task {model_name} ID {record_id} after error. Giving up.")
    finally:
        db.close()


@celery.task(
    bind=True,
    autoretry_for=(Exception,),
    retry_kwargs={'max_retries': 5, 'countdown': 5},
    name='tasks.delete_meilisearch_document'
)
def delete_meilisearch_document_task(self, model_name: str, record_id: any):
    """
    Celery task để xóa document khỏi Meilisearch.
    Không cần truy vấn DB.
    """
    logger.info(f"Task received: Delete Meilisearch document for {model_name} with ID {record_id}")

    if not is_meilisearch_available():
        logger.warning(f"Meilisearch unavailable. Retrying delete task for {model_name} ID {record_id}...")
        try:
            countdown = 2 ** self.request.retries
            logger.info(f"Retrying in {countdown} seconds...")
            raise self.retry(countdown=countdown, exc=ConnectionError("Meilisearch unavailable"))
        except self.MaxRetriesExceededError:
            logger.error(f"Max retries exceeded for delete task {model_name} ID {record_id}. Giving up.")
            return

    try:
        index_name = ""
        doc_id = str(record_id) 

        if model_name == 'Individual': index_name = INDEX_INDIVIDUALS
        elif model_name == 'SocialAccount': index_name = INDEX_SOCIAL_ACCOUNTS
        elif model_name == 'Report': index_name = INDEX_REPORTS

        if index_name:
            logger.debug(f"Deleting document ID {doc_id} from Meilisearch index '{index_name}'...")
            delete_document(index_name, doc_id)
            logger.info(f"Successfully sent delete request to Meilisearch for {model_name} ID {doc_id}.")
        else:
             logger.error(f"No index name configured for model {model_name} to delete ID {doc_id}.")

    except Exception as exc:
        # Lỗi document_not_found thường không cần retry, các lỗi khác thì nên retry
        if "document_not_found" in str(exc).lower():
            logger.warning(f"Document {model_name} ID {record_id} already deleted or never existed in Meilisearch.")
        else:
            logger.error(f"Error processing delete task for {model_name} ID {record_id}: {exc}", exc_info=True)
            try:
                countdown = 10 * (self.request.retries + 1)
                logger.info(f"Retrying delete task due to error in {countdown} seconds...")
                raise self.retry(exc=exc, countdown=countdown)
            except self.MaxRetriesExceededError:
                logger.error(f"Max retries exceeded for delete task {model_name} ID {record_id} after error. Giving up.")