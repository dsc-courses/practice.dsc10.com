# BEGIN PROB
The DataFrame `apps` contains application data for a random sample of 1,000 applicants for a particular credit card from the 1990s. The `"age"` column contains the applicants' ages, in years, to the nearest twelfth of a year.

The credit card company that owns the data in `apps`, BruinCard, has decided not to give us access to the entire `apps` DataFrame, but instead just a random sample of 100 rows of apps called `hundred_apps`.

We are interested in estimating the mean age of all applicants in `apps` given only the data
in `hundred_apps`. The ages in `hundred_apps` have a mean of 35 and a standard deviation of 10.

# BEGIN SUBPROB
Give the endpoints of the CLT-based 95% confidence interval for the mean age of all applicants in `apps`, based on the data in `hundred_apps`.

# BEGIN SOLUTION

**Answer:** Left endpoint = 33, Right endpoint = 37

According to the Central Limit Theorem, the standard deviation of the distribution of the sample mean is $\frac{\text{sample SD}}{\sqrt{\text{sample size}}} = \frac{10}{\sqrt{100}} = 1$. Then using the fact that the distribution of the sample mean is roughly normal, since 95% of the area of a normal curve falls within two standard deviations of the mean, we can find the endpoints of the 95% CLT-based confidence interval as $35 - 2 = 33$ and $35 + 2 = 37$.


We can think of this as using the formula below:
$$
\left[\text{sample mean} - 2\cdot \frac{\text{sample SD}}{\sqrt{\text{sample size}}}, \: \text{sample mean} + 2\cdot \frac{\text{sample SD}}{\sqrt{\text{sample size}}}
\right].$$
Plugging in the appropriate quantities yields
$[35 - 2\cdot\frac{10}{\sqrt{100}}, 35 - 2\cdot\frac{10}{\sqrt{100}}] = [33, 37]$.

<average>67</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB
BruinCard reinstates our access to `apps` so that we can now easily
extract information about the ages of all applicants. We determine that,
just like in `hundred_apps`, the ages in `apps` have a mean of 35 and a
standard deviation of 10. This raises the question of how other samples
of 100 rows of `apps` would have turned out, so we compute $10,000$
sample means as follows.

```py
    sample_means = np.array([])
    for i in np.arange(10000):
        sample_mean = apps.sample(100, replace=True).get("age").mean()
        sample_means = np.append(sample_means, sample_mean)
```

Which of the following three visualizations best depict the distribution of `sample_means`?

<center><img src='../assets/images/fa22-final/3hist.png' width=45%></center>
<br>

# BEGIN SOLUTION

**Answer:** Option 1

As we found in the previous part, the distribution of the sample mean should have a standard deviation of 1. We also know it should be centered at the mean of our sample, at 35, but since all the options are centered here, that's not too helpful. Only Option 1, however, has a standard deviation of 1. Remember, we can approximate the standard deviation of a normal curve as the distance between the mean and either of the inflection points. Only Option 1 looks like it has inflection points at 34 and 36, a distance of 1 from the mean of 35.

If you chose Option 2, you probably confused the standard deviation of our original sample, 10, with the standard deviation of the distribution of the sample mean, which comes from dividing that value by the square root of the sample size.

<average>57</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Which of the following statements are guaranteed to be true? Select all that
apply.

[ ] We used bootstrapping to compute `sample_means`.
[ ] The ages of credit card applicants are roughly normally distributed.
[ ] A CLT-based 90% confidence interval for the mean age of credit card applicants, based on the data in hundred apps, would be narrower than the interval you gave in part (a).
[ ] The expression `np.percentile(sample_means, 2.5)` evaluates to the left endpoint of the interval you gave in part (a).
[ ] If we used the data in `hundred_apps` to create 1,000 CLT-based 95% confidence intervals for the mean age of applicants in `apps`, approximately 950 of them would contain the true mean age of applicants in `apps`.
[ ] None of the above.


# BEGIN SOLUTION


**Answer:** A CLT-based 90% confidence interval for the mean age of credit card applicants, based on the data in `hundred_apps`, would be narrower than the interval you gave in part (a).

Let's analyze each of the options:

- Option 1: We are not using bootstrapping to compute sample means since we are sampling from the `apps` DataFrame, which is our population here. If we were bootstrapping, we'd need to sample from our first sample, which is `hundred_apps`.

- Option 2: We can't be sure what the distribution of the ages of credit card applicants are. The Central Limit Theorem says that the distribution of `sample_means` is roughly normally distributed, but we know nothing about the population distribution.

- Option 3: The CLT-based 95% confidence interval that we calculated in part (a) was computed as follows: 
$$\left[\text{sample mean} - 2\cdot \frac{\text{sample SD}}{\sqrt{\text{sample size}}},
\text{sample mean} + 2\cdot \frac{\text{sample SD}}{\sqrt{\text{sample size}}}
\right]$$
A CLT-based 90% confidence interval would be computed as 
$$\left[\text{sample mean} - z\cdot \frac{\text{sample SD}}{\sqrt{\text{sample size}}},
\text{sample mean} + z\cdot \frac{\text{sample SD}}{\sqrt{\text{sample size}}}
\right]$$
for some value of $z$ less than 2. We know that 95% of the area of a normal curve is within two standard deviations of the mean, so to only pick up 90% of the area, we'd have to go slightly less than 2 standard deviations away. This means the 90% confidence interval will be narrower than the 95% confidence interval.

- Option 4: The left endpoint of the interval from part (a) was calculated using the Central Limit Theorem, whereas using `np.percentile(sample_means, 2.5)` is calculated empirically, using the data in `sample_means`. Empirically calculating a confidence interval doesn't necessarily always give the exact same endpoints as using the Central Limit Theorem, but it should give you values close to those endpoints. These values are likely very similar but they are not guaranteed to be the same. One way to see this is that if we ran the code to generate `sample_means` again, we'd probably get a different value for `np.percentile(sample_means, 2.5)`.

- Option 5: The key observation is that if we used the data in `hundred_apps` to create 1,000 CLT-based 95% confidence intervals for the mean age of applicants in `apps`, all of these intervals would be exactly the same. Given a sample, there is only one CLT-based 95% confidence interval associated with it. In our case, given the sample `hundred_apps`, the one and only CLT-based 95% confidence interval based on this sample is the one we found in part (a). Therefore if we generated 1,000 of these intervals, either they would all contain the parameter or none of them would. In order for a statement like the one here to be true, we would need to collect 1,000 different samples, and calculate a confidence interval from each one.

<average>49</average>

# END SOLUTION
# END SUBPROB
# END PROB
