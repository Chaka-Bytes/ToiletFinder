from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from app.db.database import Base
from sqlalchemy.orm import relationship

class Accessibility(Base):
    __tablename__ = "accessibility"

    id = Column(Integer, primary_key=True, index=True)
    wheelchair_accessible = Column(Boolean)
    gender_neutral = Column(Boolean)
    toilet_id = Column(Integer, ForeignKey('toilets.id')) # FK toilet

    related_toilet = relationship("Toilet", back_populates="accessibility")