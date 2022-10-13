# BEGIN PROB
Suppose you want to estimate the proportion of UCSD students that love
dogs using a survey with a yes/no question. If you poll 400 students,
what is the widest possible width for a 95% confidence interval?

( ) 0.01
( ) 0.05
( ) 0.1
( ) 0.2
( ) 0.5
( ) None of the above

# BEGIN SOLUTION
**Answer: ** Option 3: 0.01

Recall that a 95% confidence interval of a sample mean is given by `[sample mean - 2 * (sample std / np.sqrt(sample size)), sample mean -+ 2 * (sample std / np.sqrt(sample size))]`. Using this, we realize that the width of a 95% confidence interval is approximately `4 * (sample std / np.sqrt(sample size))`. Now, the sample size is already constat, which was given to be 400. However, we can attempt to maximize the `sample std`. Without loss of generality, assume that a "yes" vote has a value of 1 and "no" vote has a value of 0 (to make calculations easier). It's not hard to see that the maximum std we could achieve is buy recieving an equal number of yes/no votes (aka 200 of each vote). The standard deviation in this case is just 0.5, and so the widest possible width for a 95% confidence interval is just `4 * 0.5/np.sqrt(200)` which evaluates to 0.1. (Note that we chose yes and no to be 1 and 0 so that we wouldn't have to standardize the values. Had you chosen other values, you may or may not have had to do an extra step of standardizing the data).

# END SOLUTION

# END PROB
