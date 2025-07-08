from typing import Optional
import pandas as pd

def preprocess_data(raw_data: pd.DataFrame, max_price_change: float = 0.1) -> Optional[pd.DataFrame]:
    """Clean data and validate price movements."""
    if raw_data is None or raw_data.empty:
        return None
    
    processed = raw_data.copy()
    processed = processed.dropna()
    
    # Check for extreme price jumps (likely bad data)
    price_changes = processed['Close'].pct_change().abs()
    if (price_changes > max_price_change).any():
        print("⚠️ Extreme price jump detected. Dropping outliers.")
        processed = processed[price_changes <= max_price_change]
    
    processed['Price'] = processed['Close']
    return processed[['Price']]