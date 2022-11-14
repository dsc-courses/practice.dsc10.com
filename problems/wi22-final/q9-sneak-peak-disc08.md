# BEGIN PROB

Suppose we only have access to the DataFrame `small_season`, which is a random sample of **size 36** from `season`. We're interested in learning about the true mean points per game of all players in `season` given just the information in `small_season`.

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

# END PROB