from sqlalchemy import Column, String, Float, Date
from src.database import base
import uuid
from datetime import datetime
from sqlalchemy.sql import func

class OHLCV(base):
    __tablename__ = "ohlcv_data"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    date = Column(datetime, server_default=func.now())
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Float)