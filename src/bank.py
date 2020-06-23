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


class Balance(Command):
    """
        Check amount on a bank account
    """

    def execute(self) -> None:
        pass


class Withdraw(Command):
    """
        Let the user withdraw some amount
    """

    def execute(self) -> None:
        pass


class Deposit(Command):
    """
        Let the user deposit an amount to it's account
    """

    def execute(self) -> None:
        pass


if __name__ == '__main__':
    pass
