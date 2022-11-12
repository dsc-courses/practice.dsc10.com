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
**Answer: ** Option 3: 0.1

Since, we're looking at a proportion of UCSD students that love dogs, we'll set a "yes" vote to a value of 1 and a "no" vote to a value of 0. (Try to see why this makes the mean of "yes"/"no" votes also the proportion of "yes" votes). Also by central limit theorem, the distribution of the sample mean is approximately normal. Now recall that a 95% confidence interval of a sample mean is given by `[sample mean - 2 * (sample std / np.sqrt(sample size)), sample mean + 2 * (sample std / np.sqrt(sample size))]`. As a result, we realize that the width of a 95% confidence interval is `4 * (sample std / np.sqrt(sample size))`. Now, the sample size is already constant, which was given to be 400. However, we can attempt to maximize the `sample std`. It's not hard to see that the maximum std we could achieve is by recieving an equal number of yes/no votes (aka 200 of each vote). Calculating the standard deviation in this case is just 0.5*, and so the widest possible width for a 95% confidence interval is just `4 * 0.5/np.sqrt(400)` which evaluates to 0.1. 

*To make the calculation of the standard deviation faster, try to see why calculating the std of a dataset with 200 1's and 200 0's is the same as calculating the std of a data set with only a single 1 and a single 0.

<average>34</average>

# END SOLUTION

# END PROB
