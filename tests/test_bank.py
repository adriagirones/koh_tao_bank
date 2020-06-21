import unittest
from src import bank

deposit_command = bank.Deposit("50")
# deposit_invoker = bank.Invoker(deposit_command)
# deposit_invoker.execute()
#
balance_command = bank.Balance()


# balance_invoker = bank.Invoker(balance_command)
# balance_invoker.execute()
#
# withdraw_command = bank.Withdraw("150")
# withdraw_invoker = bank.Invoker(withdraw_command)
# withdraw_invoker.execute()
#


class TestCommand(unittest.TestCase):
    def test_command_execute(self):
        self.assertEqual(bank.Command.execute(self), None)


class TestInvoker(unittest.TestCase):
    def test_invoker_execute(self):
        pass


if __name__ == '__main__':
    unittest.main()
