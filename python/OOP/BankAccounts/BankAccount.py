class BankAccount:
    def __init__(self, int_rate, balance): 
        self.account_balance = 0
        self.int_rate = 0.01

    def deposit(self, amount):
        self.account_balance += amount
    def withdraw(self, amount):
        self.account_balance -= amount
    def display_account_info(self):
        self.account_balance
        print(self.account_balance)
    def yield_interest(self):
        self.account_balance = 0.01 * self.account_balance

account1 = BankAccount(0,0)
account2 = BankAccount(0,0)

account1.deposit(100).deposit(100).deposit(100).withdraw(100).yield_interest().display_account_info()
account2.deposit(100).deposit(100).withdraw(50).withdraw(50).withdraw(50).withdraw(50).yield_interest().display_account_info()