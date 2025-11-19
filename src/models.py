from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from .database import Base


class Baby(Base):
    __tablename__ = "babies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    birth_date = Column(String, nullable=False)
    gender = Column(String, nullable=False)

    # relação com medições
    measurements = relationship("Measurement", back_populates="baby")


class Measurement(Base):
    __tablename__ = "measurements"

    id = Column(Integer, primary_key=True, index=True)
    baby_id = Column(Integer, ForeignKey("babies.id"))
    temperature = Column(Float, nullable=False)
    heart_rate = Column(Integer, nullable=True)
    breathing_rate = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # relação com Baby
    baby = relationship("Baby", back_populates="measurements")
 
