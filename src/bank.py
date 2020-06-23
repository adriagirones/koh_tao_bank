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
        self.command.run()


if __name__ == '__main__':
    pass
