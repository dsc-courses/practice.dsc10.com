# BEGIN PROB

Consider the definition of the function `diff_in_group_means`:

```py
def diff_in_group_means(df, group_col, num_col):
    s = df.groupby(group_col).mean().get(num_col)
    return s.loc[False] - s.loc[True]
```


# BEGIN SUBPROB

It turns out that Kelsey Plum averages 0.61 more assists in games that she wins than in games that she loses. After observing that Kelsey Plum averages more assists in winning games than in losing games, we become interested in conducting a permutation test for the following hypotheses:

- **Null Hypothesis:** The number of assists Kelsey Plum makes in winning games and in losing games come from the same distribution.
- **Alternative Hypothesis:** The number of assists Kelsey Plum makes in winning games is higher on average than the number of assists that she makes in losing games.

To conduct our permutation test, we place the following code in a `for`-loop.

```py

won = plum.get('Won')
ast = plum.get('AST')
shuffled = plum.assign(Won_shuffled=np.random.permutation(won)) \
               .assign(AST_shuffled=np.random.permutation(ast))
```

Which of the following options **does not** compute a valid simulated test statistic for this permutation test?

( ) `diff_in_group_means(shuffled, 'Won', 'AST')`
( ) `diff_in_group_means(shuffled, 'Won', 'AST_shuffled')`
( ) `diff_in_group_means(shuffled, 'Won_shuffled, 'AST')`
( ) `diff_in_group_means(shuffled, 'Won_shuffled, 'AST_shuffled')`
( ) More than one of these options do not compute a valid simulated test statistic for this permutation test

# BEGIN SOLN

**Answer:** `diff_in_group_means(shuffled, 'Won', 'AST')`

`diff_in_group_means(shuffled, 'Won', 'AST')` computes the observed test statistic, which is -0.61. There is no randomness involved in the observed test statistic; each time we run the line `diff_in_group_means(shuffled, 'Won', 'AST')` we will see the same result, so this cannot be used for simulation.

To perform a permutation test here, we need to simulate under the null by randomly assigning assist counts to groups; here, the groups are "win" and "loss".

- **Option 2:** Here, assist counts are shuffled and the group names are kept in the same order. The end result is a random pairing of assists to groups.
- **Option 3:** Here, the group names are shuffled and the assist counts are kept in the same order. The end result is a random pairing of assist counts to groups.
- **Option 4:** Here, both the group names and assist counts are shuffled, but the end result is still the same as in the previous two options.

As such, Options 2 through 4 are all valid, and Option 1 is the only invalid one.

<average>68</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Suppose we generate 10,000 simulated test statistics, using one of the valid options from Question 1.1. The empirical distribution of test statistics, with a red line at `observed_diff`, is shown below.

<center><img src='../assets/images/wi22-final/quarter-hist.png' width=50%></center>

Roughly one-quarter of the area of the histogram above is to the left of the red line. What is the correct interpretation of this result?

( ) There is roughly a one quarter probability that Kelsey Plum's number of assists in winning games and in losing games come from the same distribution.
( ) The significance level of this hypothesis test is roughly a quarter.
( ) Under the assumption that Kelsey Plum's number of assists in winning games and in losing games come from the same distribution, and that she wins 22 of the 31 games she plays, the chance of her averaging **at least** 0.61 more assists in wins than losses is roughly a quarter.
( ) Under the assumption that Kelsey Plum's number of assists in winning games and in losing games come from the same distribution, and that she wins 22 of the 31 games she plays, the chance of her averaging 0.61 more assists in wins than losses is roughly a quarter.

# BEGIN SOLN

**Answer:** Under the assumption that Kelsey Plum's number of assists in winning games and in losing games come from the same distribution, and that she wins 22 of the 31 games she plays, the chance of her averaging **at least** 0.61 more assists in wins than losses is roughly a quarter. (Option 3)

First, we should note that the area to the left of the red line (a quarter) is the p-value of our hypothesis test. Generally, the p-value is the probability of observing an outcome as or more extreme than the observed, under the assumption that the null hypothesis is true. The direction to look in depends on the alternate hypothesis; here, since our alternative hypothesis is that the number of assists Kelsey Plum makes in winning games is higher on average than in losing games, a "more extreme" outcome is where the assists in winning games are higher than in losing games, i.e. where $\text{(assists in wins)} - \text{(assists in losses)}$ is positive or where $\text{(assists in losses)} - \text{(assists in wins)}$ is negative. As mentioned in the solution to the first subpart, our test statistic is $\text{(assists in losses)} - \text{(assists in wins)}$, so a more extreme outcome is one where this is negative, i.e. to the left of the observed statistic.

Let's first rule out the first two options.

- **Option 1:** This option states that the probability that the null hypothesis (the number of assists she makes in winning and losing games comes from the same distribution) is true is roughly a quarter. However, the p-value **is not** the probability that the null hypothesis is true.
- **Option 2:** The significance level is the formal name for the p-value "cutoff" that we specify in our hypothesis test. There is no cutoff mentioned in the problem. The _observed_ significance level is another name for the p-value, but Option 2 did not contain the word _observed_.

Now, the only difference between Options 3 and 4 is the inclusion of "at least" in Option 3. Remember, to compute a p-value we must compute the probability of observing something as **or more** extreme than the observed, under the null. The "or more" corresponds to "at least" in Option 3. As such, Option 3 is the correct choice.

<average>70</average>

# END SOLN

# END SUBPROB

# END PROB