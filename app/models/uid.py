from app.db.base_class import Base
from sqlalchemy import Boolean, Column, DateTime, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class uid(Base):
    """
    Database model for an uid
    """
    __tablename__ = 'uid'
    id = Column(Integer, primary_key=True, index=True,nullable=False, autoincrement=True)
    uid = Column(String(20))
    name = Column(String(255))
    reaction = Column(Integer)
    phone_number = Column(String(10), default="Unknown")
    status = Column(Integer, ForeignKey('status.id'))
    account_type_id = Column(Integer, ForeignKey('type.id'))
    note = Column(String(5000), nullable=True)
    Vaiao= Column(Boolean(), default=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(
        DateTime,
        default=func.now(),
        onupdate=func.now(),
    )

    # models = relationship("", back_populates="account")