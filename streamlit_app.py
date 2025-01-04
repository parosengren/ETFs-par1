import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# List of ETF tickers
etf_tickers = [
    "JAAA", "JMBS", "VNLA", "JBBB", 
    "JSMD", "JSI", "JSML", "JEMB", 
    "JLQD", "JRE", "SSPX", "SXUS"
]

# Streamlit app
st.title("ETF Data Viewer with Accurate Close Prices")

# Automatically set the date range for the past year
end_date = datetime.today()
start_date = end_date - timedelta(days=365)

# Fetch data
st.write("Fetching Close Prices for the past year...")
etf_data = {}
for ticker in etf_t
