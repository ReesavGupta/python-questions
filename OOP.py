import string
import random

class Account:
    bank_name = "Default Bank"
    total_accounts = 0
    minimum_balance = 0

    def __init__(self, account_id, name, balance):
        if not name or balance < 0:
            raise ValueError("Invalid account details")
        self.account_id = account_id
        self.name = name
        self._balance = balance
        Account.total_accounts += 1

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            return True
        return False

    def get_balance(self):
        return self._balance

    def __str__(self):
        return f"{self.name} (ID: {self.account_id}) Balance: ${self._balance}"

    @classmethod
    def set_bank_name(cls, name):
        cls.bank_name = name

    @classmethod
    def set_minimum_balance(cls, amount):
        cls.minimum_balance = amount

    @classmethod
    def get_total_accounts(cls):
        return cls.total_accounts


class SavingsAccount(Account):
    def __init__(self, account_id, name, balance, interest_rate):
        super().__init__(account_id, name, balance)
        self.interest_rate = interest_rate

    def calculate_monthly_interest(self):
        return round(self._balance * self.interest_rate / 100 / 12, 2)


class CheckingAccount(Account):
    def __init__(self, account_id, name, balance, overdraft_limit):
        super().__init__(account_id, name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self._balance + self.overdraft_limit:
            self._balance -= amount
            return True
        return False


# ========== TEST CASES ========== #

savings_account = SavingsAccount("SA001", "Alice Johnson", 1000, 2.5)
checking_account = CheckingAccount("CA001", "Bob Smith", 500, 200)

print(f"Savings Account: {savings_account}")
print(f"Checking Account: {checking_account}")

print(f"Savings balance before: ${savings_account.get_balance()}")
savings_account.deposit(500)
print(f"After depositing $500: ${savings_account.get_balance()}")

withdrawal_result = savings_account.withdraw(200)
print(f"Withdrawal result: {withdrawal_result}")
print(f"Balance after withdrawal: ${savings_account.get_balance()}")

print(f"Checking balance: ${checking_account.get_balance()}")
overdraft_result = checking_account.withdraw(600)  # Should use overdraft
print(f"Overdraft withdrawal: {overdraft_result}")
print(f"Balance after overdraft: ${checking_account.get_balance()}")

interest_earned = savings_account.calculate_monthly_interest()
print(f"Monthly interest earned: ${interest_earned}")

print(f"Total accounts created: {Account.get_total_accounts()}")
print(f"Bank name: {Account.bank_name}")

Account.set_bank_name("New National Bank")
Account.set_minimum_balance(100)

try:
    invalid_account = SavingsAccount("SA002", "", -100, 1.5)  # Should raise error
except ValueError as e:
    print(f"Validation error: {e}")
