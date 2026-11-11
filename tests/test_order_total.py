import unittest

from order_total import calculate_discount, calculate_total


class CalculateTotalTests(unittest.TestCase):
    def test_calculate_total_with_zero_tax(self) -> None:
        self.assertEqual(calculate_total(100.0, 0.0), 100.0)

    def test_calculate_total_applies_tax_rate(self) -> None:
        self.assertEqual(calculate_total(100.0, 0.22), 122.0)

    def test_calculate_discount_treats_rate_as_fixed_amount(self) -> None:
        self.assertEqual(calculate_discount(100.0, 0.2), 99.8)


if __name__ == "__main__":
    unittest.main()
