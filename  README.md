# 🏦 Simple Banking System (Python)

A simple banking system that allows users to create accounts, deposit, withdraw, transfer money, and persist data to CSV files. Written in Python, with full unit test coverage.

## 🚀 Features

- Create a new bank account with name and starting balance
- Deposit money to existing accounts
- Withdraw money from accounts (no overdrafts allowed)
- Transfer funds between accounts
- Save and load account data from CSV
- Robust exception handling
- Unit tested with 100% coverage

## 📂 File Structure
├── bank.py          # Main business logic
├── test_bank.py     # Unit tests using unittest
├── README.md        # Project overview and instructions
├── accounts.csv     # Optional: stores saved accounts

## 🛠 Requirements

- Python 3.8 or above
- No third-party dependencies required (uses only standard library)

## ⚙️ How to Run

1. Clone the repository or download the code locally.
2. Run the test suite to verify all features:


```bash
python test_bank.py

You should see output like:

........
----------------------------------------------------------------------
Ran 8 tests in 0.000s

OK
```

## 📁 Example Usage

```python
from bank import BankSystem

bank = BankSystem()
bank.create_account("Alice", 1000)
bank.deposit("Alice", 500)
bank.withdraw("Alice", 300)
bank.create_account("Bob", 200)
bank.transfer("Alice", "Bob", 150)

bank.save_to_csv("accounts.csv")

# Load later
new_bank = BankSystem()
new_bank.load_from_csv("accounts.csv")
```

## 🧠 Design Notes
- Follows **KISS principle** (Keep It Simple, Stupid)
- Clear class separation (`BankAccount` vs `BankSystem`)
- Easily extendable to CLI or REST interface in the future

## 📬 Contact
Author: Blake Wang  
Email: blakewang_career@outlook.com
