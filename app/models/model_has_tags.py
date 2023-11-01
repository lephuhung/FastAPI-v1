import datetime
from uuid import uuid4

from app.db.base_class import Base
from sqlalchemy import Boolean, Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Model_has_tags(Base):
    """
    Database model for an account
    """

    id = Column(
        UUID(as_uuid=True), primary_key=True, index=True, default=uuid4
    )
    model_id = Column(UUID(as_uuid=True))
    tags_id = Column(UUID(as_uuid=True))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )

    # models = relationship("", back_populates="account")