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




