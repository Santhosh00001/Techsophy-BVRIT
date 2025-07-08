import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import LSTM, Dense # type: ignore
from sklearn.preprocessing import MinMaxScaler

def create_lstm_model(input_shape: tuple) -> Sequential:
    """Define LSTM model architecture."""
    model = Sequential([
        LSTM(50, return_sequences=True, input_shape=input_shape),
        LSTM(50),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse')
    return model

def train_lstm_model(data: pd.DataFrame, window_size: int = 20) -> Sequential:
    """Train LSTM on historical data."""
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(data.values.reshape(-1, 1))

    X, y = [], []
    for i in range(window_size, len(scaled_data)):
        X.append(scaled_data[i-window_size:i, 0])
        y.append(scaled_data[i, 0])
    X, y = np.array(X), np.array(y)
    X = np.reshape(X, (X.shape[0], X.shape[1], 1))

    model = create_lstm_model((window_size, 1))
    model.fit(X, y, epochs=10, batch_size=32, verbose=0)
    return model, scaler

def predict_with_lstm(model: Sequential, scaler: MinMaxScaler, data: pd.DataFrame, window_size: int) -> np.ndarray:
    """Predict next value using LSTM."""
    last_window = scaler.transform(data[-window_size:].values.reshape(-1, 1))
    last_window = np.reshape(last_window, (1, window_size, 1))
    predicted = model.predict(last_window)
    return scaler.inverse_transform(predicted)[0][0]