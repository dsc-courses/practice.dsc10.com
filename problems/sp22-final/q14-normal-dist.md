# BEGIN PROB

An IKEA employee has access to a data set of the purchase amounts for 40,000 customer transactions. This data set is roughly normally distributed with mean 150 dollars and standard deviation 25 dollars.

# BEGIN SUBPROB

Why is the distribution of purchase amounts roughly normal?

( ) because of the Central Limit Theorem
( ) for some other reason

# BEGIN SOLUTION

**Answer: ** for some other reason

The data that we have is a sample of purchase amounts. It is not a sample mean or sample sum, so the Central Limit Theorem does not apply. The data just naturally happens to be roughly normally distributed, like human heights, for example.

<average>42</average>
# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Shiv spends 300 dollars at IKEA. How would we describe Shiv's purchase in standard units?

( ) 0 standard units
( ) 2 standard units
( ) 4 standard units
( ) 6 standard units

# BEGIN SOLUTION

**Answer: ** 6 standard units

To standardize a data value, we subtract the mean of the distribution and divide by the standard deviation:

$$\begin{aligned} 
        \text{standard units} &= \frac{300 - 150}{25} \\ 
        		    &= \frac{150}{25} \\
        		    &= 6
\end{aligned}$$

A more intuitive way to think about standard units is the number of standard deviations above the mean (where negative means below the mean). Here, Shiv spent 150 dollars more than average. One standard deviation is 25 dollars, so 150 dollars is six standard deviations.

<average>97</average>
# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

 Give the endpoints of the CLT-based 95% confidence interval for the mean IKEA purchase amount, based on this data.

# BEGIN SOLUTION

**Answer: ** 149.75 and 150.25 dollars

The Central Limit Theorem tells us about the distribution of the sample mean purchase amount. That's not the distribution the employee has, but rather a distribution that shows how the mean of a *different* sample of 40,000 purchases might have turned out. Specifically, we know the following information about the distribution of the sample mean.

1. It is roughly normally distributed.
2. Its mean is about 150 dollars, the same as the mean of the employee's sample.
3. Its standard deviation is about $\frac{\text{sample standard deviation}}{\sqrt{\text{sample size}}}=\frac{25}{\sqrt{40000}} = \frac{25}{200} = \frac{1}{8}$.

Since the distribution of the sample mean is roughly normal, we can find a 95% confidence interval for the sample mean by stepping out two standard deviations from the center, using the fact that 95% of the area of a normal distribution falls within 2 standard deviations of the mean. Therefore the endpoints of the CLT-based 95% confidence interval for the mean IKEA purchase amount are

- $150 - 2*\frac{1}{8} = 149.75$ dollars, and
- $150 + 2*\frac{1}{8} = 150.25$ dollars.

<average>36</average>
# END SOLUTION

# END SUBPROB

# END PROB