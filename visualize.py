import matplotlib.pyplot as plt
import pandas as pd
import os

def plot_results(df_ohlcv, equity, trades, run_id, symbol):

    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(14, 10))
    x_values = df_ohlcv.date.tolist()
    y_values = df_ohlcv.close.tolist()
    ax1.plot(x_values, y_values, color='black', label='price')
    ax1.set_title('Price Chart')
    ax1.set_ylabel('Price($)')
    ax1.legend()
    buy_dates=[trades.date for trades in trades if trades.action == 'BUY']
    buy_prices=[trades.price for trades in trades if trades.action == 'BUY']
    sell_dates=[trades.date for trades in trades if trades.action == 'SELL']
    sell_prices=[trades.price for trades in trades if trades.action == 'SELL']
    ax1.scatter(buy_dates,buy_prices,marker='^',color='blue',label='BUY')
    ax1.scatter(sell_dates,sell_prices,marker='v',color='red',label='SELl')
    os.makedirs("results", exist_ok=True)
    plt.tight_layout()
    plt.savefig(f"results/run_{run_id}.png")
    plt.close()

    equity_dates=[equity.date for equity in equity ]
    equity_values=[equity.price for equity in equity]
    initial_shares = 100_000 / df_ohlcv.close.iloc[0]
    benchmark = (df_ohlcv.close * initial_shares).tolist()
    ax2.plot(equity_dates, equity_values, color='blue', label='Strategy')
    ax2.plot(x_values, benchmark, color='orange', label='Buy & Hold')
    ax2.set_title('Portfolio vs Buy & Hold')
    ax2.set_ylabel('Value ($)')
    ax2.legend()



