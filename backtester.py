from dataclasses import dataclass
from strategy import *

@dataclass
class Trades:
    date: str
    action: str
    price: float
    shares: float
    cash: float
    portfolio_value: float

@dataclass
class EquityCurve:
    date: str
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
                        cash=0
                        trades.append(Trades(df.date.iloc[i],"BUY",df.next_open.iloc[i],shares,0,shares*df.next_open.iloc[i]))

                    elif signals[j].action == "SELL":
                        cash = shares * df.next_open[i]
                        shares=0
                        trades.append(Trades(df.date.iloc[i],"SELL",df.next_open.iloc[i],0,cash,cash))


            equity_curve.append(EquityCurve(df.date.iloc[i],cash+shares*df.close.iloc[i]))



        return {"trades": trades, "equity_curve": equity_curve, "final_value": cash}



