# BEGIN PROB

# BEGIN SUBPROB

Now, the Museum of Natural History wants to know how many visitors they have in a year. However, their computer systems are rather archaic and so they aren't able to keep track of the number of tickets sold for an entire year. Instead, they randomly select five days in the year, and keep track of the number of visitors on those days. Let's call these numbers $v_1$, $v_2$, $v_3$, $v_4$, and $v_5$.

Which of the following is the best estimate the number of visitors for the entire year?

( ) $v_1 + v_2 + v_3 + v_4 + v_5$
( ) $\frac{5}{365}\cdot(v_1 + v_2 + v_3 + v_4 + v_5)$
( ) $\frac{365}{5}\cdot(v_1 + v_2 + v_3 + v_4 + v_5)$
( ) $365\cdot v_3$

# BEGIN SOLUTION

**Answer: ** $\frac{365}{5}\cdot(v_1 + v_2 + v_3 + v_4 + v_5)$

Our sample is the number of vistors on the five days, and our population is the number of visitors in all 365 days. 

First, we calculate the sample mean, the average number of vistors in the 5 days, which is $m = \frac{1}{5}\cdot(v_1 + v_2 + v_3 + v_4 + v_5)$. We use this statistic to estimate the poplulation mean, the average number of vistors in this year.

Then, we use the estimated population mean to calculate the estimated puplulation sum, so we multiply the number of days in a year (365) with the estimated population mean. We get $$365 m = \frac{365}{5}\cdot(v_1 + v_2 + v_3 + v_4 + v_5)$$

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Now we're interested in predicting the admission cost of a museum based on its number of visitors. Suppose: 

* admission cost and number of visitors are linearly associated with a correlation coefficient of 0.25, 

* the number of visitors at the Museum of Natural History is six standard deviations below average, 

* the average cost of museum admission is 15 dollars, and

* the standard deviation of admission cost is 3 dollars.

What would the regression line predict for the admission cost (in dollars) at the Museum of Natural History? Give your answer as a number without any units, rounded to three decimal places.

# BEGIN SOLUTION

**Answer: ** 10.500

Recall, the regression line predicts that a value of x (the independent varaible) which is $n$ standard units above (or below) average $\bar{x}$ has a value of y (dependent variable) which is $rn$ standard units above (or below) average $\bar{y}$

In this question, our correlation coefficient ($r$) is 0.25. The number of visitors is x, and the admission cost is y. Given that the number of visitors at the Museum of Natural History is six standard deviations below average, $$y_{\ \text {Museum of Natural History}} = \bar{y}-6\cdot \text{SD of y}$$ we can compute how much standard deviation is admission cost (in dollars) at the Museum of Natural History below the average:$$\frac{6}{r} = \frac{6}{0.25} = 1.5$$ 

Thus, we have $$x_{\ \text {Museum of Natural History}} = \bar{x}-1.5\cdot \text{SD of x}$$

Since $\bar{x} = 15\ \text{dollars}$, $\text{SD of x} = 3\ \text{dollars}$,
$$x_{\ \text {Museum of Natural History}} = 15\ \text{dollars} -1.5\cdot 3\ \text{dollars} = 10.500\ \text{dollars}$$

# END SOLUTION

# END SUBPROB

# END PROB