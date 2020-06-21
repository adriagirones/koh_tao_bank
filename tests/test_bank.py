import unittest
import bank


class TestCommand(unittest.TestCase):
    def test_command_execute(self):
        self.assertEqual(bank.Command.execute(self), None)


class TestDeposit(unittest.TestCase):
    def test_invoker_execute(self):
        # deposit_command = bank.Deposit("50")
        # deposit_invoker = bank.Invoker(deposit_command)
        # deposit_invoker.execute()
        pass


class TestBalance(unittest.TestCase):
    def test_balance_execute(self):
        # balance_command = bank.Balance()
        # balance_invoker = bank.Invoker(balance_command)
        # balance_invoker.execute()
        pass


class TestWithdraw(unittest.TestCase):
    def test_withdraw_execute(self):
        # withdraw_command = bank.Withdraw("150")
        # withdraw_invoker = bank.Invoker(withdraw_command)
        # withdraw_invoker.execute()
        pass


if __name__ == '__main__':
    unittest.main()
