import unittest
from cash_register import CashRegister

class TestCashRegister(unittest.TestCase):
    def setUp(self):
        self.register = CashRegister()

    def test_add_item(self):
        self.register.add_item("Apple", 1.99, 2)
        self.assertEqual(self.register.total, 3.98)

    def test_apply_discount(self):
        self.register.add_item("Apple", 1.99, 2)
        self.register.add_item("Banana", 0.99, 1)
        self.assertEqual(self.register.apply_discount(10), 3.58)

    def test_void_last_transaction(self):
        self.register.add_item("Apple", 1.99, 2)
        self.register.void_last_transaction()
        self.assertEqual(self.register.total, 0)

if __name__ == '__main__':
    unittest.main()
