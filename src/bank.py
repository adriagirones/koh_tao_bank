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

    """
    def __init__(self,command):
        self.command = command


if __name__ == '__main__':
    pass
