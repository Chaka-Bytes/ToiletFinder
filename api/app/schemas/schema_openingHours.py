from pydantic import BaseModel

class OpeningHoursBase(BaseModel):
    open_time: str
    close_time: str
    toilet_id: int

class OpeningHoursCreate(OpeningHoursBase):
    pass

class OpeningHours(OpeningHoursBase):
    id: int
    class Config:
        orm_mode = True