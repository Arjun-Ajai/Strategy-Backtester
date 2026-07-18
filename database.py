import sqlite3

class Database:
    def __init__(self, path):
        self.conn = sqlite3.connect(path)
        self._init_schema()

    def _init_schema(self):
        self.conn.execute("""CREATE TABLE IF NOT EXISTS trades (
        id              INTEGER PRIMARY KEY AUTOINCREMENT,
        run_id          INTEGER,
        date            TEXT,
        action          TEXT,
        price           REAL,
        quantity        REAL,
        portfolio_value REAL)""")

        self.conn.execute("""CREATE TABLE IF NOT EXISTS equity_curve(
        id           INTEGER PRIMARY KEY AUTOINCREMENT,
        run_id       INTEGER,
        date         TEXT,
        portfolio_value REAL)""")

        self.conn.execute("""CREATE TABLE IF NOT EXISTS runs(
        id integer primary key autoincrement, 
        symbol   text, 
        strategy text, 
        params   text, 
        start_date date, 
        end_date   date, 
        total_return float, 
        sharpe       float, 
        max_drawdown float, 
        win_rate     float, 
        num_trades   real, 
        created_at   datetime )
        """)
        self.conn.commit()

    def save_runs(self, symbol, strategy, params, start_date, end_date,
                  total_return, sharpe, max_drawdown, win_rate, num_trades):
        cursor = self.conn.execute("""INSERT INTO runs (symbol, strategy, params, start_date, end_date,
        total_return, sharpe, max_drawdown, win_rate, num_trades) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (symbol, strategy, params, start_date, end_date, total_return, sharpe, max_drawdown, win_rate, num_trades))
        self.conn.commit()
        return cursor.lastrowid

    def save_trades(self, run_id, date, action, price, quantity, portfolio_value):
        cursor = self.conn.execute(
            "INSERT INTO trades (run_id, date, action, price, quantity, portfolio_value) VALUES (?, ?, ?, ?, ?, ?)",
            (run_id, date, action, price, quantity, portfolio_value)
        )
        self.conn.commit()

    def save_equity(self,run_id,date,portfolio_value):
        cursor = self.conn.execute("INSERT INTO equity_curve(run_id, date, portfolio_value) VALUES (?, ?, ?)",(run_id,date,portfolio_value))
        self.conn.commit()

    def get_all_runs(self):
        cursor = self.conn.execute("SELECT * FROM runs ORDER BY sharpe DESC")
        return cursor.fetchall()
    def get_all_trades(self,run_id):
        cursor=self.conn.execute("SELECT * FROM trades WHERE run_id=?",(run_id,))
        return cursor.fetchall()
    def get_all_equity(self,run_id):
        cursor = self.conn.execute("SELECT * FROM equity_curve WHERE run_id=?",(run_id,))
        return cursor.fetchall()