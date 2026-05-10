import streamlit as st
import yfinance as yf
import pandas as pd

st.title("Nifty 50 Tracker")

# Nifty ka data download karna
ticker = "^NSEI"
data = yf.download(ticker, period="1d", interval="1m")

if not data.empty:
    current_price = data['Close'].iloc[-1]
    st.metric(label="Nifty 50 Live Price", value=f"INR {current_price:,.2f}")
    st.line_chart(data['Close'])
else:
    st.write("Data load nahi ho raha hai, market hours check karein.")
