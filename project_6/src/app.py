from fastapi import FastAPI, Depends
from src.database import SessionLocal
from src.schemas import OHLCV_Create, OHLCV_Read
from src.crud import create_ohlcv, get_ohlcv
from src.services.market_data import fetch_ohlcv

app = FastAPI()

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()

@app.post("/{ticker}", response_model=OHLCV_Read)
async def create_ohlcv_endpoint(ticker: str, db=Depends(get_db)):
    data = await fetch_ohlcv(ticker)
    db_obj = await create_ohlcv(db, data)
    return db_obj

@app.get("/{ticker}", response_model=list[OHLCV_Read])
async def get_ohlcv_endpoint(ticker: str, db=Depends(get_db)):
    records = await get_ohlcv(db, ticker)
    return records