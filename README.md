empty
# Esempio Python con bug intenzionale

Questo piccolo progetto Python 3.x calcola il prezzo finale di un ordine.
`calculate_total` applica l'imposta come percentuale. `calculate_discount`
contiene invece deliberatamente un errore: sottrae il tasso di sconto come
importo fisso anziché calcolarlo come percentuale del prezzo.

Esegui i test con:

```bash
python3 -m unittest discover -s tests -v
```

Il test `test_calculate_discount_treats_rate_as_fixed_amount` documenta
deliberatamente il comportamento errato di `calculate_discount`.
