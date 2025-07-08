# dashboard.py
import streamlit as st
import pandas as pd
import time
from datetime import datetime
import streamlit as st
import pandas as pd
import time
from datetime import datetime
import plotly.graph_objects as go
from config import TICKERS, WINDOW_SIZE, THRESHOLD
from main import run_monitor  # Import your existing monitoring function
import threading

# Set up the page
st.set_page_config(page_title="Stock Anomaly Dashboard", layout="wide")
st.title("📊 Real-time Stock Price Anomaly Detector")

# Sidebar for configuration
with st.sidebar:
    st.header("Configuration")
    selected_tickers = st.multiselect(
        "Select stocks to monitor", 
        TICKERS, 
        default=TICKERS
    )
    detection_method = st.radio(
        "Detection Method",
        ("statistical", "lstm"),
        index=1
    )
    window_size = st.slider(
        "Window Size", 
        min_value=5, 
        max_value=30, 
        value=int(WINDOW_SIZE)  # Ensure value is integer
    )
    threshold = st.slider(
        "Threshold (σ)", 
        min_value=1.0, 
        max_value=3.0, 
        value=float(THRESHOLD),  # Ensure value is float
        step=0.1
    )
    
    if st.button("Update Configuration"):
        # Update config - in a real app you'd persist these
        TICKERS[:] = selected_tickers
        WINDOW_SIZE = window_size
        THRESHOLD = threshold

# Placeholder for anomaly logs
anomaly_logs = pd.DataFrame(columns=["timestamp", "ticker", "message"])

# Display tabs
tab1, tab2, tab3 = st.tabs(["Live View", "Anomaly Log", "Historical Data"])

# Start the monitoring system in a background thread
if 'monitor_thread' not in st.session_state:
    st.session_state.monitor_thread = threading.Thread(
        target=run_monitor,
        daemon=True
    )
    st.session_state.monitor_thread.start()

# Live View Tab
with tab1:
    st.subheader("Live Stock Monitoring")
    
    # Placeholder for live charts
    chart_placeholders = {ticker: st.empty() for ticker in TICKERS}
    
    # Simulate updating charts (in a real app, this would connect to your actual data)
    for ticker in TICKERS:
        with chart_placeholders[ticker]:
            st.write(f"### {ticker}")
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=[1, 2, 3, 4, 5],
                y=[100, 101, 102, 103, 104],
                name="Price"
            ))
            fig.add_trace(go.Scatter(
                x=[1, 2, 3, 4, 5],
                y=[99, 100, 101, 102, 103],
                name="SMA",
                line=dict(dash='dash')
            ))
            fig.update_layout(height=300)
            st.plotly_chart(fig, use_container_width=True)

# Anomaly Log Tab
with tab2:
    st.subheader("Recent Anomalies")
    
    # Display anomaly log table
    st.dataframe(
        anomaly_logs.sort_values("timestamp", ascending=False),
        hide_index=True,
        use_container_width=True
    )

# Historical Data Tab
with tab3:
    st.subheader("Historical Analysis")
    selected_history_ticker = st.selectbox(
        "Select stock", 
        TICKERS,
        key="history_ticker"
    )
    
    # Placeholder for historical analysis
    st.write(f"Historical data analysis for {selected_history_ticker} would appear here")

# Add to requirements.txt
st.info("Add `streamlit` and `plotly` to your requirements.txt to run this dashboard")