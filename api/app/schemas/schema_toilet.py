from pydantic import BaseModel

class ToiletBase(BaseModel):
    name: str
    latitude: float
    longitude: float

class ToiletCreate(ToiletBase):
    pass

class Toilet(ToiletBase):
    toilet_id: int
    class Config:
        orm_mode = True

