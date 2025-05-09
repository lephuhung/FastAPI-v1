from uuid import uuid4

from app.db.base_class import Base
from sqlalchemy import Boolean, Column, DateTime, String, Integer, ForeignKey, Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Doituong(Base):
    """
    Database model for an Doituong
    """
    __tablename__='doituong'
    id = Column(UUID(as_uuid=True),primary_key=True,nullable=False, default=uuid4)
    full_name = Column(String(255))
    national_id = Column(String(20), default=None)
    citizen_id = Column(String(20), default=None)
    image_url = Column(String(255), default=None)
    date_of_birth= Column(Date, default=None)
    # True is Nam, False is Nu
    Gioitinh = Column(Boolean, default=True)
    Quequan= Column(String(255), default=None)
    Thongtinbosung = Column(String(5000), default=None)
    SDT= Column(String(10), default=None)
    KOL= Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(
        DateTime,
        default=func.now(),
        onupdate=func.now(),
    )
    # color= relationship("color", back_populated="tags")