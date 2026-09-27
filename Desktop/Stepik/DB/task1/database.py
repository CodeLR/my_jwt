import asyncpg

DATABASE="postgresql://myuser:qwerty@127.0.0.1:5432/mydatabase"

async def test_connection():
    conn = await asyncpg.connect(DATABASE)
    print("connect")
    await conn.close()

async def get_db_connection():
    conn= await asyncpg.connect(DATABASE)
    print("connect")
    try:
        yield conn
    finally:
        conn.close()


    
