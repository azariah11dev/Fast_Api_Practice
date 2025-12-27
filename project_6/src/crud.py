from sqlalchemy import select
from src.models import OHLCV

async def create_ohlcv(db, data):
    db_obj = OHLCV(**data)
    db.add(db_obj)
    await db.commit()
    await db.refresh(db_obj)
    return db_obj

async def get_ohlcv(db, ticker: str):
    stmt = select(OHLCV).where(OHLCV.ticker == ticker)
    result = await db.execute(stmt)
    return result.scalars().all()