# BEGIN PROB

Suppose you draw a sample of size 100 from a population with mean 50 and standard deviation 15.  What is the probability that your sample has a mean between 50 and 53? Input the probability below, as a number between 0 and 1, rounded to **two decimal places**.

# BEGIN SOLUTION

**Answer: ** 0.48

We want to use Z scores to anwser this question. We can find the Z score for sample mean that are 
50 or above by using the Z-score formula z = (x – μ) / (σ / √n).
x represents the sample mean, μ represents the population mean, σ represents the population
standard deviation, and n represents the sample size. Plugging in we get the following:
(50-50) / (15/10) = 0. This z score will give the probability
of having a sample mean of 50 or above, but we want to exclude anything above 53. To do this,
we can compute the z score with (53-50) / (15/10) = 2. We find that 53 is 2 standard deviations away from
the mean which indicates 2.5 percent of the sample means are not included above 53 (using the 68-95-99.7 rule).
Therefore, we can compute the final values as P(Z>0) - P(Z>2) which is the same as 0.5-0.025 = 0.475 rounded to
0.48. 

# END SOLUTION

# END PROB