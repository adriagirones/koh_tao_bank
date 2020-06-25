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

    :param
    command: Command
    """

    def __init__(self, command: Command):
        self.command = command

    def run(self) -> None:
        self.command.execute()


class Receiver:
    """
    This class will hold state

    :param
    name: str
    amount: float
    """

    def __init__(self, *args, **kwargs):
        self.name = kwargs.get('name') if kwargs.get('name') else ''
        self.amount = round(float(kwargs.get('amount')), 2) if kwargs.get('amount') else 0.0

    def deposit(self, quantity: float) -> None:
        """
        Add money to the account

        :param
        quantity: float
        """
        if isinstance(quantity, float) and quantity > 0:
            self.amount += float(round(quantity, 2))
        else:
            raise ValueError("Please deposit a correct amount.")

    def balance(self) -> float:
        """
        Send back the total amount in the bank account

        :return:
        self.amount: float
        """
        return self.amount

    def withdraw(self, quantity: float) -> None:
        """
        Remove money to the account

        :param
        quantity: float
        """
        if isinstance(quantity, float) and quantity > 0:
            if self.amount - round(quantity, 2) > 0:
                self.amount -= round(quantity, 2)


class Balance(Command):
    """
    Check amount on a bank account

    :param
    receiver: Receiver
    """

    def __init__(self, receiver: Receiver):
        self.receiver = receiver

    def execute(self) -> None:
        self.receiver.balance()


class Withdraw(Command):
    """
    Let the user withdraw some amount

    :param
    receiver : Receiver
    amount: float
    """

    def __init__(self, receiver: Receiver, amount: float):
        self.receiver = receiver
        self.amount = amount

    def execute(self) -> None:
        self.receiver.withdraw(self.amount)


class Deposit(Command):
    """
    Let the user deposit an amount to it's account

    :param
    receiver: Receiver
    amount : float
    """

    def __init__(self, receiver: Receiver, amount: float):
        self.receiver = receiver
        self.amount = amount

    def execute(self) -> None:
        self.receiver.deposit(self.amount)
