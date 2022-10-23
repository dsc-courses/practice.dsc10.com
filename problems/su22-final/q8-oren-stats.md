# BEGIN PROB
Oren has a random sample of 200 dog prices in an array called \oren. He has
also bootstrapped his sample 1,000 times and stored the mean of each
resample in an array called `boots`.

In this question, assume that the following code has run:

```py
a = np.mean(oren)
b = np.std(oren)
c = len(oren)
```

# BEGIN SUBPROB

What expression best estimates the population's standard deviation?

( ) `b`
( ) `b / c`
( ) `b / np.sqrt(c)`
( ) `b * np.sqrt(c)`

# BEGIN SOLUTION

**Answer: ** `b`

The function `np.std` directly calculated the standard deviation of array `oren`. Even though `oren` is sample of the population, it's still a pretty good estimate for the std since it's a random sample. The other options don't really make sense in this context. 

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Which expression best estimates the mean of `boots`?

( ) 0
( ) `a`
( ) `(oren - a).mean()`
( ) `(oren - a) / b`

# BEGIN SOLUTION

**Answer: ** `a`

Note that `a` is equal to the mean of `oren`, which is a pretty good estimator of the mean of the overall population. The other options don't really make sense in this context. 

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

What expression best estimates the standard deviation of `boots`?

( ) `b`
( ) `b / c`
( ) `b / np.sqrt(c)`
( ) `(a -b) / np.sqrt(c)`

# BEGIN SOLUTION

**Answer: ** `b / np.sqrt(c)`

Note that we can use the central limit theorem for this problem which states that the STD of the sample distribution is equal to `(population STD) / np.sqrt(sample size)`. Since our sample is also the population in this case, we can plug our variables in to see that `b / np.sqrt(c)` is our answer.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

What is the price of $560 in standard units?

( ) `(560 - a) / b`
( ) `(560 - a) / (b / np.sqrt(c))`
( ) `(a - 560) / (b / np.sqrt(c))}`
( ) `abs(560 - a) / b`
( ) `abs(560 - a) / (b / np.sqrt(c))`

# BEGIN SOLUTION

**Answer: ** `(560 - a) / b`

To convert a value to standard units, we simply take the value, subtract it by the mean, and divide by STD, which in this case is `(560 - a) / b`.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

The distribution of `boots` is normal because of the Central
Limit Theorem.

( ) True
( ) False

# BEGIN SOLUTION

**Answer: ** True

True. The central limit theorem states that if you have a populations and take a sufficiently large number of random samples form the population, then the distribution of the sample means will be approximately normally distributed.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

If Oren's sample was 400 dogs instead of 200, the standard deviation of `boots` will...

( ) Increase by a factor of $2$
( ) Increase by a factor of $\sqrt{2}$
( ) Decrease by a factor of 2
( ) Decrease by a factor of $\sqrt{2}$
( ) None of the above

# BEGIN SOLUTION

**Answer: ** Decrease by a factor of $\sqrt{2}$

Recall that the central limit theorem states that the STD of the sample distribution is equal to `(population STD) / np.sqrt(sample size)`. So if we increase the sample size by a factor of 2, the STD of the sample distribution will decrease by a factor of $\sqrt{2}$.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

If Oren took 4000 bootstrap resamples instead of 1000, the standard deviation of `boots` will...

( ) Increase by a factor of 4
( ) Increase by a factor of 2
( ) Decrease by a factor of 2
( ) Decrease by a factor of 4
( ) None of the above

# BEGIN SOLUTION

**Answer: ** None of the above

Again, from our formula given by the central limit theorem, the sample STD doesn't depend on the number of bootstrap resamples so long as it's "sufficiently large". Thus increasing our bootstrap sample form 1000 to 4000 will have no effect on the std of `boots`

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Write one line of code that evaluates to the **right
endpoint** of a 92% normal theory confidence interval for the mean
dog price. The following expressions may help:

```py
stats.norm.cdf(1.75) # => 0.96
stats.norm.cdf(1.4)  # => 0.92
```

# BEGIN SOLUTION

**Answer: ** `a + 1.75 * b / np.sqrt(c)`

Recall that a 92% confidence interval means an interval that consists of the middle 92% of the distribution. In other words, we want to "chop" off 4% from either end of the ditribution. Thus to get the right endpoint, we want the value corresponding to the 96th percentile, or `mean + 1.75 * (std of population / np.sqrt(sample size)` or `a + 1.75 * b / np.sqrt(c)` (we divide by `np.sqrt(c)` due to the central limit theorem). Note, that the second line of information that was given `stats.norm.cdf(1.4)` is irrelavant to this particular problem.

# END SOLUTION

# END SUBPROB

# END PROB
