# 📈 Real-time Stock Price Anomaly Detector

A Python application that monitors real-time stock prices and alerts when unusual price movements are detected. This project demonstrates modular design, time series analysis, and anomaly detection using real stock market data from Alpha Vantage.

---

## 🔧 Features

- ✅ Real-time stock price fetching using Alpha Vantage API
- 📊 Moving average and standard deviation-based anomaly detection
- 🔔 Console alerts for sudden or unusual stock price movements
- 📁 Modular structure: API client, data processing, anomaly detection, and alert system
- 🔄 Configurable polling interval and detection sensitivity

---

## 📁 Project Structure

stock-anomaly-detector/
├── api_client.py # Fetches stock data from Alpha Vantage
├── data_processing.py # Processes and cleans the time series data
├── anomaly_detector.py # Detects anomalies based on statistical thresholds
├── alert_system.py # Prints alerts to the console (can be extended to email, SMS)
├── config.py # Configuration variables (keep API key private!)
├── main.py # Entry point: orchestrates the detection pipeline
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## ⚙️ How It Works

1. **Fetches stock prices** using the Alpha Vantage API at regular intervals (e.g., every minute).
2. **Calculates a moving average** and standard deviation over a sliding window.
3. **Flags anomalies** when price deviates significantly beyond a threshold.
4. **Triggers an alert** with a snapshot of suspicious price activity.

---

## 🧠 Anomaly Detection Logic

If current_price > mean + (threshold × std_dev) 
or current_price < mean - (threshold × std_dev),
→ Then it's flagged as an anomaly.
You can control sensitivity using WINDOW_SIZE and THRESHOLD in config.py.

🚀 Getting Started
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/YOUR_USERNAME/stock-anomaly-detector.git
cd stock-anomaly-detector
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Add your Alpha Vantage API key
Edit config.py and add your key:

python
Copy
Edit
ALPHA_VANTAGE_API_KEY = "YOUR_API_KEY_HERE"
🔐 Do not commit your API key to public repos!

4. Run the app
bash
Copy
Edit
python main.py
🛠 Configuration
In config.py:

python
Copy
Edit
TICKERS = ["AAPL", "TSLA", "GOOGL"]  # Stocks to monitor
INTERVAL_SECONDS = 60               # Polling frequency in seconds

WINDOW_SIZE = 10  # Moving average window
THRESHOLD = 2     # Std dev multiplier
📦 Requirements
Generated using pip freeze > requirements.txt:

pandas

requests

datetime

time

Install with:

bash
Copy
Edit
pip install -r requirements.txt
📈 Sample Output
yaml
Copy
Edit
⏳ Checking stock prices...

🚨 ALERT for AAPL! Unusual price movement detected:
Datetime                 Price
2025-07-08 09:01:00      210.45
2025-07-08 09:02:00      213.10
...
📌 Notes
Free Alpha Vantage keys allow 25 requests per day. Consider upgrading for more usage or caching responses during development.

You can replace Alpha Vantage with another API easily by modifying api_client.py.

🙋‍♂️ Author
Vemula Santhosh
📧 santhoshvemulat12@gmail.com
🔗 GitHub

📄 License
This project is licensed under the MIT License.

yaml
Copy
Edit

---

### ✅ How to Use It

1. Copy this into a new file in your project folder: `README.md`
2. Replace `YOUR_USERNAME` in the GitHub link if needed
3. Commit & push:

```bash
git add README.md
git commit -m "Add README.md with project documentation"
git push
