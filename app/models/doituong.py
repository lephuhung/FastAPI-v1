import datetime
from uuid import uuid4

from app.db.base_class import Base
from sqlalchemy import Boolean, Column, DateTime, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Doituong(Base):
    """
    Database model for an Doituong
    """
    __tablename__='doituong'
    id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    name = Column(String(255))
    CMND = Column(String(20), default=None)
    CCCD = Column(String(20), default=None)
    Image = Column(String(255), default=None)
    Ngaysinh= Column(DateTime, default=None)
    # True is Nam, False is Nu
    Gioitinh = Column(Boolean, default=True)
    Quequan= Column(String(255), default=None)
    Thongtinbosung = Column(String(5000), default=None)
    SDT= Column(String(10), default=None)
    KOL= Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )
    # color= relationship("color", back_populated="tags")