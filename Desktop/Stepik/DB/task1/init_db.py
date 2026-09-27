import asyncpg
import asyncio
import sys
DATABASE_URL = "postgresql://myuser:qwerty@127.0.0.1:5432/mydatabase"



async def create_table():
    conn = await asyncpg.connect(DATABASE_URL)
    await conn.execute('''
        CREATE TABLE IF NOT EXISTS Rodion (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL
        )
    ''')
    await conn.close()

asyncio.run(create_table())

