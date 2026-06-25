import yfinance as yf
import pandas as pd
def fetch_ohlcv(ticker, start, end):
    df = yf.download(ticker,start,end,progress=False,auto_adjust=True)
    df=df.reset_index()
    df.columns=df.columns.str.lower()
    return df