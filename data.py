import yfinance as yf
import pandas as pd
def fetch_historical_data(tickers,start,end):
    return yf.download(tickers,start,end)



