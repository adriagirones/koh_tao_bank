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

    def test_receiver_has_method_deposit(self):
        self.assertTrue(callable(self.receiver.deposit))

    def test_receiver_deposit(self):
        self.receiver.deposit(30.00)
        self.assertEqual(self.receiver.amount, 80)

    def test_receiver_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.receiver.deposit(-3)

    def test_receiver_deposit_wrong_amount_type(self):
        with self.assertRaises(ValueError):
            self.receiver.deposit("a")

    def test_receiver_has_method_balance(self):
        self.assertTrue(callable(self.receiver.balance))

    def test_receiver_balance(self):
        self.assertEquals(self.receiver.amount, 50.00)

    def test_receiver_balance_return_type(self):
        self.assertTrue(type(self.receiver.amount) is float)

    def test_receiver_has_method_withdraw(self):
        self.assertTrue(callable(self.receiver.withdraw))

    def test_receiver_withdraw(self):
        self.receiver.withdraw(30.00)
        self.assertEqual(self.receiver.amount, 20)

    def test_receiver_withdraw_negative_amount(self):
        with self.assertRaises(ValueError):
            self.receiver.withdraw(-3)

    def test_receiver_withdraw_wrong_amount_type(self):
        with self.assertRaises(ValueError):
            self.receiver.withdraw("a")

    def tearDown(self) -> None:
        pass


class TestBalance(unittest.TestCase):
    def setUp(self) -> None:
        receiver = bank.Receiver(name="adria", amount=50)
        self.command = bank.Balance(receiver)

    def test_balance_execute(self):
        self.assertEqual(self.command.execute(), 50.0)

    def test_balance_has_attribute_receiver(self):
        self.assertTrue(hasattr(self.command, "receiver"))

    def test_balance_attribute_receiver_is_type_Receiver(self):
        self.assertIs(type(self.command.receiver), bank.Receiver)

    def tearDown(self) -> None:
        pass


class TestWithdraw(unittest.TestCase):
    def setUp(self) -> None:
        self.receiver = bank.Receiver(name="adria", amount=50)
        self.command = bank.Withdraw(self.receiver, 30.0)

    def test_withdraw_execute(self):
        self.command.execute()
        self.assertEqual(self.receiver.amount, 20.0)

    def test_withdraw_has_attribute_receiver(self):
        self.assertTrue(hasattr(self.command, "receiver"))

    def test_withdraw_has_attribute_amount(self):
        self.assertTrue(hasattr(self.command, "amount"))

    def test_withdraw_attribute_receiver_type(self):
        self.assertIs(type(self.command.receiver), bank.Receiver)

    def test_withdraw_attribute_amount_type(self):
        self.assertTrue(type(self.command.amount) is float)

    def tearDown(self) -> None:
        pass


class TestDeposit(unittest.TestCase):
    def setUp(self) -> None:
        self.receiver = bank.Receiver(name="adria", amount=50)
        self.command = bank.Deposit(self.receiver, 30.0)

    def test_deposit_execute(self):
        self.command.execute()
        self.assertEqual(self.receiver.amount, 80.0)

    def test_deposit_has_attribute_receiver(self):
        self.assertTrue(hasattr(self.command, "receiver"))

    def test_deposit_has_attribute_amount(self):
        self.assertTrue(hasattr(self.command, "amount"))

    def test_deposit_attribute_receiver_type(self):
        self.assertIs(type(self.command.receiver), bank.Receiver)

    def test_deposit_attribute_amount_type(self):
        self.assertTrue(type(self.command.amount) is float)

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
