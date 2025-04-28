from uuid import uuid4

from app.db.base_class import Base
from sqlalchemy import Boolean, Column, DateTime, String, Integer, ForeignKey, Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Individual(Base):
    """
    Database model for an Individual
    """
    __tablename__='individual'
    id = Column(UUID(as_uuid=True),primary_key=True,nullable=False, default=uuid4)
    full_name = Column(String(255))
    national_id = Column(String(20), default=None)
    citizen_id = Column(String(20), default=None)
    image_url = Column(String(255), default=None)
    date_of_birth= Column(Date, default=None)
    # True is Nam, False is Nu
    is_male = Column(Boolean, default=True)
    hometown= Column(String(255), default=None)
    additional_info = Column(String(5000), default=None)
    phone_number= Column(String(10), default=None)
    is_kol= Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(
        DateTime,
        default=func.now(),
        onupdate=func.now(),
    )
    # color= relationship("color", back_populated="tags")