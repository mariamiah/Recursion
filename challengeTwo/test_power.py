import unittest
from power import power, a, b


class TestPower(unittest.TestCase):
    def test_power(self):
        self.assertEqual(power(3, 4), 81)
    
    def test_power_one(self):
        self.assertEqual(power(3, 1), 3)
        self.assertEqual(power(0, 1), 0)
        self.assertEqual(power(-2, 1), -2)
    
    def test_value_type(self):
        self.assertIsInstance(a, int)
        self.assertIsInstance(b, int)
