# BEGIN PROB

You are browsing the IKEA showroom, deciding whether to purchase the BILLY bookcase or the LOMMARP bookcase. You are concerned about the amount of time it will take to assemble your new bookcase, so you look up the assembly times reported in `app_data`. Thinking of the data in `app_data` as a random sample of all IKEA purchases, you want to perform a permutation test to test the following hypotheses.

**Null Hypothesis**: The assembly time for the BILLY bookcase and the assembly time for the LOMMARP bookcase come from the same distribution.

**Alternative Hypothesis**: The assembly time for the BILLY bookcase and the assembly time for the LOMMARP bookcase come from different distributions. 

# BEGIN SUBPROB

Suppose we added a column to `app_data` called `'minutes'`, containing the `'assembly_time'` value for each entry converted to an integer amount of minutes. 
Then, we query `app_data` to keep only the BILLY bookcases, then average the `'minutes'` column. In addition, we separately query `app_data` to keep only the LOMMARP bookcases, then average the `'minutes'` column. If the null hypothesis is true, which of the following statements about these two averages is correct?

( ) These two averages are the same.
( ) Any difference between these two averages is due to random chance.
( ) Any difference between these two averages cannot be ascribed to random chance alone.
( ) The difference between these averages is statistically significant.

# BEGIN SOLUTION

**Answer: ** Any difference between these two averages is due to random chance.

If the null hypothesis is true, this means that the time recorded in `app_data` for each BILLY bookcase is a random number that comes from some distribution, and the time recorded in `app_data` for each LOMMARP bookcase is a random number that comes from *the same* distribution. Each assembly time is a random number, so even if the null hypothesis is true, if we take one person who assembles a BILLY bookcase and one person who assembles a LOMMARP bookcase, there is no guarantee that their assembly times will match. Their assembly times might match, or they might be different, because assembly time is random. Randomness is the only reason that their assembly times might be different, as the null hypothesis says there is no systematic difference in assembly times between the two bookcases. Specifically, it's not the case that one typically takes longer to assemble than the other.

With those points in mind, let's go through the answer choices.

The first answer choice is incorrect. Just because two sets of numbers are drawn from the same distribution, the numbers themselves might be different due to randomness, and the averages might also be different. Maybe just by chance, the people who assembled the BILLY bookcases and recorded their times in `app_data` were slower on average than the people who assembled LOMMARP bookcases. If the null hypothesis is true, this difference in average assembly time should be small, but it very likely exists to some degree.

The second answer choice is correct. If the null hypothesis is true, the only reason for the difference is random chance alone.

The third answer choice is incorrect for the same reason that the second answer choice is correct. If the null hypothesis is true, any difference must be explained by random chance.

The fourth answer choice is incorrect. If there is a difference between the averages, it should be very small and not statistically significant. In other words, if we did a hypothesis test and the null hypothesis was true, we should fail to reject the null.

<average>77</average>
# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

For the permutation test, we'll use as our test statistic the average assembly time for BILLY bookcases minus the average assembly time for LOMMARP bookcases, in minutes.

Complete the code below to generate one simulated value of the test statistic in a new way, without using `np.random.permutation`.

```py
billy = (app_data.get('product') == 
        'BILLY Bookcase, white, 31 1/2x11x79 1/2')
lommarp = (app_data.get('product') == 
          'LOMMARP Bookcase, dark blue-green, 25 5/8x78 3/8')
billy_lommarp = app_data[billy|lommarp]
billy_mean = np.random.choice(billy_lommarp.get('minutes'), billy.sum()).mean()
lommarp_mean = _________
billy_mean - lommarp_mean
```

What goes in the blank?

( ) `billy_lommarp[lommarp].get('minutes').mean()`
( ) `np.random.choice(billy_lommarp.get('minutes'), lommarp.sum()).mean()`
( ) `billy_lommarp.get('minutes').mean() - billy_mean`
( ) `(billy_lommarp.get('minutes').sum() - billy_mean * billy.sum())/lommarp.sum()`

# BEGIN SOLUTION

**Answer: ** `(billy_lommarp.get('minutes').sum() - billy_mean * billy.sum())/lommarp.sum()`

