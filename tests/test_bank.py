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
            self.assertTrue(invoker.command is command)

    def test_invoker_run(self):
        receiver = bank.Receiver(name='adria', amount=50)
        invoker = bank.Invoker(bank.Balance(receiver))
        self.assertIsNone(invoker.run())

    def tearDown(self) -> None:
        pass


class TestReceiver(unittest.TestCase):
    def setUp(self) -> None:
        self.receiver = bank.Receiver(name="adria", amount=50)

    def test_receiver_has_attribute_name(self):
        self.assertTrue(hasattr(self.receiver, 'name'))

    def test_receiver_has_attribute_amount(self):
        self.assertTrue(hasattr(self.receiver, 'amount'))

    def test_receiver_attribute_name_is_type_string(self):
        self.assertIs(type(self.receiver.name), str)

    def test_receiver_attribute_amount_is_type_string(self):
        self.assertIs(type(self.receiver.amount), int)

    def test_receiver_deposit(self):
        self.receiver.deposit(30.00)
        self.assertEqual(self.receiver.amount, 80)

    def test_receiver_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.receiver.deposit(-3)

    def test_receiver_deposit_wrong_amount_type(self):
        with self.assertRaises(ValueError):
            self.receiver.deposit("a")

    def tearDown(self) -> None:
        pass


class TestBalance(unittest.TestCase):
    def test_balance_execute(self):
        self.assertEqual(bank.Balance(), 0)

    def test_balance_argument_error(self):
        with self.assertRaises(IOError):
            bank.Balance(150)


class TestDeposit(unittest.TestCase):
    def setUp(self) -> None:
        self.balance = 30
        self.test_amount = 30

    def test_deposit_execute(self):
        self.assertEquals(bank.Deposit(self.test_amount), sum([self.balance, self.test_amount]))

    def test_deposit_input_is_integer(self):
        self.assertIs(self.test_amount, int)

    def test_deposit_negative_amount(self):
        self.assertLessEqual(self.test_amount * -1, 0)

    def test_deposit_argument_error(self):
        with self.assertRaises(IOError):
            bank.Deposit()

    def tearDown(self) -> None:
        pass


class TestWithdraw(unittest.TestCase):
    def setUp(self) -> None:
        self.balance = 20
        self.test_amount = -30
        self.app = bank.Withdraw(self.test_amount)

    def test_withdraw_execute(self):
        self.assertEquals(bank.Withdraw(self.test_amount), self.balance - self.test_amount)

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
