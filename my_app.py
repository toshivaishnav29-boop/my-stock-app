import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Nifty Live", layout="centered")
st.title("📈 Nifty 50 Live Tracker")
st.write("Raipur Diagnostic Lab Tech - Stock Monitor")

ticker = "^NSEI"
try:
    # 5 din ka data download kar rahe hain
    df = yf.download(ticker, period="5d", interval="15m")
    
    if not df.empty:
        # Latest price aur purani price nikalna
        current_price = float(df['Close'].iloc[-1])
        prev_price = float(df['Close'].iloc[-2])
        price_diff = current_price - prev_price
        
        # Dashboard par metrics dikhana
        col1, col2 = st.columns(2)
        col1.metric(label="Nifty 50 Price", value=f"₹{current_price:,.2f}", delta=f"{price_diff:.2f}")
        col2.metric(label="Market Status", value="Weekend")

        # Chart dikhana
        st.subheader("Market Trend (Last 5 Days)")
        st.line_chart(df['Close'])
        st.success("Data loaded successfully!")
    else:
        st.warning("Yahoo Finance se data nahi mil raha. Kal subah market khulte hi try karein.")

except Exception as e:
    st.error("Market data processing mein deri ho rahi hai. Please thodi der baad refresh karein.")
