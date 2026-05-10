import streamlit as st
import yfinance as yf
import pandas as pd

# Page setting (Isse app mobile par acchi dikhegi)
st.set_page_config(page_title="Nifty Live", layout="centered")

st.title("📈 Nifty 50 Live Tracker")
st.write("Raipur Diagnostic Lab Tech - Stock Monitor")

# Nifty data download (5 days taaki weekend par bhi dikhe)
ticker = "^NSEI"
try:
    data = yf.download(ticker, period="5d", interval="15m")

    if not data.empty:
        # Latest Price nikalna
        current_price = data['Close'].iloc[-1]
        prev_close = data['Close'].iloc[-2]
        change = current_price - prev_close
        
        # Dashboard Cards
        col1, col2 = st.columns(2)
        col1.metric(label="Nifty 50 Price", value=f"₹{current_price:,.2f}", delta=f"{change:.2f}")
        col2.metric(label="Market Status", value="Weekend (Closed)")

        # Chart dikhana
        st.subheader("Market Trend (Last 5 Days)")
        st.line_chart(data['Close'])
        
        st.success("Data successfully loaded!")
    else:
        st.warning("Yahoo Finance se data nahi mil raha. Thodi der baad try karein.")

except Exception as e:
    st.error(f"Error: {e}")

st.info("Tip: Ye app har 15 minute mein update hoti hai.")
