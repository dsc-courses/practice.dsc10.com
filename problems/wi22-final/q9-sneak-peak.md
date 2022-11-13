# BEGIN PROB

For your convenience, we show the first few rows of `season` again below.

<center><img src='../assets/images/wi22-final/seasons.png' width=40%></center>

In the past three problems, we presumed that we had access to the entire `season` DataFrame. Now, suppose we only have access to the DataFrame `small_season`, which is a random sample of **size 36** from `season`. We're interested in learning about the true mean points per game of all players in `season` given just the information in `small_season`.

To start, we want to bootstrap `small_season` 10,000 times and compute the mean of the resample each time. We want to store these 10,000 bootstrapped means in the array `boot_means`.

Here is a broken implementation of this procedure.

```py
boot_means = np.array([])                                           
for i in np.arange(10000):                                          
    resample = small_season.sample(season.shape[0], replace=False)  # Line 1
    resample_mean = small_season.get('PPG').mean()                  # Line 2
    np.append(boot_means, new_mean)                                 # Line 3
```

For each of the 3 lines of code above (marked by comments), specify what is incorrect about the line by selecting one or more of the corresponding options below. Or, select "Line _ is correct as-is" if you believe there's nothing that needs to be changed about the line in order for the above code to run properly.

# BEGIN SUBPROB

What is incorrect about Line 1? Select all that apply.

[ ] Currently the procedure samples from `small_season`, when it should be sampling from `season`
[ ] The sample size is `season.shape[0]`, when it should be `small_season.shape[0]`
[ ] Sampling is currently being done without replacement, when it should be done with replacement
[ ] Line 1 is correct as-is

# BEGIN SOLN

**Answers:**

- The sample size is `season.shape[0]`, when it should be `small_season.shape[0]`
- Sampling is currently being done without replacement, when it should be done with replacement

Here, our goal is to bootstrap from `small_season`. When bootstrapping, we **sample with replacement** from our original sample, with a sample size that's equal to the original sample's size. Here, our original sample is `small_season`, so we should be taking samples of size `small_season.shape[0]` from it.

Option 1 is incorrect; `season` has nothing to do with this problem, as we are bootstrapping from `small_season`.

<average>95</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

What is incorrect about Line 2? Select all that apply.

[ ] Currently it is taking the mean of the `'PPG'` column in `small_season`, when it should be taking the mean of the `'PPG'` column in `season`
[ ] Currently it is taking the mean of the `'PPG'` column in `small_season`, when it should be taking the mean of the `'PPG'` column in `resample`
[ ] `.mean()` is not a valid Series method, and should be replaced with a call to the function `np.mean`
[ ] Line 2 is correct as-is

# BEGIN SOLN

**Answer:** Currently it is taking the mean of the `'PPG'` column in `small_season`, when it should be taking the mean of the `'PPG'` column in `resample`

The current implementation of Line 2 doesn't use the `resample` at all, when it should. If we were to leave Line 2 as it is, all of the values in `boot_means` would be identical (and equal to the mean of the `'PPG'` column in `small_season`).

Option 1 is incorrect since our bootstrapping procedure is independent of `season`. Option 3 is incorrect because `.mean()` is a valid Series method.

<average>98</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

What is incorrect about Line 3? Select all that apply.

[ ] The result of calling `np.append` is not being reassigned to `boot_means`, so `boot_means` will be an empty array after running this procedure
[ ] The indentation level of the line is incorrect – `np.append` should be outside of the `for`-loop (and aligned with `for i`)
[ ] `new_mean` is not a defined variable name, and should be replaced with `resample_mean`
[ ] Line 3 is correct as-is

# BEGIN SOLN

**Answers:**

- The result of calling `np.append` is not being reassigned to `boot_means`, so `boot_means` will be an empty array after running this procedure
- `new_mean` is not a defined variable name, and should be replaced with `resample_mean`

`np.append` returns a new array and does not modify the array it is called on (`boot_means`, in this case), so Option 1 is a necessary fix. Furthermore, Option 3 is a necessary fix since `new_mean` wasn't defined anywhere.

Option 2 is incorrect; if `np.append` were outside of the `for`-loop, none of the 10,000 resampled means would be saved in `boot_means`.

<average>94</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Suppose we've now fixed everything that was incorrect about our bootstrapping implementation.

Recall from earlier in the exam that, in `season`, the mean number of points per game is 7, with a standard deviation of 5. 

It turns out that when looking at just the players in `small_season`, the mean number of points per game is 9, with a standard deviation of 4. Remember that `small_season` is a random sample of size 36 taken from `season`.

Which of the following histograms visualizes the empirical distribution of the sample mean, computed using the bootstrapping procedure above?

<center><img src='../assets/images/wi22-final/hist-grid.png' width=50%></center>

( ) Option 1
( ) Option 2
( ) Option 3
( ) Option 4

# BEGIN SOLN

**Answer:** Option 3

The key to this problem is knowing to use the Central Limit Theorem. Specifically, we know that if we collect many samples from a population with replacement, then the distribution of the sample means will be roughly normal with:

- a mean that is equal to the mean of the population
- a standard deviation that is $\frac{\text{SD of population}}{\sqrt{\text{sample size}}}$

Here, **the "population" is `small_season`**, because that is the sample we're repeatedly (re)sampling from. While `season` is actually the population, it is not seen at all in the bootstrapping process, so it doesn't directly influence the distribution of the bootstrapped sample means.

The mean of `small_season` is 9, and so is the distribution of bootstrapped sample means. The standard deviation of `small_season` is 4, so the square root law, the standard deviation of the distribution of bootstrapped sample means is $\frac{4}{\sqrt{36}} = \frac{4}{6} = \frac{2}{3}$. 

