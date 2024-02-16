from sqlalchemy.orm import Session
from app.models import model_toilet
from app.schemas import schema_toilet

def get_toilets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model_toilet.Toilet).offset(skip).limit(limit).all()