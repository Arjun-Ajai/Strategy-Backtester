
def compute_matrics(trades,equity,initial_value):
    total_returns = ((trades.portfolio_value.iloc[-1] - initial_value) / initial_value) * 100



