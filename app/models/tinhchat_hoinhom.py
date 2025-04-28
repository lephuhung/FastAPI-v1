from uuid import uuid4

from app.db.base_class import Base
from sqlalchemy import Boolean, Column, DateTime, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class characteristic_hoinhom(Base):
    """
    Database model for an characteristic hoinhom
    """
    __tablename__='characteristic_hoinhom'
    id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    characteristic_id = Column(Integer, ForeignKey('characteristic.id'), nullable=False)
    uid= Column(String(20), ForeignKey('uid.uid'), nullable=False) 
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(
        DateTime,
        default=func.now(),
        onupdate=func.now(),
    )
    # tinchat = relationship('characteristic')