The answer now boils down to choosing the histogram that looks roughly normally distributed with a mean of 9 and a standard deviation of $\frac{2}{3}$. Options 1 and 4 can be ruled out right away since their means seem to be smaller than 9. To decide between Options 2 and 3, we can use the inflection point rule, which states that in a normal distribution, the inflection points occur at one standard deviation above and one standard deviation below the mean. (An inflection point is when a curve changes from opening upwards to opening downwards.) See the picture below for more details.

<center><img src='../assets/images/wi22-final/inflection.jpeg' width=60%></center>

Option 3 is the only distribution that appears to be centered at 9 with a standard deviation of $\frac{2}{3}$ (0.7 is close to $\frac{2}{3}$), so it must be the empirical distribution of the bootstrapped sample means.

<average>42</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

We construct a 95% confidence interval for the true mean points per game for all players by taking the middle 95% of the bootstrapped sample means.

```py
left_b = np.percentile(boot_means, 2.5)
right_b = np.percentile(boot_means, 97.5)
boot_ci = [left_b, right_b]
```

Select the most correct statement below.

( ) `(left_b + right_b) / 2` is exactly equal to the mean points per game in `season`.
( ) `(left_b + right_b) / 2` is not necessarily equal to the mean points per game in `season`, but is close.
( ) `(left_b + right_b) / 2` is exactly equal to the mean points per game in `small_season`.
( ) `(left_b + right_b) / 2` is not necessarily equal to the mean points per game in `small_season`, but is close.
( ) `(left_b _+ right_b) / 2` is not close to either the mean points per game in `season` or the mean points per game in `small_season`.

# BEGIN SOLN

**Answer:** `(left_b + right_b) / 2` is not necessarily equal to the mean points per game in `small_season`, but is close.

Normal-based confidence intervals are of the form $[\text{mean} - \text{something}, \text{mean} + \text{something}]$. In such confidence intervals, it is the case that the average of the left and right endpoints is exactly the mean of the distribution used to compute the interval.

However, **the confidence interval we've created is not normal-based**, rather it is bootstrap-based! As such, we can't say that anything is _exactly_ true; this rules out Options 1 and 3.

Our 95% confidence interval was created by taking the middle 95% of bootstrapped sample means. The distribution of bootstrapped sample means is **roughly** normal, and the normal distribution is symmetric (the mean and median are both equal, and represent the "center" of the distribution). This means that the middle of our 95% confidence interval should be roughly equal to the mean of the distribution of bootstrapped sample means. This implies that Option 4 is correct; the difference between Options 2 and 4 is that Option 4 uses `small_season`, which is the sample we bootstrapped from, while Option 2 uses `season`, which was not accessed at all in our bootstrapping procedure.

<average>62</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Instead of bootstrapping, we could also construct a 95% confidence interval for the true mean points per game by using the Central Limit Theorem.

Recall that, when looking at just the players in `small_season`, the mean number of points per game is 9, with a standard deviation of 4. Also remember that `small_season` is a random sample of size 36 taken from `season`.

**Using only the information that we have about `small_season`** (i.e. without using any facts about `season`), compute a 95% confidence interval for the true mean points per game.

What are the left and right endpoints of your interval? Give your answers as numbers rounded to 3 decimal places.

# BEGIN SOLN

**Answer:** $[7.667, 10.333]$

In a normal distribution, roughly 95% of values are within 2 standard deviations of the mean. The CLT tells us that the distribution of sample means is roughly normal, and in subpart 4 of this problem we already computed the SD of the distribution of sample means to be $\frac{2}{3}$.

So, our normal-based 95% confidence interval is computed as follows:

$$\begin{aligned} &[\text{mean of sample} - 2 \cdot \text{SD of distribution of sample means}, \text{mean of sample} + 2 \cdot \text{SD of distribution of sample means}] \\ &= [9 - 2 \cdot \frac{4}{\sqrt{36}}, 9 + 2 \cdot \frac{4}{\sqrt{36}}] \\ &= [9 - \frac{4}{3}, 9 + \frac{4}{3}] \\ &\approx \boxed{[7.667, 10.333]} \end{aligned}$$

<average>87</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Recall that the mean points per game in `season` is 7, which is not in the interval you found above (if it is, check your work!).

Select the true statement below.

( ) The 95% confidence interval we created in the previous subpart did not contain the true mean points per game, which means that the distribution of the sample mean is not normal.
( ) The 95% confidence interval we created in the previous subpart did not contain the true mean points per game, which means that the distribution of points per game in `small_season` is not normal.
( ) The 95% confidence interval we created in the previous subpart did not contain the true mean points per game. This is to be expected, because the Central Limit Theorem is only correct 95% of the time.
( ) The 95% confidence interval we created in the previous subpart did not contain the true mean points per game, but if we collected many original samples and constructed many 95% confidence intervals, then roughly 95% of them would contain the true mean points per game.
( ) The 95% confidence interval we created in the previous subpart did not contain the true mean points per game, but if we collected many original samples and constructed many 95% confidence intervals, then exactly 95% of them would contain the true mean points per game.

# BEGIN SOLN

**Answer:** The 95% confidence interval we created in the previous subpart did not contain the true mean points per game, but if we collected many original samples and constructed many 95% confidence intervals, then roughly 95% of them would contain the true mean points per game.

In a confidence interval, the confidence level gives us a level of confidence in **the process** used to create the confidence interval. If we repeat the process of collecting a sample from the population and using the sample to construct a c% confidence interval for the population mean, then **roughly** c% of the intervals we create should contain the population mean. Option 4 is the only option that corresponds to this interpretation; the others are all incorrect in different ways.

<average>87</average>

# END SOLN

# END SUBPROB

# END PROB