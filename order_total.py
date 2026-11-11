"""Functions for calculating order totals."""


def calculate_total(subtotal: float, tax_rate: float) -> float:
    """Return the total after applying the specified tax rate."""
    return subtotal + subtotal * tax_rate


def calculate_discount(price: float, discount_rate: float) -> float:
    """Return the price after applying the specified discount rate."""
    return price - discount_rate
