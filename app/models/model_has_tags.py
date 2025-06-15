from uuid import uuid4
from sqlalchemy.sql import func

from app.db.base_class import Base
from sqlalchemy import Boolean, Column, DateTime, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class model_has_tags(Base):
    """
    Database model for an account
    """
    __tablename__ = 'model_has_tags'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    model_id = Column(String(255))
    tags_id = Column(Integer, ForeignKey("tags.id"), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(
        DateTime,
        default=func.now(),
        onupdate=func.now(),
    )

    # models = relationship("", back_populates="account")