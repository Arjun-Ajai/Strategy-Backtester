from dataclasses import dataclass
from strategy import Signal, BaseStrategy, SmaCrossStrategy
import pandas as pd

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
        signals_map={}
        for s in signals:
            signals_map[s.date]=s
        for i in range(len(df)):
            if df.date.iloc[i] in signals_map:
                    if pd.isna(df.next_open.iloc[i]):
                        continue
                    if signals_map[df.date.iloc[i]].action == "BUY":
                        shares = cash / df.next_open.iloc[i]
                        cash=0
                        trades.append(Trades(df.date.iloc[i],"BUY",df.next_open.iloc[i],shares,0,shares*df.next_open.iloc[i]))

                    elif signals_map[df.date.iloc[i]].action == "SELL":
                        cash = shares * df.next_open.iloc[i]
                        shares=0
                        trades.append(Trades(df.date.iloc[i],"SELL",df.next_open.iloc[i],0,cash,cash))


            equity_curve.append(EquityCurve(df.date.iloc[i],cash+shares*df.close.iloc[i]))



        return {"trades": trades, "equity_curve": equity_curve, "final_value": cash}



