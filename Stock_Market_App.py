import streamlit as st
import yfinance as yf
import datetime
import pandas as pd
import numpy as np

ticker_symbol = st.text_input("Enter the stock name", "AAPL")
col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("Start Date", datetime.date(2019, 7, 6))
with col2:
    end_date = st.date_input("End Date", datetime.date(2024, 12, 18))

data = yf.download(tickers=ticker_symbol, start=start_date, end=end_date)

stock = yf.Ticker(ticker_symbol)

name = stock.info['longName']

st.header(name)
st.write(data)

st.line_chart(data['Close'])
st.bar_chart(data['Volume'])