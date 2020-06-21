class BankMethods:

    def get_deposit(self, amount, quantity):
        amount += quantity
        return amount

    def get_balance(self, amount):
        return amount

    def get_withdraw(self, amount, quantity):

        if amount - quantity > 0:
            amount -= quantity
            return amount,True
        else:
            return amount,False
