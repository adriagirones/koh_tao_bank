from bank_methods import BankMethods

# TODO: Move this to the bank.py file and delete user.py

class UserBank:

    def __init__(self, name):
        self.amount = 0
        self.name = name

    def deposit(self, quantity):
        self.amount = BankMethods.get_deposit(self, self.amount, quantity)

    def balance(self):
        self.amount = BankMethods.get_balance(self, self.amount)
        return self.amount

    def withdraw(self, quantity):
        self.amount, withdraw_done = BankMethods.get_withdraw(self, self.amount, quantity)
        return withdraw_done
