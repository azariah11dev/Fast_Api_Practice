import uuid

from sqlalchemy import Column, String, Text, DateTime
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker, AsyncGenerator
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime
from sqlalchemy.sql import func


DATABASE_URL = "sqlite+aiosqlite:///./test.db"

class Database(DeclarativeBase):
    __tablename__= "items"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    caption = Column(Text)
    url = Column(String, nullable=False)
    file_type = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())


engine = create_async_engine(DATABASE_URL, echo=True)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(DeclarativeBase.metadata.create_all)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session