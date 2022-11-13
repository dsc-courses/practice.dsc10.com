# BEGIN PROB

For each IKEA desk, we know the cost of producing the desk, in dollars, and the current sale price of the desk, in dollars. We want to predict sale price based on production cost using linear regression. 

# BEGIN SUBPROB

For this scenario, which of the following most likely describes the slope of the regression line when both variables are measured in dollars?

( ) less than 0
( ) between 0 and 1, exclusive
( ) more than 1
( ) none of the above (exactly equal to 0 or 1)

# BEGIN SOLUTION

**Answer: ** more than 1

The slope of a line represents the change in $y$ for each change of 1 in $x$. Therefore, the slope of the regression line is the amount we'd predict the sale price to increase when the production cost of an item increases by one dollar. In other words, it's the sale price per dollar of production cost. This is almost certainly more than 1, otherwise the company would not make a profit. We'd expect that for any company, the sale price of an item should exceed the production cost, meaning the slope of the regression line has a value greater than one.

<average>72</average>
# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

For this scenario, which of the following most likely describes the slope of the regression line when both variables are measured in standard units?

( ) less than 0
( ) between 0 and 1, exclusive
( ) more than 1
( ) none of the above (exactly equal to 0 or 1)

# BEGIN SOLUTION

**Answer: ** between 0 and 1, exclusive

When both variables are measured in standard units, the slope of the regression line is the correlation coefficient. Recall that correlation coefficients are always between -1 and 1, however, because it’s not realistic for production cost and sale price to be negatively correlated (as that would mean products sell for less if they cost more to produce) we can limit our choice of answer to values between 0 and 1. Because a coefficient of 0 would mean there is no correlation and 1 would mean perfect correlation (that is, plotting the data would create a line), these are unlikely occurrences leaving us with the answer being between 0 and 1, exclusive.

<average>86</average>
# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

The residual plot for this regression is shown below.

<center><img src='../assets/images/sp22-final/resid.png' width=40%></center>

What is being represented on the horizontal axis of the residual plot?

( ) actual production cost
( ) actual sale price
( ) predicted production cost
( ) predicted sale price

# BEGIN SOLUTION

**Answer: ** actual production cost

Residual plots show $x$ on the horizontal axis and the residuals, or differences between actual $y$ values and predicted $y$ values, on the vertical axis. Therefore, the horizontal axis here shows the production cost. Note that we are not predicting production costs at all, so production cost means the *actual* cost to produce a product.

<average>43</average>
# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Which of the following is a correct conclusion based on this residual plot? Select all that apply.

[ ] The correlation between production cost and sale price is weak.
[ ] It would be better to fit a nonlinear curve.
[ ] Our predictions will be more accurate for some inputs than others.
[ ] We don't have enough data to do regression.
[ ] The regression line is not the best-fitting line for this data set.
[ ] The data set is not representative of the population.

# BEGIN SOLUTION

**Answer: ** It would be better to fit a nonlinear curve.

Let's go through each answer choice.

- The correlation between production cost and sale price could be very strong. After all, we are able to predict the sale price within ten dollars almost all the time, since residuals are almost all between -10 and 10. 

- It would be better to fit a nonlinear curve because the residuals show a pattern. Reading from left to right, they go from mostly negative to mostly positive to mostly negative again. This suggests that a nonlinear curve might be a better fit for our data.

- Our predictions are typically within ten dollars of the actual sale price, and this is consistent throughout. We see this on the residual plot by a fairly even vertical spread of dots as we scan from left to right. This data is not heteroscedastic.

- We can do regression on a dataset of any size, even a very small data set. Further, this dataset is decently large, since there are a good number of points in the residual plot. 

- The regression line is **always** the best-fitting line for any dataset. There may be other curves that are better fits than lines, but when we restrict to lines, the best of the bunch is the regression line.

- We have no way of knowing how representative our data set is of the population. This is not something we can discern from a residual plot because such a plot contains no information about the population from which the data was drawn.

<average>61</average>
# END SOLUTION

# END SUBPROB

# END PROB