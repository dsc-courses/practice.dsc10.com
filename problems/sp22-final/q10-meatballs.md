# BEGIN PROB

IKEA is piloting a new rewards program where customers can earn free Swedish meatball plates from the in-store cafe when they purchase expensive items. Meatball plates are awarded as follows. Assume the item price is always an integer.

<center>
<table class="table" style="width:30%">
  <thead>
    <tr>
      <th scope="col">Item price</th>
      <th scope="col">Number of meatball plates</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">less than 99 dollars</th>
      <td>0</td>
    </tr>
    <tr>
      <th scope="row">100 to 199 dollars</th>
      <td>1</td>
    </tr>
    <tr>
      <th scope="row">200 dollars or more</th>
      <td>2</td>
    </tr>
  </tbody>
</table>
</center>

We want to implement a function called `calculate_meatball_plates` that takes as input an array of several item prices, corresponding to the individual items purchased in one transaction, and returns the total number of meatball plates earned in that transaction.

Select all correct ways of implementing this function from the options below.

Way 1:

```py
def calculate_meatball_plates(prices): 
    meatball_plates = 0
    for price in prices:
        if price >= 100 and price <= 199:
            meatball_plates = 1
        elif price >= 200:
            meatball_plates = 2
    return meatball_plates
```

Way 2:

```py
def calculate_meatball_plates(prices): 
    meatball_plates = 0
    for price in prices:
        if price >= 200:
            meatball_plates = meatball_plates + 1
        if price >= 100:
            meatball_plates = meatball_plates + 1
    return meatball_plates
```

Way 3:

```py
def calculate_meatball_plates(prices): 
    return np.count_nonzero(prices >= 100) + np.count_nonzero(prices >= 200)
```

Way 4:

```py
def calculate_meatball_plates(prices): 
    return (prices >= 200).sum()*2 + ((100 <= prices) & (prices <= 199)).sum()*1
```

[ ] Way 1
[ ] Way 2
[ ] Way 3
[ ] Way 4

# BEGIN SOLUTION

**Answer: ** Way 2, Way 3, Way 4

Way 1 does not work because it resets the variable `meatball_plates` with each iteration instead of adding to a running total. At the end of the loop, `meatball_plates` evaluates to the number of meatball plates earned by the last price in `prices` instead of the total number of meatball plates earned by all purchases. A quick way to see this is incorrect is to notice that the only possible return values are 0, 1, and 2, but it's possible to earn more than 2 meatball plates with enough purchases.

Way 2 works. As in Way 1, it loops through each price in `prices`. When evaluating each price, it checks if the price is at least 200 dollars, and if so, increments the total number of meatball plates by 1. Then it checks if the price is at least 100 dollars, and if so, increments the count of meatball plates again. This works because for prices that are at least 200 dollars, both `if` conditions are satisfied, so the meatball plate count goes up by 2, and for prices that are between 100 and 199 dollars, only one of the `if` conditions is satisfied, so the count increases by 1. For prices less than 100 dollars, the count doesn't change. 

Way 3 works without using any iteration at all. It uses `np.count_nonzero` to count the number of prices that are at least 100 dollars, then it similarly counts the number of prices that are at least 200 dollars and adds these together. This works because prices that are at least 200 dollars are also at least 100 dollars, so they contribute 2 to the total. Prices that are between 100 and 199 contribute 1, and prices below 100 dollars don't contribute at all. 

Way 4 also works and calculates the number of meatball plates without iteration. The expression `prices >= 200` evaluates to a boolean Series with True for each price that is at least 200 dollars. Summing this Series gives a count of the number of prices that are at least 200 dollars, since True counts as 1 and False counts as 0 in Python. Each such purchase earns 2 meatball plates, so this count of purchases 200 dollars and up gets multiplied by 2. Similarly, `(100 <= prices) & (prices <= 199)` is a Series containing True for each price that is at least 100 dollars and at most 199 dollars, and the sum of that Series is the number of prices between 100 and 199 dollars. Each such purchase contributes one additional meatball plate, so the number of such purchases gets multiplied by 1 and added to the total.

<average>64</average>
# END SOLUTION

# END PROB