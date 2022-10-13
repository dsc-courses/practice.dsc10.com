# BEGIN PROB
Answer the following true/false questions.

# BEGIN SUBPROB

When John Snow took off the handle from the Broad Street pump, the
number of cholera deaths decreased. Because of this, he could
conclude that cholera was caused by dirty water.

( ) True
( ) False

# BEGIN SOLUTION

**Answer: ** False

There are a couple details that the problem fails to convey and that we cannot assume. 1) Do we even know that the pump he removed was the only pump with dirty water? 2) Do we know that people even drank/took water from the Broad Street pump? 3) Do we even know what kinds of people drank from the Broad Street pump?

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

If you get a p-value of 0.009 using a permutation test, you can
conclude causality.

( ) True
( ) False

# BEGIN SOLUTION

**Answer: ** False

Permutation tests don't prove causality. Remember, we typically use the permutation test and calculate a p-value to reject a null hypothesis, not to prove the alternative.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

`df.groupby("kind").mean()` will have 5 columns.

( ) True
( ) False

# BEGIN SOLUTION

**Answer: ** True

Referring to `df` at the beginning of the exam, we could see that 5 of the columns have numerical values as inputs, and thus `df.groupby("kind").mean()` will return the mean of these 5 numerical columns

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

If the 95% confidence interval for dog price is [650, 900], there
is a 95% chance that the population dog price is between $650 and
$900.

# BEGIN SOLUTION

**Answer: ** False

A confidence interval gives us an interval in which one can be 95% confident that the population dog price will lie in between the given interval, not a probability that the dog price will lie in the interval.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

For a given sample, an 90% confidence interval is narrower than a
95% confidence interval.

( ) True
( ) False

# BEGIN SOLUTION

**Answer: ** True

The more narrow an interval is, the less confident one is that the true statistic lies within that interval.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

If you tried to bootstrap your sample 1,000 times but accidentally
sampled **without** replacement, the standard deviation of
your test statistics is always equal to 0.

( ) True
( ) False

# BEGIN SOLUTION

**Answer: True

Note that bootstrapping form a sample **without** replacement just means that we're drawing the same sample over and over again. So the resulting test statistic will be the same between each sample, and thus the std of the test statistic is 0.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

You run a permutation test and store 500 simulated test statistics
in an array called `stats`. You can construct a 95%
confidence interval by finding the 2.5th and 97.5th percentiles of
`stats`.

( ) True
( ) False

# BEGIN SOLUTION

**Answer: ** False

False, to calculate a 95 percent confidence interval, we use bootstrapping to add variation to our samples. 

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

The distribution of sample proportions is roughly normal for large samples because of the Central Limit Theorem.

( ) True
( ) False

# BEGIN SOLUTION

**Answer: ** True

This is just the definition of Central Limit Theorem.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

The 20th percentile of the sequence [10, 30, 50, 40, 9, 70] is 30.

( ) True
( ) False

# BEGIN SOLUTION

**Answer: ** False

To calculate percentile, we take 20 / 100 * 6, which gives us the ordinal rank of 6/5. Now we take the next largest integer ordinal rank which is 2. And since 10 has an ordinal rank of 2 in the data set, the 20th percentile value of the data set is 10.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Chebyshev's inequality implies that we can always create a 96%
confidence interval from a bootstrap distribution using
the mean of the distribution plus or minus 5 standard deviations.

# BEGIN SOLUTION

**Answer: ** True

By Chebyshev's theorem, at most `1 - 1 / z^2` of the data is within `z` STD of the mean. Thus `1 - 1 / 5^2 = 0.96` of the data is within 5 STD of the mean. 

# END SOLUTION

# END SUBPROB

# END PROB
