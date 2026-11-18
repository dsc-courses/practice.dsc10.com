# BEGIN PROB

# BEGIN SUBPROB

We're interested in predicting the admission cost of a museum based on its number of visitors. Suppose: 

* admission cost and number of visitors are linearly associated with a correlation coefficient of 0.25, 

* the number of visitors at the Museum of Natural History is six standard deviations below average, 

* the average cost of museum admission is 15 dollars, and

* the standard deviation of admission cost is 3 dollars.

What would the regression line predict for the admission cost (in dollars) at the Museum of Natural History? Give your answer as a number without any units, rounded to three decimal places.

# BEGIN SOLUTION

**Answer:** 10.500

Recall, the regression line predicts that a value of x (the independent variable) which is $n$ standard units above (or below) average $\bar{x}$ has a value of y (dependent variable) which is $rn$ standard units above (or below) average $\bar{y}$

In this question, our correlation coefficient ($r$) is 0.25. The number of visitors is x, and the admission cost is y. Given that the number of visitors at the Museum of Natural History is six standard deviations below average, $$y_{\ \text {Museum of Natural History}} = \bar{y}-6\cdot \text{SD of y}$$ we can compute how much standard deviation is admission cost (in dollars) at the Museum of Natural History below the average:$$\frac{6}{r} = \frac{6}{0.25} = 1.5$$ 

Thus, we have $$x_{\ \text {Museum of Natural History}} = \bar{x}-1.5\cdot \text{SD of x}$$

Since $\bar{x} = 15\ \text{dollars}$, $\text{SD of x} = 3\ \text{dollars}$,
$$x_{\ \text {Museum of Natural History}} = 15\ \text{dollars} -1.5\cdot 3\ \text{dollars} = 10.500\ \text{dollars}$$

<average>62</average>

# END SOLUTION

# END SUBPROB

# END PROB