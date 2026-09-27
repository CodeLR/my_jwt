from pydantic import BaseModel
from fastapi import FastAPI, Depends
from database import get_db_connection,test_connection
import asyncpg


app = FastAPI()

class Item(BaseModel):
    name: str

@app.post("/items")
async def create_item(item: Item, db: asyncpg.Connection = Depends(get_db_connection)):
    await db.execute('''
        INSERT INTO Rodion(name) VALUES($1)
    ''', item.name)
    return {"message": "Item added successfully!"}


@app.get('/')
async def get_table(conn=Depends(get_db_connection)):
   
    return {"OK": True}
    
