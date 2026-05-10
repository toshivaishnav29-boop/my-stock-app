import streamlit as st
import yfinance as df
import pandas as pd

st.title("Nifty 50 Tracker")
st.write("Live Data from Yahoo Finance")

ticker = "^NSEI"
data = df.download(ticker, period="1d", interval="1m")

if not data.empty:
    current_price = data['Close'].iloc[-1]
    st.metric(label="Nifty 50", value=f"{current_price:,.2f}")
    st.line_chart(data['Close'])
else:
    st.write("Data loading... please wait.")
