# import os
# import ssl
# from typing import AsyncGenerator
# from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
# from sqlalchemy.orm import sessionmaker

# DATABASE_URL = os.getenv("DATABASE_URL")

# ssl_context = ssl.create_default_context()
# ssl_context.check_hostname = False
# ssl_context.verify_mode = ssl.CERT_NONE

# connect_args = {
#     "ssl": ssl_context
# }

# engine = create_async_engine(
#     DATABASE_URL,
#     echo=True,
#     connect_args=connect_args
# )

# async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

# async def get_session() -> AsyncGenerator[AsyncSession, None]:
#     async with async_session() as session:
#         yield session

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.core.config import DATABASE_URL

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

async def get_session() -> AsyncSession: # type: ignore
    async with async_session() as session:
        yield session
