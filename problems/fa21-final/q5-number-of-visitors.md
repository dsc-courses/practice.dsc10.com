# BEGIN PROB

# BEGIN SUBPROB

Now, the Museum of Natural History wants to know how many visitors they have in a year. However, their computer systems are rather archaic and so they aren't able to keep track of the number of tickets sold for an entire year. Instead, they randomly select five days in the year, and keep track of the number of visitors on those days. Let's call these numbers $v_1$, $v_2$, $v_3$, $v_4$, and $v_5$.

Which of the following is the best estimate the number of visitors for the entire year?

( ) $v_1 + v_2 + v_3 + v_4 + v_5$
( ) $\frac{5}{365}\cdot(v_1 + v_2 + v_3 + v_4 + v_5)$
( ) $\frac{365}{5}\cdot(v_1 + v_2 + v_3 + v_4 + v_5)$
( ) $365\cdot v_3$

# BEGIN SOLUTION

**Answer:** $\frac{365}{5}\cdot(v_1 + v_2 + v_3 + v_4 + v_5)$

Our sample is the number of visitors on the five days, and our population is the number of visitors in all 365 days. 

First, we calculate the sample mean, the average number of visitors in the 5 days, which is $m = \frac{1}{5}\cdot(v_1 + v_2 + v_3 + v_4 + v_5)$. We use this statistic to estimate the population mean, the average number of visitors in this year.

Then, we use the estimated population mean to calculate the estimated pupulation sum, so we multiply the number of days in a year (365) with the estimated population mean. We get $$365 m = \frac{365}{5}\cdot(v_1 + v_2 + v_3 + v_4 + v_5)$$

<average>92</average>

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

**Answer:** 10.500

Recall, we can make predictions in standard units with the following formula

$$ \text{predicted}\ y_{su} = r \cdot x_{su}$$

We're given that the correlation coefficient, $r$, between visitors and admission cost is 0.25. Here, we're using the number of visitors ($x$) to predict admission cost ($y$). Given that the number of visitors at the Museum of Natural History is 6 standard deviations **below** average, 

$$\text{predicted}\ y_{su} =  r \cdot x_{su} = 0.25 \cdot -6 =  -1.5$$

We then compute y, which is the admission cost (in dollars) at the Museum of Natural History.

$$\begin{align*} y_{su} &= \frac{y- \text{Mean of } y}{\text{SD of } y}\\
-1.5 &= \frac{y-15}{3} \\
-1.5 \cdot 3 &= y-15\\
-4.5 + 15 &= y\\
y &= \boxed{10.5}
\end{align*}
$$

So, the regression line predicts that the admission cost at the Museum of Natural History is \$10.50.

<average>62</average>

# END SOLUTION

# END SUBPROB

# END PROB