from dataclasses import dataclass
from strategy import *

@dataclass
class Trades:
    cash: float
    shares: int

@dataclass
class EquityCurve:
    date: str
    equity: float
    portfolio_value: float

class Backtester:
    def run(self,df,signals):
        df["next_open"] = df.open.shift(-1)
        trades = []
        equity_curve =[]
        cash=100000
        shares=0
        for i in range(len(df)):
            for j in range(len(signals)):
                if signals[j].date == df.date[i]:
                    if signals[j].action == "BUY":
                        shares = cash / df.next_open[i]
                        trades.append(Trades(0, shares))
                        shares = 0
                    elif signals[j].action == "SELL":
                        cash = shares * df.next_open[i]
                        trades.append(Trades(cash, 0))
                        cash =0

            equity_curve.append(EquityCurve(df.date[i],trades[i].cash+trades[i].shares*df.close[i],trades[i].cash))


        return {"trades": trades, "equity_curve": equity_curve, "final_value": cash}



