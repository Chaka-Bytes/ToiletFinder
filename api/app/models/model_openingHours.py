from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.db.database import Base
from sqlalchemy.orm import relationship

class OpeningHours(Base):
    __tablename__ = "openingHours"

    id = Column(Integer, primary_key=True, index=True)
    open_time = Column(String(255))
    close_time = Column(String(255))
    toilet_id = Column(Integer, ForeignKey('toilets.id')) # FK toilet

    related_toilet = relationship("Toilet", back_populates="opening_hours")