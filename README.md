# Strategy Backtester

Tests rule based trading strategies on historical OHLCV data.
Simulates realistic trade execution, computes performance metrics,
and stores every run for comparison.

## Install

pip install -r requirements.txt

## Strategies

**SMA Crossover**
BUY when fast SMA crosses above slow SMA (bullish momentum).
SELL when fast SMA crosses below slow SMA.
Parameters: `--fast` (default 20), `--slow` (default 50)

**RSI Mean Reversion**
BUY when RSI drops below oversold threshold (asset beaten down, likely to recover).
SELL when RSI rises above overbought threshold (asset overextended, likely to pull back).
Parameters: `--oversold` (default 30), `--overbought` (default 70)
