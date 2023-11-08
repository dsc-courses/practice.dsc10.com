# BEGIN PROB

Given below is the `season` DataFrame, which contains statistics on all players in the WNBA in the 2021 season. The first few rows of `season` are shown below:

<center><img src='../assets/images/wi22-final/seasons.png' width=40%></center>

Each row in season corresponds to a single player. In this problem, we'll be looking at the `'PPG'` column, which records the number of points scored per game played.

Now, suppose we only have access to the DataFrame `small_season`, which is a random sample of **size 36** from `season`. We're interested in learning about the true mean points per game of all players in `season` given just the information in `small_season`.

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

We construct a 95% confidence interval for the true mean points per game for all players by taking the middle 95% of the bootstrapped sample means.

```python
left_b = np.percentile(boot_means, 2.5)
right_b = np.percentile(boot_means, 97.5)
boot_ci = [left_b, right_b]         
```

We find that `boot_ci` is the interval [7.7, 10.3]. However, the mean points per game in `season` is 7, which is not in the interval we found. Which of the following statements is true? (Select all question)

[ ] 95% of games in `season` have a number of points between 7.7 and 10.3.
[ ] 95% of values in `boot_means` fall between 7.7 and 10.3.
[ ] There is a 95% chance that the true mean points per game is between 7.7 and 10.3.
[ ] The interval we created did not contain the true mean points per game, but if we collected many original samples and constructed many 95% confidence intervals, then exactly 95% of them would contain the true mean points per game.
[ ] The interval we created did not contain the true mean points per game, but if we collected many original samples and constructed many 95% confidence intervals, then roughly 95% of them would contain the true mean points per game.


# BEGIN SOLN

**Answers:** 

- 95% of values in `boot_means` fall between the endpoints of the interval we found. 
- The interval we created did not contain the true mean points per game, but if we collected many original samples and constructed many 95% confidence intervals, then roughly 95% of them would contain the true mean points per game.

The first option is incorrect because the confidence interval describes what we think the *mean* points per game could be. Individual games likely have a very large variety in the number of points scores. Probably very few have between 7.7 and 10.3 points.

The second option is correct because this is precisely how we calculated the endpoints of our interval, by taking the middle 95% of values in `boot_means`.

The third option is incorrect because we know the true mean points per game - it's 7. 7 does not fall in the interval 7.7 to 10.3, and we can say that with certainty. This is not a probability statement because the interval and the parameter are both fixed.

The fourth option is incorrect because of the word *exactly*. We generally can't make guarantees like this when working with randomness. 

The fifth option is correct, as this is the meaning of confidence. We have confidence in the process of generating 95% confidence intervals, because roughly 95% of such intervals we create will capture the parameter of interest.

<!-- <average>87</average> -->

# END SOLN

# END SUBPROB

# END PROB