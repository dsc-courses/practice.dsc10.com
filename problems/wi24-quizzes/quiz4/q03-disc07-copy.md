# BEGIN PROB

The Oscars, or Academy Awards, are the highest awards in the film
industry, awarded each year to the best movies of that year. The
`oscars` DataFrame contains a row for each movie that has ever been
nominated for an Oscar. The `"name"` column contains the name of the
movie and the `"rating"` column contains a rating of the movie on a 0 to
100 scale. This number incorporates many factors, but we won't worry
about how it is computed.

<center><img src="../../assets/images/wi24-quizzes/oscar.png" width=700></center>

# BEGIN SUBPROB

Fill in the blanks below to collect a **simple random sample** of 400
movies from the `oscars` DataFrame, then calculate 10,000 bootstrapped
sample mean ratings.

    my_sample = __(x)__
    n_resamples = 10000
    boot_means = np.array([])
    for i in np.arange(n_resamples):
        resample = __(y)__
        mean = __(z)__
        boot_means = np.append(boot_means, mean)


# BEGIN SOLUTION

**Answer (x):** `oscars.sample(400)`

<average>85</average>

**Answer (y):** `my_sample.sample(400, replace=True)`

<average>87</average>

**Answer (z):** `resample.get("rating").mean()`

<average>96</average>
# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

In each blank, circle the word that correctly fills in the sentence.\

*A histogram of `boot_means` shows a(n) **probability** / **empirical** distribution of a **statistic** / **parameter**.*

# BEGIN SOLUTION
**Answer:** empirical, statistic

<average>77</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Suppose we use the array `boot_means` to calculate a 90% confidence
interval for the mean rating of Oscar-nominated movies. **Select all**
correct conclusions we can draw about this interval.

[ ] There is a 90% chance that the true mean rating of all Oscar-nominated movies falls within this interval.
[ ] The sample mean rating is within 90% of the true mean rating of all Oscar-nominated movies.
[ ] If we looked at the ratings of many Oscar-nominated movies, about 90% of them would fall within this range.
[ ] None of the above.

# BEGIN SOLUTION
**Answer:** None of the above.

<average>74</average>

# END SOLUTION

# END SUBPROB

# END PROB