import csv
from typing import Dict


class BankAccount:
    def __init__(self, name: str, balance: float):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.name = name
        self.balance = balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def transfer(self, target_account, amount: float):
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds for transfer.")
        self.withdraw(amount)
        target_account.deposit(amount)


class BankSystem:
    def __init__(self):
        self.accounts: Dict[str, BankAccount] = {}

    def create_account(self, name: str, balance: float):
        if name in self.accounts:
            raise ValueError("Account already exists.")
        self.accounts[name] = BankAccount(name, balance)

    def get_account(self, name: str) -> BankAccount:
        if name not in self.accounts:
            raise ValueError("Account not found.")
        return self.accounts[name]

    def deposit(self, name: str, amount: float):
        account = self.get_account(name)
        account.deposit(amount)

    def withdraw(self, name: str, amount: float):
        account = self.get_account(name)
        account.withdraw(amount)

    def transfer(self, from_name: str, to_name: str, amount: float):
        from_account = self.get_account(from_name)
        to_account = self.get_account(to_name)
        from_account.transfer(to_account, amount)

    def save_to_csv(self, filename: str):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Balance'])
            for account in self.accounts.values():
                writer.writerow([account.name, account.balance])

    def load_from_csv(self, filename: str):
        self.accounts.clear()
        try:
            with open(filename, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    name = row['Name']
                    balance = float(row['Balance'])
                    self.accounts[name] = BankAccount(name, balance)
        except FileNotFoundError:
            raise FileNotFoundError(f"{filename} not found.")