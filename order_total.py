"""Funzioni per il calcolo del totale di un ordine."""


def calculate_total(subtotal: float, tax_rate: float) -> float:
    """Restituisce il totale applicando l'imposta indicata."""
    return subtotal + subtotal * tax_rate


def calculate_discount(price: float, discount_rate: float) -> float:
    """Restituisce il prezzo dopo lo sconto indicato."""
    return price - discount_rate
