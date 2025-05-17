# app/db/listeners.py
from sqlalchemy import event
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.attributes import get_history # Để kiểm tra các trường đã thay đổi (tuỳ chọn) => TODO: nếu cần


from app.models.individual import Individual
from app.models.social_account import SocialAccount
from app.models.report import Report

from app.search import (
    add_or_update_document,
    delete_document,
    convert_to_searchable_dict,
    INDEX_INDIVIDUALS,
    INDEX_SOCIAL_ACCOUNTS,
    INDEX_REPORTS
)

from app.celery_app import (
    update_meilisearch_document_task,
    delete_meilisearch_document_task
)

import logging

logger = logging.getLogger(__name__)

# def is_meilisearch_available():
#     """Kiểm tra nhanh xem Meilisearch có đang hoạt động không."""
#     try:
#         # Sử dụng một lệnh nhẹ nhàng như get health
#         health = meili_client.health()
#         return health.get('status') == 'available'
#     except Exception as e:
#         logger.warning(f"Meilisearch health check failed: {e}")
#         return False

# --- Định nghĩa Listeners cho Model 'Individual' ---

# --- Listener cho Individual Save/Update ---
@event.listens_for(Individual, 'after_insert')
@event.listens_for(Individual, 'after_update')
def after_individual_save_listener(mapper, connection, target: Individual):
    """Gửi task cập nhật Meilisearch cho Individual."""
    record_id = target.id # Lấy ID (UUID)
    model_name = target.__class__.__name__ # Lấy tên class ('Individual')
    logger.info(f"Event triggered: {model_name} {record_id} saved/updated. Sending task to Celery.")
    try:
        # Gửi task vào queue, truyền ID và tên model
        # .delay() là shortcut của .apply_async()
        update_meilisearch_document_task.delay(model_name, record_id)
        logger.debug(f"Task sent for {model_name} {record_id}")
    except Exception as e:
        # Lỗi khi gửi task vào Broker (ví dụ Redis down)
        logger.error(f"Failed to send Celery task for {model_name} {record_id}: {e}", exc_info=True)
        # Cần có cơ chế xử lý lỗi này (ghi log, cảnh báo,...)

# --- Listener cho Individual Delete ---
@event.listens_for(Individual, 'after_delete')
def after_individual_delete_listener(mapper, connection, target: Individual):
    """Gửi task xóa khỏi Meilisearch cho Individual."""
    record_id = target.id
    model_name = target.__class__.__name__
    logger.info(f"Event triggered: {model_name} {record_id} deleted. Sending delete task to Celery.")
    try:
        delete_meilisearch_document_task.delay(model_name, record_id)
        logger.debug(f"Delete task sent for {model_name} {record_id}")
    except Exception as e:
        logger.error(f"Failed to send Celery delete task for {model_name} {record_id}: {e}", exc_info=True)

# --- Listener cho SocialAccount Save/Update ---
@event.listens_for(SocialAccount, 'after_insert')
@event.listens_for(SocialAccount, 'after_update')
def after_social_account_save_listener(mapper, connection, target: SocialAccount):
    """Gửi task cập nhật Meilisearch cho SocialAccount."""
    record_id = target.uid # ID cho SocialAccount là uid (string)
    model_name = target.__class__.__name__
    logger.info(f"Event triggered: {model_name} {record_id} saved/updated. Sending task to Celery.")
    try:
        update_meilisearch_document_task.delay(model_name, record_id)
        logger.debug(f"Task sent for {model_name} {record_id}")
    except Exception as e:
        logger.error(f"Failed to send Celery task for {model_name} {record_id}: {e}", exc_info=True)

# --- Listener cho SocialAccount Delete ---
@event.listens_for(SocialAccount, 'after_delete')
def after_social_account_delete_listener(mapper, connection, target: SocialAccount):
    """Gửi task xóa khỏi Meilisearch cho SocialAccount."""
    record_id = target.uid
    model_name = target.__class__.__name__
    logger.info(f"Event triggered: {model_name} {record_id} deleted. Sending delete task to Celery.")
    try:
        delete_meilisearch_document_task.delay(model_name, record_id)
        logger.debug(f"Delete task sent for {model_name} {record_id}")
    except Exception as e:
        logger.error(f"Failed to send Celery delete task for {model_name} {record_id}: {e}", exc_info=True)


# --- Listener cho Report Save/Update ---
@event.listens_for(Report, 'after_insert')
@event.listens_for(Report, 'after_update')
def after_report_save_listener(mapper, connection, target: Report):
    """Gửi task cập nhật Meilisearch cho Report."""
    record_id = target.id # ID cho Report là id (int)
    model_name = target.__class__.__name__
    logger.info(f"Event triggered: {model_name} {record_id} saved/updated. Sending task to Celery.")
    try:
        update_meilisearch_document_task.delay(model_name, record_id)
        logger.debug(f"Task sent for {model_name} {record_id}")
    except Exception as e:
        logger.error(f"Failed to send Celery task for {model_name} {record_id}: {e}", exc_info=True)


# --- Listener cho Report Delete ---
@event.listens_for(Report, 'after_delete')
def after_report_delete_listener(mapper, connection, target: Report):
    """Gửi task xóa khỏi Meilisearch cho Report."""
    record_id = target.id
    model_name = target.__class__.__name__
    logger.info(f"Event triggered: {model_name} {record_id} deleted. Sending delete task to Celery.")
    try:
        delete_meilisearch_document_task.delay(model_name, record_id)
        logger.debug(f"Delete task sent for {model_name} {record_id}")
    except Exception as e:
        logger.error(f"Failed to send Celery delete task for {model_name} {record_id}: {e}", exc_info=True)

# 