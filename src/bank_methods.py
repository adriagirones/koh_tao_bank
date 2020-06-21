class BankMethods:

    def get_deposit(self, amount, quantity):  # TODO: how is a deposit a get? It should set something so no return needed.
        amount += quantity
        return amount

    def get_balance(self, amount):
        return amount

    def get_withdraw(self, amount, quantity): # TODO: Same as deposit, this is an executing action so does not to return.

        if amount - quantity > 0:
            amount -= quantity
            return amount, True
        else:
            return amount, False
