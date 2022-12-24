# BEGIN PROB

Suppose you draw a sample of size 100 from a population with mean 50 and standard deviation 15.  What is the probability that your sample has a mean between 50 and 53? Input the probability below, as a number between 0 and 1, rounded to **two decimal places**.

# BEGIN SOLUTION

**Answer: ** 0.48

This problem is testing our understanding of the Central Limit Theorem and normal distributions. Recall, the Central Limit Theorem tells us that the distribution of the sample mean is roughly normal, with the following characteristics:

$$\begin{align*}
\text{Mean of Distribution of Possible Sample Means} &= \text{Population Mean} = 50 \\
\text{SD of Distribution of Possible Sample Means} &= \frac{\text{Population SD}}{\sqrt{\text{Sample Size}}} = \frac{15}{\sqrt{100}} = 1.5
\end{align*}
$$

Given this information, it may be easier to express the problem as "We draw a value from a normal distribution with mean 50 and SD 1.5. What is the probability that the value is between 50 and 53?" Note that this probability is equal to the **proportion of values between 50 and 53** in a normal distribution whose mean is 50 and 1.5 (since probabilities can be thought of as proportions).

In class, we typically worked with the _standard_ normal distribution, in which the mean was 0, the SD was 1, and the $x$-axis represented values in standard units. Let's convert the quantities of interest in this problem to standard units, keeping in mind that the mean and SD we're using now are the mean and SD of the distribution of possible sample means, not of the population.

- 50 converted to standard units is $\frac{50 - \text{mean}}{\text{SD}} = \frac{50 - 50}{1.5} = 0$ (no calculation was necessary – 0 in standard units is equal to the mean in original units).
- 53 converted to standard units is $\frac{53 - \text{mean}}{\text{SD}} = \frac{53 - 50}{1.5} = 2$.

Now, our problem boils down to finding the **proportion of values in a standard normal distribution that are between 0 and 2**, or **the proportion of values in a normal distribution that are in the interval $[\text{mean}, \text{mean} + 2 \text{ SDs}]$**.

From class, we know that in a normal distribution, roughly 95% of values are within 2 standard deviations of the mean, i.e. the proportion of values in the interval $[\text{mean} - 2 \text{ SDs}, \text{mean} + 2 \text{ SDs}]$ is 0.95. 

<center><img src="../assets/images/wi21-final/normal-solution.png" width=50%></center>

Since the normal distribution is symmetric about the mean, half of the values in this interval are to the right of the mean, and half are to the left. This means that the proportion of values in the interval $[\text{mean}, \text{mean} + 2 \text{ SDs}]$ is $\frac{0.95}{2} = 0.475$, which rounds to 0.48, and thus the desired result is 0.48.

<average>48</average>

# END SOLUTION

# END PROB
