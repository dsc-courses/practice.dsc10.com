# BEGIN PROB

At the San Diego Model Railroad Museum, there are different admission prices for children, adults, and seniors. Over a period of time, as tickets are sold, employees keep track of how many of each type of ticket are sold. These ticket counts (in the order child, adult, senior) are stored as follows.

```py
admissions_data = np.array([550, 1550, 400])
```

# BEGIN SUBPROB

Complete the code below so that it creates an array `admissions_proportions` with the proportions of tickets sold to each group (in the order child, adult, senior).

```py
def as_proportion(data):
    return __(a)__

admissions_proportions = as_proportion(admissions_data)
```

What goes in blank (a)?

# BEGIN SOLUTION

**Answer:** `data/data.sum()`

To calculate proportion for each group, we divide each value in the array (tickets sold to each group) by the sum of all values (total tickets sold). Remember values in an array can be processed as a whole.

<average>95</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

The museum employees have a model in mind for the proportions in which they sell tickets to children, adults, and seniors. This model is stored as follows.

```py
model = np.array([0.25, 0.6, 0.15])
```

We want to conduct a hypothesis test to determine whether the admissions data we have is consistent with this model. Which of the following is the null hypothesis for this test?

( ) Child, adult, and senior tickets might plausibly be purchased in proportions 0.25, 0.6, and 0.15.
( ) Child, adult, and senior tickets are purchased in proportions 0.25, 0.6, and 0.15.
( ) Child, adult, and senior tickets might plausibly be purchased in proportions other than 0.25, 0.6, and 0.15.
( ) Child, adult, and senior tickets, are purchased in proportions other than 0.25, 0.6, and 0.15.

# BEGIN SOLUTION

**Answer:** Child, adult, and senior tickets are purchased in proportions 0.25, 0.6, and 0.15. (Option 2)

Recall, null hypothesis is the hypothesis that there is no significant difference between specified populations, any observed difference being due to sampling or experimental error. So, we assume the distribution is the same as the model.

<average>88</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Which of the following test statistics could we use to test our hypotheses? Select all that could work.

[ ] sum of differences in proportions
[ ] sum of squared differences in proportions
[ ] mean of differences in proportions
[ ] mean of squared differences in proportions
[ ] none of the above

# BEGIN SOLUTION

**Answer:** sum of squared differences in proportions, mean of squared differences in proportions (Option 2, 4)

We need to use squared difference to avoid the case that large positive and negative difference cancel out in the process of calculating sum or mean, resulting in small sum of difference or mean of difference that does not reflect the actual deviation. So, we eliminate Option 1 and 3.

<average>77</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Below, we'll perform the hypothesis test with a different test statistic, the mean of the absolute differences in proportions.

Recall that the ticket counts we observed for children, adults, and seniors are stored in the array `admissions_data  = np.array([550, 1550, 400])`, and that our model is `model = np.array([0.25, 0.6, 0.15])`.

For our hypothesis test to determine whether the admissions data is consistent with our model, what is the observed value of the test statistic? Input your answer as a decimal between 0 and 1. Round to three decimal places. (Suppose that the value you calculated is assigned to the variable `observed_stat`, which you will use in later questions.)

# BEGIN SOLUTION

**Answer:** 0.02

We first calculate the proportion for each value in `admissions_data`
$$\frac{550}{550+1550+400} = 0.22$$
$$\frac{1550}{550+1550+400} = 0.62$$
$$\frac{400}{550+1550+400} = 0.16$$
So, we have the distribution of the `admissions_data`

Then, we calculate the observed value of the test statistic (the mean of the absolute differences in proportions)
$$\frac{|0.22-0.25|+|0.62-0.6|+|0.16-0.15|}{number\ of\ goups}$$
$$=\frac{0.03+0.02+0.01}{3} = 0.02$$

<average>82</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Now, we want to simulate the test statistic 10,000 times under the assumptions of the null hypothesis. Fill in the blanks below to complete this simulation and calculate the p-value for our hypothesis test. Assume that the variables `admissions_data`, `admissions_proportions`, `model`, and `observed_stat` are already defined as specified earlier in the question.

```py
simulated_stats = np.array([]) 
for i in np.arange(10000):
    simulated_proportions = as_proportions(np.random.multinomial(__(a)__, __(b)__))
    simulated_stat = __(c)__
    simulated_stats = np.append(simulated_stats, simulated_stat)

p_value = __(d)__
```

What goes in blank (a)? 
What goes in blank (b)? 
What goes in blank (c)? 
What goes in blank (d)? 

# BEGIN SOLUTION

**Answer:** (a) `admissions_data.sum()` (b) `model` (c) `np.abs(simulated_proportions - model).mean()` (d) `np.count_nonzero(simulated_stats >= observed_stat) / 10000`

Recall, in `np.random.multinomial(n, [p_1, ..., p_k])`, `n` is the number of experiments, and `[p_1, ..., p_k]` is a sequence of probability. The method returns an array of length k in which each element contains the
number of occurrences of an event, where the probability of the
ith event is `p_i`.  

We want our `simulated_proportion` to have the same data size as `admissions_data`, so we use `admissions_data.sum()` in (a). 

Since our null hypothesis is based on `model`, we simulate based on distribution in `model`, so we have `model` in (b). 

In (c), we compute the mean of the absolute differences in proportions. `np.abs(simulated_proportions - model)` gives us a series of absolute differences, and `.mean()` computes the mean of the absolute differences.

In (d), we calculate the `p_value`. Recall, the `p_value` is the chance, under the null hypothesis, that the test statistic is equal to the value that was observed in the data or is even further in the direction of the alternative. `np.count_nonzero(simulated_stats >= observed_stat)` gives us the number of `simulated_stats` greater than or equal to the `observed_stat` in the 10000 times simulations, so we need to divide it by `10000` to compute the proportion of `simulated_stats` greater than or equal to the `observed_stat`, and this gives us the `p_value`.

<average>79</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

True or False: the p-value represents the probability that the null hypothesis is true.

( ) True
( ) False

# BEGIN SOLUTION

**Answer:** False

Recall, the p-value is the chance, under the null hypothesis, that the test statistic is equal to the value that was observed in the data or is even further in the direction of the alternative. It only gives us the strength of evidence in favor of the null hypothesis, which is different from "the probability that the null hypothesis is true". 

<average>64</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

The new statistic that we used for this hypothesis test, the mean of the absolute differences in proportions, is in fact closely related to the total variation distance. Given two arrays of length three, `array_1` and `array_2`, suppose we compute the mean of the absolute differences in proportions between `array_1` and `array_2` and store the result as `madp`. What value would we have to multiply `madp` by to obtain the total variation distance  `array_1` and `array_2`? Input your answer below, rounding to three decimal places.

# BEGIN SOLUTION

**Answer:** 1.5

Recall, the total variation distance (TVD) is the sum of the absolute differences in proportions, divided by 2. When we compute the mean of the absolute differences in proportions, we are computing the sum of the absolute differences in proportions, divided by the number of groups (which is 3). Thus, to get TVD, we first multiply our current statistics (the mean of the absolute differences in proportions) by 3, we get the sum of the absolute differences in proportions. Then according to the definition of TVD, we divide this value by 2. Thus, we have $\text{current statistics}\cdot 3 / 2 = \text{current statistics}\cdot 1.5$.

<average>65</average>

# END SOLUTION

# END SUBPROB

# END PROB