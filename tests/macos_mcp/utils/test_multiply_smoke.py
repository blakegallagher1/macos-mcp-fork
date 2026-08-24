import unittest
from decimal import Decimal
from fractions import Fraction
from src.macos_mcp.utils.math import multiply

class TestMultiplySmoke(unittest.TestCase):
    def test_decimal(self):
        self.assertEqual(multiply(Decimal('1.5'), Decimal('2')), Decimal('3.0'))
    def test_fraction(self):
        self.assertEqual(multiply(Fraction(1, 3), Fraction(3, 4)), Fraction(1, 4))
    def test_mixed(self):
        self.assertEqual(multiply(2, Fraction(3, 5)), Fraction(6, 5))
        self.assertEqual(multiply(Decimal('2'), 3), Decimal('6'))

if __name__ == '__main__':
    unittest.main()
