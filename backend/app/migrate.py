import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text

DATABASE_URL = "postgresql+asyncpg://postgres:"

engine = create_async_engine(DATABASE_URL, echo=True)

async def run_alter():
    async with engine.begin() as conn:
        await conn.execute(text('''
            ALTER TABLE contacts
            ADD COLUMN IF NOT EXISTS logradouro VARCHAR(255) NOT NULL DEFAULT '',
            ADD COLUMN IF NOT EXISTS bairro VARCHAR(100) NOT NULL DEFAULT '',
            ADD COLUMN IF NOT EXISTS cidade VARCHAR(100) NOT NULL DEFAULT '',
            ADD COLUMN IF NOT EXISTS estado VARCHAR(2) NOT NULL DEFAULT '';
        '''))

if __name__ == "__main__":
    asyncio.run(run_alter())
