# BEGIN PROB

You need to estimate the proportion of American adults who want to be vaccinated against Covid-19. You plan to survey a random sample of American adults, and use the proportion of adults in your sample who want to be vaccinated as your estimate for the true proportion in the population. Your estimate must be within 0.04 of the true proportion, 95% of the time. Using the fact that the standard deviation of any dataset of 0’s and 1’s is no more than 0.5, calculate the minimum number of people you would need to survey. Input your answer below, as an **integer**.
# BEGIN SOLUTION

**Answer: ** 625

To anwser this question we can find the minimum number of people to survey by plugging in
n = (2/0.04)^2 (0.5) (1-0.5) = 625. To solve this we use the following formula:
n = (Z/M)^2 * (P) * (1-P)
where n is the sample size, Z is the score, M is the margin of error, and P is the probability. 
We decided to use a probability of 0.5 since it is the worst case (provides the largest value for the P * (1-P)
portion of the equation). M is given in the problem as 0.04. We can calculate Z from intuition,
we want the estimate to be within 0.04 95% of the time. Using the 68-95-99.7 rule we know 2 standard deviations
(Z = 2) is the correct choice for Z. 
# END SOLUTION

# END PROB