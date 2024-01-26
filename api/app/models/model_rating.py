from sqlalchemy import Column, Integer, ForeignKey
from app.db.database import Base
from sqlalchemy.orm import relationship

class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True, index=True)
    rating = Column(Integer)
    rating_count = Column(Integer)
    toilet_id = Column(Integer, ForeignKey('toilets.id')) # FK toilet

    related_toilet = relationship("Toilet", back_populates="ratings")