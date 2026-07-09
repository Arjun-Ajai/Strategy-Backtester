import pandas as pd


def compute_metrics(trades,equity,initial_value):
    total_returns = ((trades[-1].portfolio_value - initial_value) / initial_value) * 100
    values = pd.Series([e.portfolio_value for e in equity])

    daily_returns = values.pct_change()
    sharpe = (daily_returns.mean() / daily_returns.std()) * (252 ** 0.5)

    return {"total_return_pct": total_returns,"sharpe": sharpe}





