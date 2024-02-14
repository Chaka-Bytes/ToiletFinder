from fastapi import FastAPI
#from app.db.database import init_db
from app.crud import crud_toilet
from app.db.database import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
app = FastAPI()

    
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/toilets")
# create "/toilets" endpoint to get all toilets using crud_toilet.py read_toilets function
def read_toilets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_toilet.get_toilets(db, skip, limit)