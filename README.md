empty
# Python Example with an Intentional Bug

This small Python 3.x project calculates the final price of an order.
`calculate_total` applies tax as a percentage. `calculate_discount`
deliberately contains a bug: it subtracts the discount rate as a fixed amount
instead of calculating it as a percentage of the price.

Run the tests with:

```bash
python3 -m unittest discover -s tests -v
```

The `test_calculate_discount_treats_rate_as_fixed_amount` test deliberately
documents the incorrect behavior of `calculate_discount`.
