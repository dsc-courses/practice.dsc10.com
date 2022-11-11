# BEGIN PROB

# BEGIN SUBPROB

You’re definitely going to Sun God 2022, but you don’t want to go alone! Fortunately, you have $n$ friends who promise to go with you. Unfortunately, your friends are somewhat flaky, and each has a probability $p$ of actually going (independent of all others). What is the probability that you wind up going alone? Give your answer in terms of $p$ and $n$.

# BEGIN SOLUTION

**Answer: ** $(1-p)^n$

If you go alone, it means all of your friends failed to come. We can think of this as an *and* condition in order to use multiplication. The condition is: your first friend doesn't come *and* your second friend doesn't come, and so on. The probability of any individual friend not coming is $1-p$, so the probability of all your friends not coming is $(1-p)^n$.

<average>76</average>


# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

In past Sun God festivals, sometimes artists that were part of the lineup have failed to show up! Let’s say there are $n$ artists scheduled for Sun God 2022, and each artist has a probability $p$ of showing up (independent of all others). What is the probability that the number of artists that show up is less than $n$, meaning somebody no-shows? Give your answer in terms of $p$ and $n$.

# BEGIN SOLUTION

**Answer: ** $1-p^n$

It's actually easier to figure out the opposite event. The opposite of somebody no-showing is everybody shows up. This is easier to calculate because we can think of it as an *and* condition: the first artist shows up *and* the second artist shows up, and so on. That means we just multiply probabilities. Therefore, the probability of all artists showing up is $p^n$ and the probability of some artist not showing up is $1-p^n$.

<average>73</average>


# END SOLUTION

# END SUBPROB

# END PROB
