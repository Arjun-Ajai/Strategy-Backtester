import pandas as pd


def compute_metrics(trades,equity,initial_value):
    total_returns = ((trades[-1].portfolio_value - initial_value) / initial_value) * 100
    values = pd.Series([e.portfolio_value for e in equity])

    daily_returns = values.pct_change()
    sharpe = (daily_returns.mean() / daily_returns.std()) * (252 ** 0.5)

    peaks=values.cummax()
    drawdown=(values-peaks)/peaks*100
    max_drawdown_pct = min(drawdown)

    win=0
    buy_price=None
    num_trades = 0
    for t in trades:
        if t.action == 'BUY':
            buy_price=t.price
        elif t.action == 'SELL' and buy_price is not None:
            num_trades+=1
            if buy_price<t.price:
                win+=1
    win_rate=win/num_trades*100
    return {"total_return_pct": total_returns,"sharpe": sharpe,"max_drawdown_pct":max_drawdown_pct,"win_rate":win_rate,"num_trades":num_trades}





