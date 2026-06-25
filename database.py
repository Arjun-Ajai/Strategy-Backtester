import pandas as pd
import sqlite3

def to_database(df,database_name : str):
    conn =sqlite3.connect(database_name+".db")
    df.to_sql(database_name,conn,if_exists='replace')
    conn.close()