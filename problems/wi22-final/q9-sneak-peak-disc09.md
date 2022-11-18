# BEGIN PROB

Answer the following questions about a basketball dataset.


# BEGIN SUBPROB

Lets try to a construct a 95% confidence interval for the true mean points per game by using the Central Limit Theorem.

Assume that you have a random sample of size 36 of games in a basketball season with mean number of points per game = 9 and standard deviation = 4.

Compute a 95% confidence interval for the true mean points per game.

What are the left and right endpoints of your interval? Give your answers as numbers in mixed number notation.

# BEGIN SOLN

**Answer:** $[7.667, 10.333]$

In a normal distribution, roughly 95% of values are within 2 standard deviations of the mean. The CLT tells us that the distribution of sample means is roughly normal, and in subpart 4 of this problem we already computed the SD of the distribution of sample means to be $\frac{2}{3}$.

So, our normal-based 95% confidence interval is computed as follows:

$$\begin{aligned} &[\text{mean of sample} - 2 \cdot \text{SD of distribution of sample means}, \text{mean of sample} + 2 \cdot \text{SD of distribution of sample means}] \\ &= [9 - 2 \cdot \frac{4}{\sqrt{36}}, 9 + 2 \cdot \frac{4}{\sqrt{36}}] \\ &= [9 - \frac{4}{3}, 9 + \frac{4}{3}] \\ &\approx \boxed{[7.667, 10.333]} \end{aligned}$$

<average>87</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Now assume that the true mean points per game in is 7, which is not in the interval you found above (if it is, check your work!).

Select the true statement below.

( ) The 95% confidence interval we created in the previous subpart did not contain the true mean points per game, which means that the distribution of the sample mean is not normal.
( ) The 95% confidence interval we created in the previous subpart did not contain the true mean points per game, which means that the distribution of points per game in `small_season` is not normal.
( ) The 95% confidence interval we created in the previous subpart did not contain the true mean points per game. This is to be expected, because the Central Limit Theorem is only correct 95% of the time.
( ) The 95% confidence interval we created in the previous subpart did not contain the true mean points per game, but if we collected many original samples and constructed many 95% confidence intervals, then roughly 95% of them would contain the true mean points per game.
( ) The 95% confidence interval we created in the previous subpart did not contain the true mean points per game, but if we collected many original samples and constructed many 95% confidence intervals, then exactly 95% of them would contain the true mean points per game.

# BEGIN SOLN

**Answer:** The 95% confidence interval we created in the previous subpart did not contain the true mean points per game, but if we collected many original samples and constructed many 95% confidence intervals, then roughly 95% of them would contain the true mean points per game.

In a confidence interval, the confidence level gives us a level of confidence in **the process** used to create the confidence interval. If we repeat the process of collecting a sample from the population and using the sample to construct a c% confidence interval for the population mean, then **roughly** c% of the intervals we create should contain the population mean. Option 4 is the only option that corresponds to this interpretation; the others are all incorrect in different ways.

<average>87</average>

# END SOLN

# END SUBPROB

# END PROB
