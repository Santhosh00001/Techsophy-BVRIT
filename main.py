import time
from config import TICKERS, INTERVAL_SECONDS
from api_client import fetch_stock_data
from data_processing import preprocess_data
from anomaly_detector import detect_anomalies
from alert_system import alert

METHOD = "lstm"  # Choose "statistical" or "lstm"

def run_monitor():
    print(f"📈 Starting Anomaly Detector (Method: {METHOD})...")
    while True:
        for ticker in TICKERS:
            raw_data = fetch_stock_data(ticker)
            processed_data = preprocess_data(raw_data)
            anomalies = detect_anomalies(processed_data, ticker, method=METHOD)
            alert(anomalies, ticker)
        time.sleep(INTERVAL_SECONDS)

if __name__ == "__main__":
    run_monitor()