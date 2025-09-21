from fastapi import FastAPI, Depends
from db.database import engine, get_db
from db.models import User
from sqlalchemy.orm import Session

app = FastAPI()

@app.get("/users")
def get_users(db:Session = Depends(get_db)):
    users = db.query(User).all()
    return users

@app.get("/")
def root():
    return {"ok": True}