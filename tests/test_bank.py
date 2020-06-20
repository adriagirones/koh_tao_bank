import unittest

import bank


class TestCommand(unittest.TestCase):
    def test_command_execute(self):
        self.assertEqual(bank.Command.execute(self), None)


class TestReceiver(unittest.TestCase):
    def test_receiver_action(self):
        self.assertEqual(bank.Receiver.action(self), None)


if __name__ == '__main__':
    unittest.main()
