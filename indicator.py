
def sma(series,window):
    return series.rolling(window).mean()
def ema(series,span):
    return series.ewm(span=span).mean()
def rsi(series,period):
    delta =series.diff()
    gain = delta.clip(lower=0).rolling(period).mean()
    loss = (-delta).clip(lower=0).rolling(period).mean()
    rsi_val= 100-(100/((gain/loss)+1))
    return rsi_val
