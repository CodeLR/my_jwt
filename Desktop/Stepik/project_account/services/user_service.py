from database import get_db
from sqlalchemy.orm import Session
from models.user import User
from fastapi import Depends

def update_user_name(db:Session,user:User,name:str):
    if not name.strip():
        return None
    else:
        user.name=name.strip()
        db.commit()
        db.refresh(user)
