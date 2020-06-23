import abc


class Command:
    """
    Parent object executing an abstract method
    """

    @abc.abstractmethod
    def execute(self) -> None:
        pass


class Invoker:
    """
        Class that execute any command you send through
    """

    def __init__(self, command):
        self.command = command

    def run(self):
        self.command.execute()


class Receiver:
    """
        This class will hold state
    """

    def __init__(self, *a, **kw):
        self.name = kw.get('name') if kw.get('name') else ''
        self.amount = kw.get('amount') if kw.get('amount') else 0

    def deposit(self, quantity):
        self.amount += quantity

    def balance(self):
        return self.amount

    def withdraw(self, quantity):
        if self.amount - quantity > 0:
            self.amount -= quantity


class Balance(Command):
    """
        Check amount on a bank account
    """

    def __init__(self, receiver: Receiver):
        self.receiver = receiver

    def execute(self) -> None:
        self.receiver.balance()


class Withdraw(Command):
    """
        Let the user withdraw some amount
    """

    def __init__(self, receiver, amount):
        self.receiver = receiver
        self.amount = amount

    def execute(self) -> None:
        self.receiver.withdraw(self.amount)


class Deposit(Command):
    """
        Let the user deposit an amount to it's account
    """

    def __init__(self, receiver, amount):
        self.receiver = receiver
        self.amount = amount

    def execute(self) -> None:
        self.receiver.deposit(self.amount)


if __name__ == '__main__':
    pass
