import logging
from datetime import datetime

import pandas as pd

# Setup logging
logging.basicConfig(
    filename='alerts.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

def alert(anomalies: pd.DataFrame, ticker: str) -> None:
    """Log alerts and print to console."""
    if anomalies is None or anomalies.empty:
        print(f"[{datetime.now()}] ✅ {ticker}: No anomalies detected.")
        return
    
    message = f"🚨 ALERT: {ticker} - {len(anomalies)} anomalies detected!"
    print(message)
    logging.info(message)
    print(anomalies[['Price', 'SMA', 'Upper', 'Lower']].tail())