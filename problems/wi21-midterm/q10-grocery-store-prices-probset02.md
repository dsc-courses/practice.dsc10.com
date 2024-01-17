# BEGIN PROB

You have a DataFrame called `prices` that contains information about food prices at 18 different grocery stores. There is column called `'broccoli'` that contains the price in dollars for one pound of broccoli at each grocery store. There is also a column called `'ice_cream'` that contains the price in dollars for a pint of store-brand ice cream.

# BEGIN SUBPROB

What should `type(prices.get('broccoli').iloc[0])` output?

( ) int
( ) float
( ) array
( ) Series

# BEGIN SOLUTION

**Answer: ** float

This code extracts the first entry of the `'broccoli'` column. Since this column contains prices in dollars for a pound of broccoli, it makes sense to represent such a price using a float, because the price of a pound of broccoli is not necessarily an integer.

<average>92</average>
# END SOLUTION

# END SUBPROB

# END PROB