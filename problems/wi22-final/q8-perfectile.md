# BEGIN PROB

# BEGIN SUBPROB

Recall that the mean points per game is 7, with a standard deviation of 5. Also note that for all players, points per game must be greater than or equal to 0.

Using Chebyshev's inequality, we find that at least $p\%$ of players scored 25 or fewer points per game.

What is the value of $p$? Give your answer as number between 0 and 100, rounded to 3 decimal places.

# BEGIN SOLN

**Answer:** $92.284\%$

Recall, Chebyshev's inequality states that the proportion of values within $z$ standard deviations of the mean is **at least** $1 - \frac{1}{z^2}$.

To approach the problem, we'll start by converting 25 points per game to standard units. Doing so yields $\frac{25 - 7}{5} = 3.6$. This means that 25 is 3.6 standard deviations **above** the mean. The value 3.6 standard deviations **below** the mean is $7 - 3.6 \cdot 5 = -11$, so when we use Chebyshev's inequality with $z = 3.6$, we will get a lower bound on the proportion of values between -11 and 25. However, as the question tells us, points per game must be non-negative, so in this case the proportion of values between -11 and 25 is the same as the proportion of values between 0 and 25 (i.e. the proportion of values less than or equal to 25).

When $z = 3.6$, we have $1 - \frac{1}{z^2} = 1 - \frac{1}{3.6^2} = 0.922839$, which as a percentage rounded to three decimal places is $92.284\%$. Thus, at least $92.284\%$ scored 25 or fewer points per game.

<average>46</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

<span style="color:red"><b>Note: This problem is out of scope; it covers material no longer included in the course.</b></span>

**Note:** This question uses the mathematical definition of percentile, not `np.percentile`.

The array `aces` defined below contains the points per game scored by all members of the Las Vegas Aces. Note that it contains 14 numbers that are in sorted order.

```py
aces = np.array([0, 0, 1.05, 1.47, 1.96, 2, 3.25, 
                 10.53, 11.09, 11.62, 12.19, 
                 14.24, 14.81, 18.25])
```

As we saw in lab, percentiles are not unique. For instance, the number 1.05 is both the 15th percentile and 16th percentile of `aces`.

There is a positive integer $q$, between 0 and 100, such that 14.24 is the $q$th percentile of `aces`, but 14.81 is the $(q+1)$th percentile of `aces`. 

What is the value of $q$? Give your answer as an integer between 0 and 100.

# BEGIN SOLN

**Answer:** 85

For reference, recall that we find the $p$th percentile of a collection of $n$ numbers as follows:

1. Sort the collection in increasing order.
2. Define $h$ to be $p\%$ of $n$: 

$$h = \frac{p}{100} \cdot n$$

3. If $h$ is an integer, define $k = h$. Otherwise, let $k$ be the smallest integer greater than $h$.

4. Take the $k$th element of the sorted collection (start counting from 1, not 0).

<br>

To start, it's worth emphasizing that there are $n = 14$ numbers in `aces` total. 14.24 is at position 12 (when the positions are numbered 1 through 14).

Let's try and find a value of $p$ such that 14.24 is the $p$th percentile. To do so, we might try and find what "percentage" of the way through the distribution 14.24 is; doing so gives $\frac{12}{14} = 85.71\%$. If we follow the process outlined above with $p = 85$, we get that $h = \frac{85}{100} \cdot 14 = 11.9$ and thus $k = 12$, meaning that the 85th percentile is the number at position 12, which 14.24.

Let's see what happens when we try the same process with $p = 86$. This time, we have $h = \frac{86}{100} \cdot 14 = 12.04$ and thus $k = 13$, meaning that the 86th percentile is the number at position 13, which is 14.81.

This means that the value of $q$ is 85 – the 85th percentile is 14.24, while the 86th percentile is 14.81.

<average>57</average>

# END SOLN

# END SUBPROB

# END PROB