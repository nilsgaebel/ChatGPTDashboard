import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objs as go

# Set page title
st.set_page_config(page_title='Stock Market Overview')

# Define sidebar options
ticker = st.sidebar.text_input(
    'Enter Ticker Symbol', value='AAPL', max_chars=5)
start_date = st.sidebar.date_input(
    'Start Date', value=pd.to_datetime('2020-01-01'))
end_date = st.sidebar.date_input('End Date', value=pd.to_datetime('today'))

# Fetch data from Yahoo Finance
stock_data = yf.download(ticker, start=start_date, end=end_date)

# Create line chart for stock price over time
fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=stock_data.index,
               y=stock_data['Close'], name='Stock Price'))
fig1.update_layout(title='Stock Price',
                   xaxis_title='Date', yaxis_title='Price')

# Create line chart for volume over time
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=stock_data.index,
               y=stock_data['Volume'], name='Volume'))
fig2.update_layout(title='Volume', xaxis_title='Date', yaxis_title='Volume')


# Display charts in Streamlit app
st.plotly_chart(fig1)
st.plotly_chart(fig2)
