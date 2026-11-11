empty
# Esempio Python con bug intenzionale

Questo piccolo progetto Python 3.x calcola il prezzo finale di un ordine.
Contiene deliberatamente un errore in `calculate_total`: l'imposta viene
aggiunta come importo fisso anziché calcolata come percentuale.

Esegui i test con:

```bash
python3 -m unittest discover -s tests -v
```

Il test `test_calculate_total_applies_tax_rate` fallisce intenzionalmente e
riproduce il problema descritto nell'issue GitHub associato.
