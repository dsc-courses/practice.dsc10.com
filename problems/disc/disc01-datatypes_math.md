# BEGIN PROB

`prices` is an array of prices, in dollars, of different products at the grocery store. Similarly, `calories` is an array of the calories in these same products, in the same order.

# BEGIN SUBPROB

What does `type(prices[0])` evaluate to?

( ) `int`
( ) `float`
( ) `str`
( ) The price of the first product.

# BEGIN SOLN

**Answer:** `float`

`prices[0]` represents the price in dollars of some product at the grocery store. The data type should be a `float` because prices are numbers but not necessarily integers.

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

What does `type(calories[0])` evaluate to?

( ) `int`
( ) `float`
( ) `str`
( ) The calories in the first product.

# BEGIN SOLN

**Answer:** `int`

Similarly, `calories[0]` represents the calories in some product at the grocery store. The data type should be `int` because calories in foods are always reported as integers.

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

When we divide two arrays of the same length, their corresponding elements get divided, and the result is a new array of the same length as the two originals. In one sentence, interpret the meaning of `min(prices / calories)`.

# BEGIN SOLN

**Answer:** This is the cost per calorie of the product which has the lowest cost per calorie, which you might say is the cheapest food to fuel up on (like instant ramen or pasta).

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

True or False: `min(prices / calories)` is the same as `max(calories / price)`.

# BEGIN SOLN

**Answer:** False

The former is measured in dollars per calories (a very small number), whereas the latter is measured in calories per dollar (a very big number).

However, there is a connection between these two values. The product that has the lowest price per calorie is the same product with the most calories per dollar. So these numbers refer to the same grocery store product, and we can convert one value into the other by taking the reciprocal, which swaps the numerator and denominator of a fraction. Therefore, it's true that `min(prices / calories)` is the same as `1 / max(calories / price)`.

# END SOLN

# END SUBPROB

# END PROB