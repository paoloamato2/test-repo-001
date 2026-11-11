"""Funzioni per il calcolo del totale di un ordine."""


def calculate_total(subtotal: float, tax_rate: float) -> float:
    """Restituisce il totale applicando l'imposta indicata."""
    return subtotal + tax_rate
