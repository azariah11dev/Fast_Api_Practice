import yfinance as yf

async def fetch_ohlcv(ticker: str):
    data = yf.download(ticker, period="1mo", interval="1d")
    if data.empty:
        raise ValueError(f"No data found for ticker: {ticker}")
    row = data.iloc[0]
    stock = yf.Ticker(ticker)
    return {
        "ticker": ticker.upper(),
        "date": row.name.strftime("%Y-%m-%d"),
        "open": float(row["Open"]),
        "high": float(row["High"]),
        "low": float(row["Low"]),
        "close": float(row["Close"]),
        "volume": float(row["Volume"])
    }