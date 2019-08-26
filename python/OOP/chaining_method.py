class user:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        self.account_balance
        print(guido.account_balance)

guido = user("Guido van Rossum", "guido@python.com")
monty = user("Monty Python", "monty@python.com")
bob = user("Bob Ross", "bob@python.com")


guido.make_deposit(100).make_deposit(200).make_deposit(100).make_withdrawal(100).display_user_balance()

monty.make_deposit(100).make_deposit(200).make_withdrawal(100).make_withdrawal(100).display_user_balance()

bob.make_deposit(100).make_withdrawal(100).make_withdrawal(100).make_withdrawal(100).display_user_balance()