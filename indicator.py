
def sma(series,window):
    return series.rolling(window).mean()
def ema(series,span):
    return series.ewm(span=span).mean()
