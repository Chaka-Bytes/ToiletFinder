from fastapi import FastAPI
#from app.db.database import init_db
from app.crud import crud_toilet
from app.db.database import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()



# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

@app.get("/toilets")
# create "/toilets" endpoint to get all toilets using crud_toilet.py read_toilets function
def read_toilets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_toilet.get_toilets(db, skip, limit)