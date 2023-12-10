import datetime
from uuid import uuid4

from app.db.base_class import Base
from sqlalchemy import Boolean, Column, DateTime, String, Integer, ForeignKey, Nullable
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class trangthai(Base):
    """
    Database model for an uid
    """

    id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    trangtha_name = Column(String(255))
    color = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )
    color = relationship("trangthai", back_populates="color")