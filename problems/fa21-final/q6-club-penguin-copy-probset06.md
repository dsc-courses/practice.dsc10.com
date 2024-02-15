# BEGIN PROB

Researchers from the San Diego Zoo, located within Balboa Park, collected physical measurements of several species of penguins in a region of Antarctica. 

One piece of information they tracked for each of 330 penguins was its mass in grams. The average penguin mass is 4200 grams, and the standard deviation is 840 grams.

# BEGIN SUBPROB

Consider the histogram of mass below.

<center><img src='../assets/images/fa21-final/mass.png' width=40%></center>
<br>

Select the true statement below.

( ) The median mass of penguins is larger than the average mass of penguins
( ) The median mass of penguins is roughly equal to the average mass of penguins (within 50 grams)
( ) The median mass of penguins is less than the average mass of penguins
( ) It is impossible to determine the relationship between the median and average mass of penguins just by looking at the above histogram

# BEGIN SOLUTION

**Answer:** The median mass of penguins is less than the average mass of penguins

This is a distribution that is skewed to the right, so mean is greater than median.

<average>87</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

For your convenience, we show the histogram of mass again below.

<center><img src='../assets/images/fa21-final/mass.png' width=40%></center>
<br>

Recall, there are 330 penguins in our dataset. Their average mass is 4200 grams, and the standard deviation of mass is 840 grams.

Per Chebyshev's inequality, at least what percentage of penguins have a mass between 3276 grams and 5124 grams? Input your answer as a percentage between 0 and 100, without the % symbol. Round to three decimal places.

# BEGIN SOLUTION

**Answer:** 17.355

Recall, Chebyshev's inequality states that No matter what the shape of the distribution is, the proportion of values in the range “average ± z SDs” is  **at least** $1 - \frac{1}{z^2}$.

To approach the problem, we'll start by converting 3276 grams and 5124 grams to standard units. Doing so yields $\frac{3276 - 4200}{840} = -1.1$, similarly, $\frac{5124 - 4200}{840} = 1.1$. This means that 3276 is 1.1 standard deviations **below** the mean, and 5124 is 1.1 standard deviations **above** the mean. Thus, we are calculating the proportion of values in the range “average ± 1.1 SDs”. 

When $z = 1.1$, we have $1 - \frac{1}{z^2} = 1 - \frac{1}{1.1^2} \approx 0.173553719$, which as a percentage rounded to three decimal places is $17.355\%$.

<average>76</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Per Chebyshev's inequality, at least what percentage of penguins have a mass between 1680 grams and 5880 grams?

( ) 50%
( ) 55.5%
( ) 65.25%
( ) 68%
( ) 75%
( ) 88.8%
( ) 95%

# BEGIN SOLUTION

**Answer:** 75%

Recall: proportion with $z$ SDs of the mean

|Percent in Range | All Distributions (via Chebyshev's Inequality) | Normal Distributions|
|---|---|---|
|$\text{average} \pm 1 \ \text{SD}$ | $\geq 0\%$ | $\approx 68\%$ |
|$\text{average} \pm 2\text{SDs}$ | $\geq 75\%$ | $\approx 95\%$ |
|$\text{average} \pm 3\text{SDs}$ | $\geq 88\%$ | $\approx 99.73\%$ |


To approach the problem, we'll start by converting 3276 grams and 5124 grams to standard units. Doing so yields $\frac{1680 - 4200}{840} = -3$, similarly, $\frac{5880 - 4200}{840} = 2$. This means that 1680 is 3 standard deviations **below** the mean, and 5880 is 2 standard deviations **above** the mean. 

Proportion of values in [-3 SUs, 2 SUs] >= Proportion of values in [-2 SUs, 2 SUs] >= 75% (Since we cannot assume that the distribution is normal, we look at the **All Distributions (via Chebyshev's Inequality)** column for proportion).

Thus, **at least** 75% of the penguins have a mass between 1680 grams and 5880 grams.

<average>72</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

The distribution of mass in grams is not roughly normal. Is the distribution of mass in standard units roughly normal?

( ) Yes
( ) No
( ) Impossible to tell

# BEGIN SOLUTION

**Answer:** No

The shape of the distribution does not change since we are scaling the x values for all data.

<average>60</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Suppose `boot_means` is an array of the resampled means. Fill in the blanks below so that `[left, right]` is a 68% confidence interval for the true mean mass of penguins.

```py
left = np.percentile(boot_means, __(a)__)
right = np.percentile(boot_means, __(b)__)
[left, right]
```
What goes in blank (a)? 
What goes in blank (b)? 

# BEGIN SOLUTION

**Answer:** (a) 16 (b) 84

Recall, `np.percentile(array, p)` computes the `p`th percentile of the numbers in `array`. To compute the 68% CI, we need to know the percentile of left tail and right tail. 

left percentile = $(1-0.68)/2 = (0.32)/2 = 0.16$ so we have 16th percentile

right percentile = $1-((1-0.68)/2) = 1-((0.32)/2) = 1-0.16 = 0.84$ so we have 84th percentile

<average>94</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Which of the following is a correct interpretation of this confidence interval? Select all that apply.

[ ] There is an approximately 68% chance that mean weight of all penguins in Antarctica falls within the bounds of this confidence interval.
[ ] Approximately 68% of penguin weights in our sample fall within the bounds of this confidence interval.
[ ] Approximately 68% of penguin weights in the population fall within the bounds of this interval.
[ ] If we created many confidence intervals using the same method, approximately 68% of them would contain the mean weight of all penguins in Antarctica.
[ ] None of the above

# BEGIN SOLUTION

**Answer:** Option 4 (If we created many confidence intervals using the same method, approximately 68% of them would contain the mean weight of all penguins in Antarctica.)

Recall, what a $k$% confidence level states is that approximately $k$% of the time, the intervals you create through this process will contain the true population parameter.

In this question, our population parameter is the mean weight of all penguins in Antarctica. So 86% of the time, the intervals you create through this process will contain the mean weight of all penguins in Antarctica. This is the same as Option 4. However, it will be false if we state it in the reverse order (Option 1) since our population parameter is already fixed.

<average>81</average>

# END SOLUTION

# END SUBPROB

# END PROB