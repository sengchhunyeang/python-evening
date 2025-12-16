import asyncio
import asyncpg


async def connect():
    conn = await asyncpg.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="12345",
        port="5432"
    )

    rows = await conn.fetch('SELECT version();')
    print(rows)

    await conn.close()
asyncio.run(connect())
