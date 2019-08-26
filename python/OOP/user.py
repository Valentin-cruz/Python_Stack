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
        print(self.account_balance)

guido = user("Guido van Rossum", "guido@python.com")
monty = user("Monty Python", "monty@python.com")
bob = user("Bob Ross", "bob@python.com")


guido.make_deposit(100)
guido.make_deposit(200)
guido.make_deposit(100)
guido.make_withdrawal(100)
print(guido.account_balance)

monty.make_deposit(100)
monty.make_deposit(200)
monty.make_withdrawal(100)
monty.make_withdrawal(100)
print(monty.account_balance)

bob.make_deposit(100)
bob.make_withdrawal(100)
bob.make_withdrawal(100)
bob.make_withdrawal(100)
print(bob.account_balance)







# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150
# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance