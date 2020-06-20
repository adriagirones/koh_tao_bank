import unittest
import bank


class Command(unittest.TestCase):
    def test_balance(self):
        self.assertEqual(bank.Command.execute(), False)


if __name__ == '__main__':
    unittest.main()
