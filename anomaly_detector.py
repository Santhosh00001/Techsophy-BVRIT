from typing import Optional
import pandas as pd
from config import WINDOW_SIZE, THRESHOLD
from lstm_model import train_lstm_model, predict_with_lstm

def detect_anomalies(data: pd.DataFrame, ticker: str, method: str = "statistical") -> Optional[pd.DataFrame]:
    """Hybrid anomaly detection (Statistical or LSTM)."""
    if data is None or data.empty:
        return None

    if method == "statistical":
        return _statistical_anomalies(data)
    elif method == "lstm":
        return _lstm_anomalies(data, ticker)
    else:
        raise ValueError("Invalid method. Choose 'statistical' or 'lstm'.")

def _statistical_anomalies(data: pd.DataFrame) -> pd.DataFrame:
    """Bollinger Bands (Original Method)."""
    data['SMA'] = data['Price'].rolling(window=WINDOW_SIZE).mean()
    data['STD'] = data['Price'].rolling(window=WINDOW_SIZE).std()
    data['Upper'] = data['SMA'] + (THRESHOLD * data['STD'])
    data['Lower'] = data['SMA'] - (THRESHOLD * data['STD'])
    return data[(data['Price'] > data['Upper']) | (data['Price'] < data['Lower'])]

def _lstm_anomalies(data: pd.DataFrame, ticker: str) -> pd.DataFrame:
    """LSTM-based anomaly detection."""
    model, scaler = train_lstm_model(data['Price'].to_frame(), window_size=WINDOW_SIZE)
    data['Predicted'] = data['Price'].rolling(window=WINDOW_SIZE).apply(
        lambda x: predict_with_lstm(model, scaler, x.to_frame(), WINDOW_SIZE)
    )
    data['Error'] = abs(data['Price'] - data['Predicted'])
    data['Threshold'] = data['Error'].rolling(window=WINDOW_SIZE).mean() + THRESHOLD * data['Error'].std()
    return data[data['Error'] > data['Threshold']]