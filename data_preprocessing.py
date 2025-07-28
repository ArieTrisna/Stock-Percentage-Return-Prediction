# Importing Dependencies
import yfinance as yf
import pandas as pd
import numpy as np

# Setting Up Ticker and Data Pull
ticker_symbol = 'BBCA.JK'
ticker = yf.Ticker(ticker_symbol)
stock_data = ticker.history(period='5y')

# Delete Unrelated Columns
df = stock_data.copy()
df.drop(columns=['Dividends', 'Stock Splits'], inplace=True)

# Check for Duplicated Rows
duplicates = len(df.drop_duplicates()) / len(df)
if duplicates > 1:
    df = df.drop_duplicates()

# Transform the datetime format
df = df.reset_index()
df['Date'] = pd.to_datetime(df['Date']).dt.date
df = df.set_index('Date')

def dataframe():
    return df
