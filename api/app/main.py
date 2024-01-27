from fastapi import FastAPI
#from app.db.database import init_db

app = FastAPI()

    
@app.get("/")
def read_root():
    return {"Hello": "World"}
