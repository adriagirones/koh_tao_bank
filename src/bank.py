import abc


class Command:
    """
    Parent object executing an abstract method
    """

    @abc.abstractmethod
    def execute(self) -> None:
        pass


if __name__ == '__main__':
    pass
