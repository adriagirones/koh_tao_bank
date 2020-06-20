import unittest

import bank


class TestCommand(unittest.TestCase):
    def test_command_execute(self):
        self.assertEqual(bank.Command.execute(self), None)


class TestReceiver(unittest.TestCase):
    def test_receiver_action(self):
        self.assertEqual(bank.Receiver.action(self), None)


class TestInvoker(unittest.TestCase):
    def test_invoker_store_commands(self):
        invoker = bank.Invoker()
        invoker.store_command("duck")
        invoker.store_command(3)
        invoker.store_command(True)
        self.assertListEqual(["duck", 3, True], invoker._commands)


if __name__ == '__main__':
    unittest.main()
