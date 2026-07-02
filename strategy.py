from indicator import *
from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class Signal:
    date: str
    action: str
    price: float
    reason: str


class BaseStrategy(ABC):
    @abstractmethod
    def generate_signals(self,df):
        ...

    @property
    @abstractmethod
    def name(self):
        ...


    @property
    @abstractmethod
    def params(self):
        ...

class SmaCrossStrategy(BaseStrategy):
    def generate_signals(self, df):
        signals = []
        in_position = False
        fast = sma(df.close, 10)
        slow = sma(df.close, 50)

        for i in range(1,len(df)):
            if fast.iloc[i] > slow.iloc[i] and fast.iloc[i - 1] < slow.iloc[i - 1] and not in_position:
                in_position = True
                signals.append(Signal(df.date.iloc[i - 1], "BUY", df.close.iloc[i - 1], "fast crossed above slow"))
            elif fast.iloc[i] < slow.iloc[i] and fast.iloc[i - 1] > slow.iloc[i - 1] and in_position:
                in_position = False
                signals.append(Signal(df.date.iloc[i - 1], "SELL", df.close.iloc[i - 1], "fast crossed below slow"))
        return signals

    @property
    def name(self):
        return "Sma Cross Strategy"

    @property
    def params(self):
        return {"fast" : 10 , "slow" : 50}

class RsiStrategy(BaseStrategy):
    def generate_signals(self, df):
        signals = []
        in_position = False
        rsi_values = rsi(df.close, 14)
        oversold, overbought = 30, 70

        for i in range(1, len(df)):
            if rsi_values.iloc[i] < oversold and not in_position:
                in_position = True
                signals.append(Signal(df.date.iloc[i], "BUY", df.close.iloc[i], f"RSI below {oversold}"))
            elif rsi_values.iloc[i] > overbought and in_position:
                in_position = False
                signals.append(Signal(df.date.iloc[i], "SELL", df.close.iloc[i], f"RSI above {overbought}"))

        return signals

    @property
    def name(self):
        return "RSI Strategy"

    @property
    def params(self):
        return {"period": 14, "oversold": 30, "overbought": 70}