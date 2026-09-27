import asyncio
import asyncpg

DATABASE = "postgresql://myuser:qwerty@127.0.0.1:5432/mydatabase"

async def test():
    conn = await asyncpg.connect(DATABASE)
    print("Подключение успешно!")

    values = await conn.fetch("SELECT version()")
    print("Версия PostgreSQL:", values[0]['version'])

    await conn.close()

if __name__ == "__test__":
    asyncio.run(test())