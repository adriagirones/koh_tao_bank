import unittest

import bank


class TestCommand(unittest.TestCase):
    def test_command_execute_type_check(self):
        self.assertIsNone(bank.Command.execute(self))


class TestInvoker(unittest.TestCase):
    def test_invoker_init_command_parameter_type_check(self):
        commands = [bank.Balance, bank.Deposit, bank.Withdraw]
        for command in commands:
            invoker = bank.Invoker(command)
            self.assertIsInstance(invoker.command, command)
            # self.assertTrue(invoker.command is command)

    def test_invoker_run(self):
        self.assertIsNone(bank.Invoker.run(self))


class TestBalance(unittest.TestCase):
    def test_balance_execute(self):
        # balance_command = bank.Balance()
        # balance_invoker = bank.Invoker(balance_command)
        # balance_invoker.execute()
        pass


class TestDeposit(unittest.TestCase):
    def test_deposit_execute(self):
        # deposit_command = bank.Deposit("50")
        # deposit_invoker = bank.Invoker(deposit_command)
        # deposit_invoker.execute()
        pass


class TestWithdraw(unittest.TestCase):
    def test_withdraw_execute(self):
        # withdraw_command = bank.Withdraw("150")
        # withdraw_invoker = bank.Invoker(withdraw_command)
        # withdraw_invoker.execute()
        pass


if __name__ == '__main__':
    unittest.main()
