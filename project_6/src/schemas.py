from pydantic import BaseModel
from datetime import date

class OHLCV_Base(BaseModel):
    ticker: str
    date: date
    open: float
    high: float
    low: float
    close: float
    volume: float

class OHLCV_Create(OHLCV_Base):
    pass

class OHLCV_Read(OHLCV_Base):
    class Config:
        orm_mode = True