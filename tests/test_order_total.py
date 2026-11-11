import unittest

from order_total import calculate_total


class CalculateTotalTests(unittest.TestCase):
    def test_calculate_total_with_zero_tax(self) -> None:
        self.assertEqual(calculate_total(100.0, 0.0), 100.0)

    def test_calculate_total_applies_tax_rate(self) -> None:
        self.assertEqual(calculate_total(100.0, 0.22), 122.0)


if __name__ == "__main__":
    unittest.main()
