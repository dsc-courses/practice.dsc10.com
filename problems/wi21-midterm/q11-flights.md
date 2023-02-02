# BEGIN PROB

<span style="color:red"><b>Note: This problem is out of scope; it covers material no longer included in the course.</b></span>

You have a DataFrame called `flights` containing information on various plane tickets sold between US cities. The columns are `'route_length'`, which stores distance between the arrival and departure airports, in miles, and `'price'`, which stores the cost of the airline ticket, in dollars. You notice that longer flights tend to cost more, as expected.

| route_length    | price |
| ----------- | ----------- |
| 2500   | 249      |
| 2750   | 249      |
| 2850   | 349      |
| 2850   | 319      |
| 2950   | 329      |
| 2950   | 309      |
| 3000   | 349      |
<br/>
You want to use your data, shown in full above, to predict the price of an airline ticket for a route that is 2800 miles long. What would Galton's method predict for the price of your ticket, if we consider "nearby" to mean within 6o miles? Give your answer to the nearest dollar.

# BEGIN SOLUTION

**Answer: ** 306 dollars

Galton's method for making predictions is to take "nearby" $x$-values and average their corresponding $y$-values. For example, to predict the height of a child born to 70-inch parents, he averages the heights of children born to families where the parents are close to 70 inches tall. Using that same strategy here, we first need to identify which flights are considered "nearby" to a route that is 2800 miles. We are told that "nearby" means within 60 miles, so we are looking for flights between 2740 and 2860 miles in length. There are three such flights (the second, third, and fourth rows of the original data):

| route_length    | price |
| ----------- | ----------- |
| 2750   | 249      |
| 2850   | 349      |
| 2850   | 319      |
<br/>
Now, we simply need to average these three prices to make our prediction. Since $\frac{249+349+319}{3} = 305.67$ and we are told to round to the nearest dollar, our prediction is 306 dollars.

<average>59</average>
# END SOLUTION

# END PROB