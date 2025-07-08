import yfinance as yf
import pandas as pd
from typing import Optional

def fetch_stock_data(ticker: str, period: str = "1d", interval: str = "1m") -> Optional[pd.DataFrame]:
    """Fetch stock data with error handling."""
    try:
        data = yf.download(tickers=ticker, period=period, interval=interval)
        return data
    except Exception as e:
        print(f"⚠️ Failed to fetch {ticker}: {e}")
        return None