import argparse
from data import fetch_historical_data
from database import to_database

ticker=input("Enter a ticker: ").upper()
start_date =input("Enter the start date: ")
end_date =input("Enter the end date: ")

df = fetch_historical_data(ticker, start_date, end_date)
to_database(df,ticker)