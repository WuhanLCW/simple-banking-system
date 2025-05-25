import unittest
from bank import BankSystem


class TestBankSystem(unittest.TestCase):

    def setUp(self):
        self.bank = BankSystem()
        self.bank.create_account("Alice", 1000)
        self.bank.create_account("Bob", 500)

    def test_create_account_success(self):
        self.bank.create_account("Charlie", 300)
        account = self.bank.get_account("Charlie")
        self.assertEqual(account.balance, 300)

    def test_create_account_duplicate(self):
        with self.assertRaises(ValueError):
            self.bank.create_account("Alice", 100)

    def test_deposit(self):
        self.bank.deposit("Alice", 200)
        self.assertEqual(self.bank.get_account("Alice").balance, 1200)

    def test_withdraw_success(self):
        self.bank.withdraw("Bob", 100)
        self.assertEqual(self.bank.get_account("Bob").balance, 400)

    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.bank.withdraw("Bob", 1000)

    def test_transfer_success(self):
        self.bank.transfer("Alice", "Bob", 300)
        self.assertEqual(self.bank.get_account("Alice").balance, 700)
        self.assertEqual(self.bank.get_account("Bob").balance, 800)

    def test_transfer_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.bank.transfer("Bob", "Alice", 1000)

    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.bank.deposit("Alice", -100)

    def test_withdraw_negative_amount(self):
        with self.assertRaises(ValueError):
            self.bank.withdraw("Alice", -50)

    def test_transfer_negative_amount(self):
        with self.assertRaises(ValueError):
            self.bank.transfer("Alice", "Bob", -200)

    def test_access_nonexistent_account(self):
        with self.assertRaises(ValueError):
            self.bank.deposit("Charlie", 100)

    def test_save_and_load_csv(self):
        self.bank.save_to_csv("test_accounts.csv")
        # 模拟重新启动程序
        new_bank = BankSystem()
        new_bank.load_from_csv("test_accounts.csv")
        self.assertEqual(new_bank.get_account("Alice").balance, 1000)
        self.assertEqual(new_bank.get_account("Bob").balance, 500)


if __name__ == '__main__':
    unittest.main()