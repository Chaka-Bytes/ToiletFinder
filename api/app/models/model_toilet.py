from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.db.base import Base
from sqlalchemy.orm import relationship

class Toilet(Base):
    __tablename__ = "toilets"

    id = Column(Integer, primary_key=True, index=True) 
    name = Column(String(255))
    latitude = Column(Float)
    longitude = Column(Float)
    
    opening_hours = relationship("OpeningHours", back_populates="related_toilet")
    accessibility = relationship("Accessibility", back_populates="related_toilet")
    ratings = relationship("Rating", back_populates="related_toilet")
