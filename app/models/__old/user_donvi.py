from uuid import uuid4
from pydantic import UUID4
from app.db.base_class import Base
from sqlalchemy import Boolean, Column, DateTime, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship



class user_donvi(Base):
    """
    Database model for an user_donvi table
    """
    __tablename__ = 'user_donvi'
    id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    user_id = Column(UUID(as_uuid=True),ForeignKey("user.id"),primary_key=True,nullable=False)
    donvi_id = Column(UUID(as_uuid=True),ForeignKey("donvi.id"),primary_key=True,nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(
        DateTime,
        default=func.now(),
        onupdate=func.now(),
    )
