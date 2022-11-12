# BEGIN PROB

You generate a three-digit number by randomly choosing each digit to be a number 0 through 9, inclusive. Each digit is equally likely to be chosen.

# BEGIN SUBPROB

What is the probability you produce the number **027**? Give your answer as a decimal number between 0 and 1 with no rounding.

# BEGIN SOLUTION

**Answer: ** 0.001

There is a $\frac{1}{10}$ chance that we get 0 as the first random number, a $\frac{1}{10}$ chance that we get 2 as the second random number, and a $\frac{1}{10}$ chance that we get 7 as the third random number. The probability of all of these events happening is $\frac{1}{10}*\frac{1}{10}*\frac{1}{10} = 0.001$.

Another way to do this problem is to think about the possible outcomes. Any number from 000 to 999 is possible and all are equally likely. Since there are 1000 possible outcomes and the number 027 is just one of the possible outcomes, the probability of getting this outcome is $\frac{1}{1000} = 0.001$.

<average>92</average>
# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

What is the probability you produce a number with an odd digit in the middle position? For example, **250**.  Give your answer as a decimal number between 0 and 1 with no rounding.

# BEGIN SOLUTION

**Answer: ** 0.5

Because the values of the left and right positions are not important to us, think of the middle position only. When selecting a random number to go here, we are choosing randomly from the numbers 0 through 9. Since 5 of these numbers are odd (1, 3, 5, 7, 9), the probability of getting an odd number is $\frac{5}{10} = 0.5$.

<average>78</average>
# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

What is the probability you produce a number with a **7** in it somewhere? Give your answer as a decimal number between 0 and 1 with no rounding.

# BEGIN SOLUTION

**Answer: ** 0.271

It's easier to calculate the probability that the number has no 7 in it, and then subtract this probability from 1. To solve this problem directly, we'd have to consider cases where 7 appeared multiple times, which would be more complicated.

The probability that the resulting number has no 7 is $\frac{9}{10}*\frac{9}{10}*\frac{9}{10} = 0.729$ because in each of the three positions, there is a $\frac{9}{10}$ chance of selecting something other than a 7. Therefore, the probability that the number has a 7 is $1 - 0.729 = 0.271$.
<average>69</average>
# END SOLUTION

# END SUBPROB

# END PROB