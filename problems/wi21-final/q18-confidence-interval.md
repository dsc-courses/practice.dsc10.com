# BEGIN PROB

**True or False**: Suppose that from a sample, you compute a 95% bootstrapped confidence interval for a population parameter to be the interval [L, R]. Then the average of L and R is the mean of the original sample.

# BEGIN SOLUTION

**Answer: ** False

A 95% confidence interval indicates we are 95% confident that the true population parameter falls within the interval [L, R]. Note that the problem specifies that the confidence interval is bootstrapped. Since the interval is found using bootstrapping, L and R averaged will not be the mean of the original sample since the mean of the original sample is not what is used in calculating the bootstrapped confidence interval. The bootstrapped confidence interval is created by re-sampling the data with replacement over and over again. Thus, while the interval is typically centered around the sample mean due to the nature of bootstrapping, the average of L and R (the 2.5th and 97.5th percentiles of the distribution of bootstrapped means) may not exactly equal the sample mean, but should be close to it. Additionally, L is the 2.5th percentile of the distribution of bootstrapped means and R is the 97.5th percentile, and these are not necessarily the same distance away from the mean of the sample.

<average>87</average>
# END SOLUTION


# END PROB
