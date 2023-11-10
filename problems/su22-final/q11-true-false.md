# BEGIN PROB
Answer the following true/false questions.

# BEGIN SUBPROB

<span style="color:red"><b>Note: This problem is out of scope; it covers material no longer included in the course.</b></span>

When John Snow took off the handle from the Broad Street pump, the
number of cholera deaths decreased. Because of this, he could
conclude that cholera was caused by dirty water.

( ) True
( ) False

# BEGIN SOLUTION

**Answer: ** False

There are a couple details that the problem fails to convey and that we cannot assume. 1) Do we even know that the pump he removed was the only pump with dirty water? 2) Do we know that people even drank/took water from the Broad Street pump? 3) Do we even know what kinds of people drank from the Broad Street pump? We need to eliminate all confounding factors, otherwise, it might be difficult to identify causality.

<average>91</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

If you get a p-value of 0.009 using a permutation test, you can
conclude causality.

( ) True
( ) False

# BEGIN SOLUTION

**Answer: ** False

Permutation tests don't prove causality. Remember, we use the permutation test and calculate a p-value to simply reject a null hypothesis, not to prove the alternative hypothesis.

<average>91</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

`df.groupby("kind").mean()` will have 5 columns.

( ) True
( ) False

# BEGIN SOLUTION

**Answer: ** True

Referring to `df` at the beginning of the exam, we could see that 5 of the columns have numerical values as inputs, and thus `df.groupby("kind").mean()` will return the mean of these 5 numerical columns

<average>74</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

If the 95% confidence interval for dog price is [650, 900], there
is a 95% chance that the population dog price is between $650 and
$900.

# BEGIN SOLUTION

**Answer: ** False

Recall, what a k% confidence level states is that approximately k% of the time, the intervals you create through this process will contain the true population parameter. In this case, the confidence interval states that approximately 95% of the time, the intervals you create through this process will contain the population dog price. However, it will be false if we state it in the reverse order since our population parameter is already fixed. 

<average>66</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

For a given sample, an 90% confidence interval is narrower than a
95% confidence interval.

( ) True
( ) False

# BEGIN SOLUTION

**Answer: ** True

The more narrow an interval is, the less confident one is that the intervals one creates will contain the true population parameter.

<average>91</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

If you tried to bootstrap your sample 1,000 times but accidentally
sampled **without** replacement, the standard deviation of
your test statistics is always equal to 0.

( ) True
( ) False

# BEGIN SOLUTION

**Answer: ** True

Note that bootstrapping form a sample **without** replacement just means that we're drawing the same sample over and over again. So the resulting test statistic will be the same between each sample, and thus the std of the test statistic is 0.

<average>86</average>

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

<average>40</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

The distribution of sample proportions is roughly normal for large samples because of the Central Limit Theorem.

( ) True
( ) False

# BEGIN SOLUTION

**Answer: ** True

This is just the definition of Central Limit Theorem.

<average>43</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

<span style="color:red"><b>Note: This problem is out of scope; it covers material no longer included in the course.</b></span>

The 20th percentile of the sequence [10, 30, 50, 40, 9, 70] is 30.

( ) True
( ) False

# BEGIN SOLUTION

**Answer: ** False

Recall, we find the $p$th percentile in 4 steps: 

1. Sort the collection in increasing order.
[9, 10, 30, 40, 50, 70]

2. Define $h$ to be $p\%$ of $n$: 
$$h = \frac p{100} \cdot n$$
$$h = \frac {20}{100} \cdot 6 = 1.2$$

3. If $h$ is an integer, define $k = h$. Otherwise, let $k$ be the smallest integer greater than $h$.
Since h (which is 1.2) is not an integer, so $k$ is 2

4. Take the $k$th element of the sorted collection (start counting from 1, not 0).
Since 10 has an ordinal rank of 2 in the data set, the 20th percentile value of the data set is 10, not 30.

<average>66</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Chebyshev's inequality implies that we can always create a 96%
confidence interval from a bootstrap distribution using
the mean of the distribution plus or minus 5 standard deviations.

# BEGIN SOLUTION

**Answer: ** True

By Chebyshev's theorem, at least `1 - 1 / z^2` of the data is within `z` STD of the mean. Thus at least `1 - 1 / 5^2 = 0.96` of the data is within 5 STD of the mean. 

<average>51</average>

# END SOLUTION

# END SUBPROB

# END PROB
