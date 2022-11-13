# BEGIN PROB

From a population with mean 500 and standard deviation 50, you collect a sample of size 100. The sample has mean 400 and standard deviation 40. You bootstrap this sample 10,000 times, collecting 10,000 resample means.

# BEGIN SUBPROB

Which of the following is the most accurate description of the mean of the distribution of the 10,000 bootstrapped means?

( ) The mean will be exactly equal to 400.
( ) The mean will be exactly equal to 500.
( ) The mean will be approximately equal to 400.
( ) The mean will be approximately equal to 500.
# BEGIN SOLUTION

**Answer: ** The mean will be approximately equal to 400.

The distribution of bootstrapped means' mean will be approximately 400 since that is the mean
of the sample and bootstrapping is taking many samples of the original sample. The mean will not be exactly 400 do to some
randomness though it will be very close. 

<average>54</average>
# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Which of the following is closest to the standard deviation of the distribution of the 10,000 bootstrapped means?

( ) 400
( ) 40
( ) 4
( ) 0.4
# BEGIN SOLUTION

**Answer: ** 4

To find the standard deviation of the distribution, we can take the sample standard deviation S divided by the square root of
the sample size. From plugging in, we get 40 / 10 = 4. 

<average>51</average>
# END SOLUTION

# END SUBPROB

# END PROB
