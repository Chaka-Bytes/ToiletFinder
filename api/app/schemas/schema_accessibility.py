from pydantic import BaseModel

class AccessibilityBase(BaseModel):
    toilet_id: int
    wheelchair_accessible: bool
    gender_neutral: bool

class AccessibilityCreate(AccessibilityBase):
    pass

class Accessibility(AccessibilityBase):
    id: int
    class Config:
        orm_mode = True
