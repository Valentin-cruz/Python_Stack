class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self):	
        self.account.deposit()
        print(self.account.balance)

    def make_withdrawal(self, amount):
        self.account.withdrawal()
        print(self.account.balance)

    def display_user_balance(self):
        self.account.display_account_info()
        print(self.account.balance)