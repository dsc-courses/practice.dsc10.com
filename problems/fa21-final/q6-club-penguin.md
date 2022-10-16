# BEGIN PROB

Researchers from the San Diego Zoo, located within Balboa Park, collected physical measurements of several species of penguins in a region of Antarctica. 

One piece of information they tracked for each of 330 penguins was its mass in grams. The average penguin mass is 4200 grams, and the standard deviation is 840 grams.

# BEGIN SUBPROB

Consider the histogram of mass below.

<center><img src='../assets/images/fa21-final/mass.png' width=40%></center>

Select the true statement below.

( ) The median mass of penguins is larger than the average mass of penguins
( ) The median mass of penguins is roughly equal to the average mass of penguins (within 50 grams)
( ) The median mass of penguins is less than the average mass of penguins
( ) It is impossible to determine the relationship between the median and average mass of penguins just by looking at the above histogram

# BEGIN SOLUTION

**Answer: ** The median mass of penguins is less than the average mass of penguins

This is a distribution that skewed to the right, so mean is greater than median.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Which of the following is a valid conclusion that we can draw solely from the histogram above?

( ) The number of penguins with a mass of exactly 3500 grams is greater than the number of penguins with a mass of exactly 5500 grams.
( ) The number of penguins with a mass of at most 3500 grams is greater than the number of penguins with a mass of at least 5500 grams.
( ) There is an odd number of penguins in the dataset.
( ) The number penguins with a mass of exactly 4000 grams is greater than zero.
( ) None of the above.

# BEGIN SOLUTION

**Answer: ** The number of penguins with a mass of at most 3500 grams is greater than the number of penguins with a mass of at least 5500 grams.

Recall, a histogram has intervals on axis, so we cannot know the frequency of an exact value. Thus, we cannot conclude statement 1, 3, 4. Since the frequency of an exact value is unkown, for statement 3, it is possible that all numbers we have in this distribution are even. Although in the graph, we are only given frequency rather than number, we can justify statement 2 by comparing the sum of frequency in the left side of 3500, and the sum of frequency in the right side of 5500. You can either estimate by visually compare the areas of both parts or compute the sum of both sides by estimating the bars' height.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

For your convenience, we show the histogram of mass again below.

<center><img src='../assets/images/fa21-final/mass.png' width=40%></center>

Recall, there are 330 penguins in our dataset. Their average mass is 4200 grams, and the standard deviation of mass is 840 grams.

Per Chebyshev's inequality, at least what percentage of penguins have a mass between 3276 grams and 5124 grams? Input your answer as a percentage between 0 and 100, without the % symbol. Round to three decimal places.

# BEGIN SOLUTION

**Answer: ** 17.355

Recall, Chebyshev's inequality states that No matter what the shape of the distribution is, the proportion of values in the range “average ± z SDs” is  **at least** $1 - \frac{1}{z^2}$.

To approach the problem, we'll start by converting 3276 grams and 5124 grams to standard units. Doing so yields $\frac{3276 - 4200}{840} = -1.1$, similarly, $\frac{5124 - 4200}{840} = 1.1$. This means that 3276 is 1.1 standard deviations **below** the mean, and 5124 is 1.1 standard deviations **above** the mean. Thus, we are calculating the proportion of values in the range “average ± 1.1 SDs”. 

When $z = 1.1$, we have $1 - \frac{1}{z^2} = 1 - \frac{1}{1.1^2} \approx 0.173553719$, which as a percentage rounded to three decimal places is $17.355\%$.

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

**Answer: ** 75%

Recall, Chebyshev's inequality states that No matter what the shape of the distribution is, the proportion of values in the range “average ± z SDs” is  **at least** $1 - \frac{1}{z^2}$.

To approach the problem, we'll start by converting 3276 grams and 5124 grams to standard units. Doing so yields $\frac{1680 - 4200}{840} = -3$, similarly, $\frac{5880 - 4200}{840} = 2$. This means that 1680 is 3 standard deviations **below** the mean, and 5880 is 2 standard deviations **above** the mean. Thus, we are calculating the proportion of values in the range “average - 3 SDs and average + 2 SDs”. 

When $z = -3$, we have $\frac{1 - \frac{1}{z^2}}{2} = \frac{1 - \frac{1}{3^2}}{2} = \frac{1-\frac{1}{9}}{2} = \frac{4}{9}$. (Remember we have to divide the percentage by 2 since we are only computing one side of the mean. In other words, half of the range.) When $z = +2$, we have $\frac{1 - \frac{1}{z^2}}{2} = \frac{1 - \frac{1}{2^2}}{2} = \frac{1-\frac{1}{4}}{2} = \frac{3}{8}$. We sum the percentage together, $\frac{4}{9}+\frac{3}{8}=\frac{32+27}{72} \approx 0.819444$, which as a percentage rounded to one decimal places is $81.9\%$.

In our options, 75% < 81.9%, 88.8% > 81.9%. Thus, **at least** $75\%$ of penguins have a mass between 1680 grams and 5880 grams.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

The distribution of mass in grams is not roughly normal. Is the distribution of mass in standard units roughly normal?

( ) Yes
( ) No
( ) Impossible to tell

# BEGIN SOLUTION

**Answer: ** No

