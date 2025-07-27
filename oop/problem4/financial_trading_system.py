import random

# ===== Base Classes =====

class Account:
    def __init__(self, account_id, trader_name, balance):
        self.account_id = account_id
        self.trader_name = trader_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

class RiskManagement:
    def assess_portfolio_risk(self):
        return random.choice(["Low", "Medium", "High"])

    def calculate_position_size(self, balance, symbol, price):
        position_size = int(balance * 0.02 / price)
        return position_size

class AnalyticsEngine:
    def analyze_market_trend(self, symbol):
        return {"symbol": symbol, "trend": random.choice(["up", "down", "sideways"]), "confidence": random.uniform(0.5, 1.0)}

class NotificationSystem:
    def set_price_alert(self, symbol, target_price, direction):
        self.alerts = getattr(self, "alerts", [])
        self.alerts.append((symbol, target_price, direction))
        return True

    def get_pending_notifications(self):
        return [f"Alert for {s} at {p} ({d})" for s, p, d in getattr(self, "alerts", [])]

# ===== Trader Types =====

class StockTrader(Account, RiskManagement, AnalyticsEngine):
    def __init__(self, account_id, trader_name, balance):
        super().__init__(account_id, trader_name, balance)
        self.portfolio = []

class CryptoTrader(Account, NotificationSystem):
    def __init__(self, account_id, trader_name, balance):
        super().__init__(account_id, trader_name, balance)
        self.wallet = []

# ===== ProfessionalTrader with Multiple Inheritance =====

class ProfessionalTrader(StockTrader, CryptoTrader):
    def __init__(self, account_id, trader_name, balance):
        StockTrader.__init__(self, account_id, trader_name, balance)
        CryptoTrader.__init__(self, account_id, trader_name, balance)

    def execute_diversified_strategy(self, strategy):
        self.portfolio = strategy.get("stocks", [])
        self.wallet = strategy.get("crypto", [])
        return {
            "status": "executed",
            "positions": self.portfolio + self.wallet,
            "allocation": strategy.get("allocation", {})
        }

# ===== Pytest-Compatible Test Functions =====

def test_mro_and_inheritance():
    pro_trader = ProfessionalTrader("PT001", "Mike Johnson", 100000.0)
    mro_names = [cls.__name__ for cls in ProfessionalTrader.__mro__]
    assert "ProfessionalTrader" in mro_names
    assert "StockTrader" in mro_names
    assert "CryptoTrader" in mro_names

def test_account_management():
    stock_trader = StockTrader("ST001", "John Doe", 50000.0)
    assert stock_trader.account_id == "ST001"
    assert stock_trader.balance == 50000.0

    assert stock_trader.deposit(10000) is True
    assert stock_trader.balance == 60000.0

    assert stock_trader.withdraw(5000) is True
    assert stock_trader.balance == 55000.0

def test_risk_management():
    stock_trader = StockTrader("ST002", "Risk Guy", 30000.0)
    risk_level = stock_trader.assess_portfolio_risk()
    assert risk_level in ["Low", "Medium", "High"]

    pos_size = stock_trader.calculate_position_size(stock_trader.balance, "AAPL", 150.0)
    assert isinstance(pos_size, int)
    assert pos_size > 0

def test_analytics():
    stock_trader = StockTrader("ST003", "Analytics Person", 40000.0)
    trend = stock_trader.analyze_market_trend("AAPL")
    assert isinstance(trend, dict)
    assert "trend" in trend
    assert "confidence" in trend

def test_notification_system():
    crypto_trader = CryptoTrader("CT001", "Jane Smith", 25000.0)
    assert crypto_trader.set_price_alert("BTC", 45000, "above") is True
    notes = crypto_trader.get_pending_notifications()
    assert isinstance(notes, list)
    assert "BTC" in notes[0]

def test_professional_trader_combination():
    pro_trader = ProfessionalTrader("PT001", "Mike Johnson", 100000.0)
    assert hasattr(pro_trader, 'assess_portfolio_risk')
    assert hasattr(pro_trader, 'analyze_market_trend')
    assert hasattr(pro_trader, 'set_price_alert')

    strategy = {
        "stocks": ["AAPL", "GOOGL"],
        "crypto": ["BTC", "ETH"],
        "allocation": {"stocks": 0.7, "crypto": 0.3}
    }
    result = pro_trader.execute_diversified_strategy(strategy)
    assert result["status"] == "executed"
    assert len(result["positions"]) > 0
