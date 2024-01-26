from pydantic import BaseModel, Field

class RatingBase(BaseModel):
    toilet_id: int
    rating: int
    rating_count: int

class RatingCreate(RatingBase):
    pass

class Rating(RatingBase):
    id: int
    class Config:
        orm_mode = True