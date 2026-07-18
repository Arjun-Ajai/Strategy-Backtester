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
    os.makedirs("results", exist_ok=True)
    plt.tight_layout()
    plt.savefig(f"results/run_{run_id}.png")
    plt.close()