The shape of the distribution does not change since we are scaling the x values for all data.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Suppose all 330 penguin body masses (in grams) that the researchers collected are stored in an array called `masses`. We'd like to estimate the probability that two different randomly selected penguins from our dataset have body masses within 50 grams of one another (including a difference of exactly 50 grams). Fill in the missing pieces of the simulation below so that the function `estimate_prob_within_50g` returns an estimate for this probability.

```py
def estimate_prob_within_50g():
    num_reps = 10000
    within_50g_count = 0
    for i in np.arange(num_reps):
        two_penguins = np.random.choice(__(a)__)
        if __(b)__:
            within_50g_count = within_50g_count + 1
    return within_50g_count / num_reps
```

What goes in blank (a)? ____
What goes in blank (b)? ____

# BEGIN SOLUTION

**Answer: ** (a) `masses, 2, replace=False` (b) `abs(two_penguins[0] - two_penguins[1])<=50`

(a) Recall, `np.random.choice( )` can have three parameters `array, n, replace=False`, and returns n elements from the array at random, without replacement. We are randomly choosing **2 different** penguins from the `masses` **array**, so we are using `np.random.choice( )` without repalcement.
(b) We want to count the number of pairs of penguins that have body masses difference within 50 grams, so we are using the index to access the two penguins generated from `two_penguins` and caculating their absolute difference with `abs()`. And in this `if` condition, we only want to have penguins with absolute difference less than or equal to 50, so we write a `<=` condition to justify whether the generated pairs of penguins fulfill this requirement.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Recall, there are 330 penguins in our dataset. Their average mass is 4200 grams, and the standard deviation of mass is 840 grams. Assume that the 330 penguins in our dataset are a random sample from the population of all penguins in Antarctica. Our sample gives us one estimate of the population mean.

To better estimate the population mean, we bootstrapped our sample and plotted a histogram of the resample means, then took the middle 68 percent of those values to get a confidence interval. Which option below shows the histogram of the resample means and the confidence interval we found?

<center><img src='../assets/images/fa21-final/option1.png' width=40%></center>

<center><img src='../assets/images/fa21-final/option2.png' width=40%></center>

<center><img src='../assets/images/fa21-final/option3.png' width=40%></center>

<center><img src='../assets/images/fa21-final/option4.png' width=40%></center>

( ) Option 1
( ) Option 2
( ) Option 3
( ) Option 4


# BEGIN SOLUTION

**Answer: ** Option 2

Recall, the distribution of sample mean is roughly normal and centered at the **population mean** (which is not necessarily our sample mean which is 4200). Thus, we eliminate **Option 1**

To compute the SD of the sample mean's distribution, when we don't know the population's SD, we can use the sample's SD (840):
$$\text{SD of Distribution of Possible Sample Means} \approx \frac{\text{Sample SD}}{\sqrt{\text{sample size}}} = \frac{840}{\sqrt{330}} \approx 46.24$$

Recall: proportion with $z$ SDs of the mean

|Percent in Range | All Distributions (via Chebyshev's Inequality) | Normal Distributions|
|---|---|---|
|$\text{average} \pm 1 \ \text{SD}$ | $\geq 0\%$ | $\approx 68\%$ |
|$\text{average} \pm 2\text{SDs}$ | $\geq 75\%$ | $\approx 95\%$ |
|$\text{average} \pm 3\text{SDs}$ | $\geq 88\%$ | $\approx 99.73\%$ |

In this question, we want 68% confidence interval, given that the distribution of sample mean is roughly normal, our CI should have range $\text{population mean} \pm 1 \ \text{SD}$. Thus, the interval is approximately $46.24-(-46.24)=92.48$.
We compare the 68% CI in Option 2, 3, 4, and we choose **Option 2** since it has a 68% CI with an interval approximates to 92.48. (There is 3.5 bars between 4150 and 4200, so 1 bar is about $50/3.5 \approx 14$ width. There is about 6.5 bars within 68% CI in Option 2, so we have $6.5 \cdot 14 = 91$)

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Suppose `boot_means` is an array of the resampled means. Fill in the blanks below so that `[left, right]` is a 68% confidence interval for the true mean mass of penguins.

```py
left = np.percentile(boot_means, __(a)__)
right = np.percentile(boot_means, __(b)__)
[left, right]
```
What goes in blank (a)? ____
What goes in blank (b)? ____

# BEGIN SOLUTION

**Answer: ** (a) 16 (b) 84

Recall, `np.percentile(array, p)` computes the `p`th percentile of the numbers in `array`. To compute the 68% CI, we need to know the percentile of left tail and right tail. 

left percentile = $(1-0.68)/2 = (0.32)/2 = 0.16$ so we have 16th percentile

right percentile = $1-((1-0.68)/2) = 1-((0.32)/2) = 1-0.16 = 0.84$ so we have 84th percentile

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

**Answer: ** Option 4 (If we created many confidence intervals using the same method, approximately 68% of them would contain the mean weight of all penguins in Antarctica.)

Recall, what a $k$% confidence level states is that approximately $k$% of the time, the intervals you create through this process will contain the true population parameter.

In this question, our population parameter is the mean weight of all penguins in Antarctica. So 86% of the time, the intervals you create through this process will contain the the mean weight of all penguins in Antarctica. This is the same as Option 4. However, it will be false if we state it in the reverse order (Option 1) since our population parameter is already fixed.

# END SOLUTION

# END SUBPROB

# END PROB