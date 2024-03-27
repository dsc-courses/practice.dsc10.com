# BEGIN PROB

We want to use `app_data` to estimate the average amount of time it takes to build an IKEA bed (any product in the `'bed'` category). Which of the following strategies would be an appropriate way to estimate this quantity? Select all that apply.

[ ] Query to keep only the beds. Then resample with replacement many times. For each resample, take the mean of the `'minutes'` column. Compute a 95% confidence interval based on those means.
[ ] Query to keep only the beds. Group by `'product'` using the mean aggregation function. Then resample with replacement many times. For each resample, take the mean of the `'minutes'` column. Compute a 95% confidence interval based on those means.
[ ] Resample with replacement many times. For each resample, first query to keep only the beds and then take the mean of the `'minutes'` column. Compute a 95% confidence interval based on those means.
[ ] Resample with replacement many times. For each resample, first query to keep only the beds. Then group by `'product'` using the mean aggregation function, and finally take the mean of the `'minutes'` column. Compute a 95% confidence interval based on those means.

# BEGIN SOLUTION

**Answer: ** Option 1

Only the first answer is correct. This is a question of parameter estimation, so our approach is to use bootstrapping to create many resamples of our original sample, computing the average of each resample. Each resample should always be the same size as the original sample. The first answer choice accomplishes this by querying first to keep only the beds, then resampling from the DataFrame of beds only. This means resamples will have the same size as the original sample. Each resample's mean will be computed, so we will have many resample means from which to construct our 95% confidence interval.

In the second answer choice, we are actually taking the mean twice. We first average the build times for all builds of the same product when grouping by product. This produces a DataFrame of different products with the average build time for each. We then resample from this DataFrame, computing the average of each resample. But this is a resample of products, not of product builds. The size of the resample is the number of unique products in `app_data`, not the number of reported product builds in `app_data`. Further, we get incorrect results by averaging numbers that are already averages. For example, if 5 people build bed A and it takes them each 1 hour, and 1 person builds bed B and it takes them 10 hours, the average amount of time to build a bed is $\frac{5*1+10}{6} = 2.5$. But if we average the times for bed A (1 hour) and average the times for bed B (5 hours), then average those, we get $\frac{1+5}{2} = 3$, which is not the same. More generally, grouping is not a part of the bootstrapping process because we want each data value to be weighted equally.

The last two answer choices are incorrect because they involve resampling from the full `app_data` DataFrame before querying to keep only the beds. This is incorrect because it does not preserve the sample size. For example, if `app_data` contains 1000 reported bed builds and 4000 other product builds, then the only relevant data is the 1000 bed build times, so when we resample, we want to consider another set of 1000 beds. If we resample from the full `app_data` DataFrame, our resample will contain 5000 rows, but the number of beds will be random, not necessarily 1000. If we query first to keep only the beds, then resample, our resample will contain exactly 1000 beds every time. As an added bonus, since we only care about beds, it's much faster to resample from a smaller DataFrame of beds only than it is to resample from all `app_data` with plenty of rows we don't care about.





 
<average>71</average>
# END SOLUTION

# END PROB