from bank_methods import BankMethods


class UserBank:

    def __init__(self, name):
        self.amount = 0
        self.name = name

    def deposit(self, quantity):
        self.amount = BankMethods.set_amount(self, self.amount, quantity)

    def balance(self):
        return self.amount

    def withdraw(self, quantity):
        self.amount, withdraw_done = BankMethods.get_withdraw(self, self.amount, quantity)
        return withdraw_done


if __name__ == '__main__':
    adria = UserBank('adria')
    print(adria.balance())
    adria.deposit(50)
    print(adria.balance())
    print(adria.withdraw(45))
    print(adria.balance())
    print(adria.withdraw(100))
    print(adria.balance())
