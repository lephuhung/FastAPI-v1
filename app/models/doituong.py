import datetime
from uuid import uuid4

from app.db.base_class import Base
from sqlalchemy import Boolean, Column, DateTime, String, Integer, ForeignKey, Nullable
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Doituong(Base):
    """
    Database model for an Doituong
    """

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    CMND = Column(String(20), default=Nullable)
    CCCD = Column(String(20), default=Nullable)
    Image = Column(String(255), default=Nullable)
    Ngaysinh= Column(DateTime, default=Nullable)
    # True is Nam, False is Nu
    Gioitinh = Column(Boolean, default=True)
    Quequan= Column(String(255), default=Nullable)
    Thongtinbosung = Column(String(5000), default=Nullable)
    SDT= Column(String(10), default=Nullable)
    KOL= Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )
    color= relationship("color", back_populated="tags")