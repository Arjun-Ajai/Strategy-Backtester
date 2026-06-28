import argparse
from data import data
from database import to_database

def main():
    ticker =
    start_date =
    end_date =

    df = fetch_ohclv(ticker, start_date, end_date)
    to_database(df, ticker)
