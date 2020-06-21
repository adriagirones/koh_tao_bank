import user


class bank:
    pass


if __name__ == '__main__':
    adria = user.UserBank('adria')
    print(adria.balance())
    adria.deposit(50)
    print(adria.balance())
    print(adria.withdraw(45))
    print(adria.balance())
    print(adria.withdraw(100))
    print(adria.balance())
