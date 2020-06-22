import unittest

import bank


class TestCommand(unittest.TestCase):
    def test_command_execute_type_check(self):
        self.assertIsNone(bank.Command.execute(self))


class TestInvoker(unittest.TestCase):
    def setUp(self) -> None:
        self.commands = [bank.Balance, bank.Deposit, bank.Withdraw]

    def test_invoker_init_command_parameter_type_check(self):
        for command in self.commands:
            invoker = bank.Invoker(command)
            self.assertIsInstance(invoker.command, command)
            # self.assertTrue(invoker.command is command)

    def test_invoker_run(self):
        self.assertIsNone(bank.Invoker.run(self))

    def tearDown(self) -> None:
        pass


class TestBalance(unittest.TestCase):
    def test_balance_execute(self):
        self.assertEqual(bank.Balance(), 0)

    def test_balance_argument_error(self):
        with self.assertRaises(IOError):
            bank.Balance(150)


class TestDeposit(unittest.TestCase):
    def test_deposit_execute(self):
        # deposit_command = bank.Deposit("50")
        pass


class TestWithdraw(unittest.TestCase):
    def setUp(self) -> None:
        self.balance = 20
        self.test_amount = -30
        self.app = bank.Withdraw(self.test_amount)

    def test_withdraw_input_is_integer(self):
        self.assertIs(self.test_amount, int)

    def test_withdraw_negative_amount(self):
        self.assertLessEqual(self.test_amount, 0)

    def test_withdraw_argument_error(self):
        with self.assertRaises(IOError):
            bank.Withdraw()

    def test_withdraw_amount_exceeds_balance(self):
        self.assertLess(self.test_amount, self.balance)

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
