# BEGIN PROB
We collect data on the play times of 100 games of *Chutes and Ladders* (sometimes known as *Snakes and Ladders*).

# BEGIN SUBPROB
We use our collected data to construct a 95% CLT-based confidence interval for the average play time of a game of *Chutes and Ladders*. This 95% confidence interval is [26.47, 28.47]. For the 100 games for which we collected data, what is the mean and standard deviation of the play times?

# BEGIN SOLUTION

**Answer:** mean = 27.47 and SD = 5

One of the key properties of the normal distribution is that about 95% of values lie within 2 standard deviations of the mean. The Central Limit Theorem states that the distribution of the sample mean is roughly normal, which means that to create this CLT-based 95% confidence interval, we used the 2 standard deviations rule.

What we're given, then, is the following:

$$\begin{align*} \text{Sample Mean} + 2 \cdot \text{SD of Distribution of Possible Sample Means} &= 28.47 \\ \text{Sample Mean} - 2 \cdot \text{SD of Distribution of Possible Sample Means} &= 26.47 \end{align*}$$

The sample mean is halfway between 26.47 and 28.47, which is 27.47. Substituting this into the first equation gives us

$$\begin{align*}27.47 + 2 \cdot \text{SD of Distribution of Possible Sample Means} &= 28.47\\2 \cdot \text{SD of Distribution of Possible Sample Means} &= 1 \\ \text{Distribution of Possible Sample Means} &= 0.5\end{align*}$$

It can be tempting to conclude that the sample standard deviation is 0.5, but it's not – the SD of the sample mean's distribution is 0.5. Remember, the SD of the sample mean's distribution is given by the square root law:

$$\text{SD of Distribution of Possible Sample Means} = \frac{\text{Population SD}}{\sqrt{\text{Sample Size}}} \approx \frac{\text{Sample SD}}{\sqrt{\text{Sample Size}}}$$

We don't know the population SD, so we've used the sample SD as an estimate. As such, we have that 

$$\text{SD of Distribution of Possible Sample Means} = 0.5 = \frac{\text{Sample SD}}{\sqrt{\text{Sample Size}}} = \frac{\text{Sample SD}}{\sqrt{100}}$$

So, $\text{Sample SD} = 0.5 \cdot \sqrt{100} = 0.5 \cdot 10 = 5$.

<average>64</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB
Does the CLT say that the distribution of play times of the 100 games is roughly
normal?

( ) Yes
( ) No

# BEGIN SOLUTION

**Answer:** No

The Central Limit Theorem states that the distribution of the sample mean or the sample sum is roughly normal. The distribution of play times is a sample of size 100 drawn from the population of play times; the Central Limit Theorem doesn't say anything about a population or any one sample.

<average>45</average>

# END SOLUTION

# END SUBPROB

# END PROB