The first line of code creates a boolean Series with a True value for every BILLY bookcase, and the second line of code creates the analogous Series for the LOMMARP bookcase. The third line queries to define a DataFrame called `billy_lommarp` containing all products that are BILLY or LOMMARP bookcases. In other words, this DataFrame contains a mix of BILLY and LOMMARP bookcases. 

From this point, the way we would normally proceed in a permutation test would be to use `np.random.permutation` to shuffle one of the two relevant columns (either `'product'` or `'minutes'`) to create a random pairing of assembly times with products. Then we would calculate the average of all assembly times that were randomly assigned to the label BILLY. Similarly, we'd calculate the average of all assembly times that were randomly assigned to the label LOMMARP. Then we'd subtract these averages to get one simulated value of the test statistic. To run the permutation test, we'd have to repeat this process many times.

In this problem, we need to generate a simulated value of the test statistic, without randomly shuffling one of the columns. The code starts us off by defining a variable called `billy_mean` that comes from using `np.random.choice`. There's a lot going on here, so let's break it down. Remember that the first argument to `np.random.choice` is a sequence of values to choose from, and the second is the number of random choices to make. The default behavior is to make the random choices without replacement, so that no element that has already been chosen can be chosen again. Here, we're making our random choices from the `'minutes'` column of `billy_lommarp`. The number of choices to make from this collection of values is `billy.sum()`, which is the sum of all values in the `billy` Series defined in the first line of code. The `billy` Series contains True/False values, but in Python, True counts as 1 and False counts as 0, so `billy.sum()` evaluates to the number of True entries in `billy`, which is the number of BILLY bookcases recorded in `app_data`. It helps to think of the random process like this:

1. Collect all the assembly times of any BILLY or LOMMARP bookcase in a large bag.
2. Pull out a random assembly time from this bag.
3. Repeat step 2, drawing as many times as there are BILLY bookcases, without replacement. 

If we think of the random times we draw as being labeled BILLY, then the remaining assembly times still leftover in the bag represent the assembly times randomly labeled LOMMARP. In other words, this is a random association of assembly times to labels (BILLY or LOMMARP), which is the same thing we usually accomplish by shuffling in a permutation test. 

From here, we can proceed the same way as usual. First, we need to calculate the average of all assembly times that were randomly assigned to the label BILLY. This is done for us and stored in `billy_mean`. We also need to calculate the average of all assembly times that were randomly assigned the label LOMMARP. We'll call that `lommarp_mean`. Thinking of picking times out of a large bag, this is the average of all the assembly times left in the bag. The problem is there is no easy way to access the assembly times that were not picked. We can take advantage of the fact that we can easily calculate the total assembly time of all BILLY and LOMMARP bookcases together with `billy_lommarp.get('minutes').sum()`. Then if we subtract the total assembly time of all bookcases randomly labeled BILLY, we'll be left with the total assembly time of all bookcases randomly labeled LOMMARP. That is, `billy_lommarp.get('minutes').sum() - billy_mean * billy.sum()` represents the total assembly time of all bookcases randomly labeled LOMMARP. The count of the number of LOMMARP bookcases is given by `lommarp.sum()` so the average is `(billy_lommarp.get('minutes').sum() - billy_mean * billy.sum())/lommarp.sum()`.

A common wrong answer for this question was the second answer choice, `np.random.choice(billy_lommarp.get('minutes'), lommarp.sum()).mean()`. This mimics the structure of how `billy_mean` was defined so it's a natural guess. However, this corresponds to the following random process, which doesn't associate each assembly with a unique label (BILLY or LOMMARP):

1. Collect all the assembly times of any BILLY or LOMMARP bookcase in a large bag.
2. Pull out a random assembly time from this bag.
3. Repeat, drawing as many times as there are BILLY bookcases, without replacement.
4. Collect all the assembly times of any BILLY or LOMMARP bookcase in a large bag.
5. Pull out a random assembly time from this bag.
6. Repeat step 5, drawing as many times as there are LOMMARP bookcases, without replacement.

We could easily get the same assembly time once for BILLY and once for LOMMARP, while other assembly times could get picked for neither. This process doesn't split the data into two random groups as desired.
<average>12</average>
# END SOLUTION

# END SUBPROB

# END PROB