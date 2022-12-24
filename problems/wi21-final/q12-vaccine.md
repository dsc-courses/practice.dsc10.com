# BEGIN PROB

You need to estimate the proportion of American adults who want to be vaccinated against Covid-19. You plan to survey a random sample of American adults, and use the proportion of adults in your sample who want to be vaccinated as your estimate for the true proportion in the population. Your estimate must be within 0.04 of the true proportion, 95% of the time. Using the fact that the standard deviation of any dataset of 0’s and 1’s is no more than 0.5, calculate the minimum number of people you would need to survey. Input your answer below, as an **integer**.

# BEGIN SOLUTION

**Answer: ** 625

_Note: Before reviewing these solutions, it's highly recommended to revisit the lecture on "Choosing Sample Sizes," since this problem follows the main example from that lecture almost exactly._

While this solution is long, keep in mind from the start that our goal is to solve for the **smallest sample size necessary** to create a confidence interval that achieves certain criteria.

The Central Limit Theorem tells us that the distribution of the sample mean is roughly normal, regardless of the distribution of the population from which the samples are drawn. At first, it may not be clear how the Central Limit Theorem is relevant, but remember that proportions are means too – for instance, the proportion of adults who want to be vaccinated is equal to the mean of a collection of 1s and 0s, where we have a 1 for each adult that wants to be vaccinated and a 0 for each adult who doesn't want to be vaccinated. What this means (😉) is that **the Central Limit Theorem applies to the distribution of the sample proportion, so we can use it here too**.

Not only do we know that the distribution of sample proportions is roughly normal, but we know its mean and standard deviation, too:

$$\begin{align*}
\text{Mean of Distribution of Possible Sample Means} &= \text{Population Mean} = \text{Population Proportion} \\
\text{SD of Distribution of Possible Sample Means} &= \frac{\text{Population SD}}{\sqrt{\text{Sample Size}}}
\end{align*}
$$

Using this information, we can create a 95% confidence interval for the population proportion, using the fact that in a normal distribution, roughly 95% of values are within 2 standard deviations of the mean:

$$\left[ \text{Population Proportion} - 2 \cdot \frac{\text{Population SD}}{\sqrt{\text{Sample Size}}}, \: \text{Population Proportion} + 2 \cdot \frac{\text{Population SD}}{\sqrt{\text{Sample Size}}}  \right]$$

However, this interval depends on the population proportion (mean) and SD, which we don't know. (If we did know these parameters, there would be no need to collect a sample!) Instead, we'll use the sample proportion and SD as rough estimates:

$$\left[ \text{Sample Proportion} - 2 \cdot \frac{\text{Sample SD}}{\sqrt{\text{Sample Size}}}, \: \text{Sample Proportion} + 2 \cdot \frac{\text{Sample SD}}{\sqrt{\text{Sample Size}}}  \right]$$

Note that the width of this interval – that is, its right endpoint minus its left endpoint – is: $$\text{width} = 4 \cdot \frac{\text{Sample SD}}{\sqrt{\text{Sample Size}}}$$

In the problem, we're told that we want our interval to be accurate to within 0.04, which is equivalent to wanting the width of our interval to be less than or equal to 0.08 (since the interval extends the same amount above and below the sample proportion). As such, we need to pick the **smallest sample size necessary** such that:

$$\text{width} = 4 \cdot \frac{\text{Sample SD}}{\sqrt{\text{Sample Size}}} \leq 0.08$$

We can re-arrange the inequality above to solve for our sample's size:

$$
\begin{align*}
4 \cdot \frac{\text{Sample SD}}{\sqrt{\text{Sample Size}}} &\leq 0.08 \\
\frac{\text{Sample SD}}{\sqrt{\text{Sample Size}}} &\leq 0.02 \\
\frac{1}{\sqrt{\text{Sample Size}}} &\leq \frac{0.02}{\text{Sample SD}} \\
\frac{\text{Sample SD}}{0.02} &\leq \sqrt{\text{Sample Size}} \\
\left( \frac{\text{Sample SD}}{0.02} \right)^2 &\leq \text{Sample Size}
\end{align*}
$$

All we now need to do is pick the smallest sample size that satisfies the above inequality. But there's an issue – **we don't know what our sample SD is, because we haven't collected our sample**! Notice that in the inequality above, as the sample SD increases, so does the minimum necessary sample size. In order to ensure we don't collect too small of a sample (which would result in the width of our confidence interval being _larger_ than desired), we can use an upper bound for the SD of our sample. In the problem, we're told that the largest possible SD of a sample of 0s and 1s is 0.5 – this means that if we replace our sample SD with 0.5, we will find a sample size such that the width of our confidence interval is guaranteed to be less than or equal to 0.08. This sample size may be larger than necessary, but that's better than it being smaller than necessary.

By substituting 0.5 for the sample SD in the last inequality above, we get

$$
\begin{align*}
\left( \frac{\text{Sample SD}}{0.02} \right)^2 &\leq \text{Sample Size} \\\
\left( \frac{0.5}{0.02} \right)^2 &\leq \text{Sample Size} \\
25^2 &\leq \text{Sample Size} \implies \text{Sample Size} \geq 625
\end{align*}
$$

We need to pick the smallest possible sample size that is greater than or equal to 625; that's just 625.

<average>40</average>

# END SOLUTION

# END PROB
