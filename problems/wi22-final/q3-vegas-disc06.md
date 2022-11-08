# BEGIN PROB

ESPN (a large sports news network) states that the Las Vegas Aces have a 60% chance of winning their upcoming game. You're curious as to how they came up with this estimate, and you decide to conduct a hypothesis test for the following hypotheses:

- **Null Hypothesis:** The Las Vegas Aces win each game with a probability of 60%.

- **Alternative Hypothesis:** The Las Vegas Aces win each game with a probability **above** 60%.

In both hypotheses, we are assuming that each game is independent of all other games. 

In the 2021 season, the Las Vegas Aces **won 22** of their games and **lost 9** of their games.

# BEGIN SUBPROB

Below, we have provided the code necessary to conduct the hypothesis test described above.

```py
stats = np.array([])
for i in np.arange(10000):
    sim = np.random.multinomial(31, [0.6, 0.4])
    stat = fn(sim)
    stats = np.append(stats, stat)
win_p_value = np.count_nonzero(stats >= fn([22, 9])) / 10000
```

`fn` is a **function** that computes a test statistic, given a list or array `arr` of two elements (the first of which is the number of wins, and the second of which is the number of losses). You can assume that neither element of `arr` is equal to 0.

Below, we define 5 possible test statistics `fn`.

**Option 1:**
```py
def fn(arr):
    return arr[0] / arr[1]
```

**Option 2:**
```py
def fn(arr):
    return arr[0]
```

**Option 3:**
```py
def fn(arr):
    return np.abs(arr[0] - arr[1])
```

**Option 4:**
```py
def fn(arr):
    return arr[0] - arr[1]
```

**Option 5:**
```py
def fn(arr):
    return arr[1] - arr[0]
```

Which of the above functions `fn` would be valid test statistics for this hypothesis test and p-value calculation? **Select all that apply.**

[ ] Option 1
[ ] Option 2
[ ] Option 3
[ ] Option 4
[ ] Option 5

# BEGIN SOLN

**Answer:** Options 1, 2, and 4

In the code provided to us, `stats` is an array containing 10,000 p-values generated by the function `fn` (note that we are appending `stat` to `stats`, and in the line before that we have `stat = fn(sim)`). In the very last line of the code provided, we have:

```py
win_p_value = np.count_nonzero(stats >= fn([22, 9])) / 10000
```

If we look closely, we see that we are computing the p-value by computing the proportion of simulated test statistics that were **greater than or equal to (`>=`) the observed statistic**. Since a p-value is computed as the proportion of simulated test statistics that were **as or more extreme than the observed statistic**, here it must mean that "big" test statistics are more extreme.

Remember, the direction that is "extreme" is determined by our alternative hypothesis. Here, the alternative hypothesis is that the Las Vegas Aces win each game with a probability above 60%. As such, the test statistic(s) we choose **must be large when the probability that the Aces win a game is high**, and small when the probability that the Aces win a game is low. With this all in mind, we can take a look at the 5 options, **remembering that `arr[0]` is the number of simulated wins and `arr[1]` is the number of simulated losses in a season of 31 games**. This means that when the Aces win more than they lose, `arr[0] > arr[1]`, and when they lose more than they win, `arr[0] < arr[1]`.

- **Option 1:** Here, our test statistic is the ratio of wins to losses, i.e. `arr[0] / arr[1]`. If the Aces win a lot, the numerator will be larger than the denominator, so this ratio will be large. If the Aces lose a lot, the numerator will be smaller than the denominator, and so this ratio will be small. This is what we want!
- **Option 2:** Here, our test statistic is the number of wins, i.e. `arr[0]`. If the Aces win a lot, this number will be large, and if the Aces lose a lot, this number will be small. This is what we want!
- **Option 3:** Here, our test statistic is the absolute value of the number of wins minus the number of losses, i.e. `np.abs(arr[0] - arr[1])`. If the Aces win a lot, then `arr[0] - arr[1]` will be large, and so will `np.abs(arr[0] - arr[1])`. This seems fine. **However**, if the Aces lose a lot, then `arr[0] - arr[1]` will be small (negative), but `np.abs(arr[0] - arr[1])` will still be large and positive. This test statistic doesn't allow us to **differentiate** when the Aces win a lot or lose a lot, so we can't use it as a test statistic for our alternative hypothesis.
- **Option 4:** From the explanation of Option 3, we know that when the Aces win a lot, `arr[0] - arr[1]` is large. Furthermore, when the Aces lose a lot, `arr[0] - arr[1]` is small (negative numbers are small in this context). This works!
- **Option 5:** `arr[1] - arr[0]` is the opposite of `arr[0] - arr[1]` in Option 4. When the Aces win a lot, `arr[1] - arr[0]` is small (negative), and when the Aces lose a lot, `arr[1] - arr[0]` is large (positive). This is the opposite of what we want, so Option 5 does not work.

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

The empirical distribution of one of the 5 test statistics presented in the previous subpart is shown below. To draw the histogram, we used the argument `bins=np.arange(-10, 25)`.

<center><img src='../assets/images/wi22-final/test-stat-dist.png' width=50%></center>

Which test statistic does the above empirical distribution belong to?

( ) Option 1
( ) Option 2
( ) Option 3
( ) Option 4
( ) Option 5

# BEGIN SOLN

**Answer:** Option 4

The distribution visualized in the histogram has the following unique values: -9, -7, -5, -3, ..., 17, 19, 21, 23. Crucially, the test statistic whose distribution we've visualized can both be positive and negative. Right off the bat, we can eliminate Options 1, 2, and 3:

- **Option 1**: Invalid. Option 1 is computed by dividing the number of wins (`arr[0]`) by the number of losses (`arr[1]`), and that quotient will always be a non-negative number.
- **Option 2:** Invalid, since the number of wins (`arr[0]`) will always be a non-negative number.
- **Option 3:** Invalid, since the absolute value of any real number (`np.abs(arr[0] - arr[1])`, in this case) will always be a non-negative number.

Now, we must decide between Option 4, whose test statistic is "wins minus losses" (`arr[0] - arr[1]`), and Option 5, whose test statistic is "losses minus wins" (`arr[1] - arr[0]`). 

First, let's recap _how_ we're simulating. In the code provided in the previous subpart, we have the line `sim = np.random.multinomial(31, [0.6, 0.4])`. Each time we run this line, `sim` will be set to an array with two elements, the first of which we interpret as the number of simulated wins and the second of which we interpret as the number of simulated losses in a 31 game season. The first number in `sim` will usually be larger than the second number in `sim`, since the chance of a win (0.6) is larger than the chance of a loss (0.4). As such, When we compute `fn(sim)` in the following line, the difference between the wins and losses should typically be positive.

Back to our distribution. Note that the distribution provided in this subpart is **centered** at a positive number, around 7. Since the difference between wins and losses will typically be positive, it appears that we've visualized the distribution of the difference between wins and losses (Option 4). If we instead visualized the difference between losses and wins, the distribution should be centered at a negative number, but that's not the case.

As such, the correct answer is Option 4.

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Consider the function `fn_plus` defined below.

```py
def fn_plus(arr):
    return fn(arr) + 31
```

**True or False:** If `fn` is a valid test statistic for the hypothesis test and p-value calculation presented at the start of the problem, then `fn_plus` is also a valid test statistic for the hypothesis test and p-value calculation presented at the start of the problem.

( ) True
( ) False

# BEGIN SOLN

**Answer:** True

All `fn_plus` is doing is adding 31 to the output of `fn`. If we think in terms of pictures, the _shape_ of the distribution of `fn_plus` looks the same as the distribution of `fn`, just moved to the right by 31 units. Since the distribution's shape is no different, the proportion of simulated test statistics that are greater than the observed test statistic is no different either, and so the p-value we calculate with `fn_plus` is the same as the one we calculate with `fn`.

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Below, we present the same code that is given at the start of the problem.

```py
stats = np.array([])
for i in np.arange(10000):
    sim = np.random.multinomial(31, [0.6, 0.4])
    stat = fn(sim)
    stats = np.append(stats, stat)

win_p_value = np.count_nonzero(stats >= fn([22, 9])) / 10000
```

Below are four possible replacements for the line `sim = np.random.multinomial(31, [0.6, 0.4])`.

**Option 1:**
```py
def with_rep():
    won = plum.get('Won')
    return np.count_nonzero(np.random.choice(won, 31, replace=True))

sim = [with_rep(), 31 - with_rep()]
```

**Option 2:**
```py
def with_rep():
    won = plum.get('Won')
    return np.count_nonzero(np.random.choice(won, 31, replace=True))

w = with_rep()
sim = [w, 31 - w]
```

**Option 3:**
```py
def without_rep():
    won = plum.get('Won')
    return np.count_nonzero(np.random.choice(won, 31, replace=False))

sim = [without_rep(), 31 - without_rep()]
```

**Option 4:**
```py
def perm():
    won = plum.get('Won')
    return np.count_nonzero(np.random.permutation(won))

w = perm()
sim = [w, 31 - w]
```

Which of the above four options could we replace the line `sim = np.random.multinomial(plum.shape[0], [0.6, 0.4])` with and still perform a valid hypothesis test for the hypotheses stated at the start of the problem?

( ) Option 1
( ) Option 2
( ) Option 3
( ) Option 4

# BEGIN SOLN

**Answer:** Option 2

The line `sim = np.random.multinomial(plum.shape[0], [0.6, 0.4])` assigns `sim` to an array containing two numbers such that:

- The numbers are randomly chosen each time the line is run
- The numbers always add up to 31

We need to select an option that also creates such an array (or list, in this case). Note that `won = plum.get('Won')`, a line that is common to all four options, assigns `won` to a Series with 31 elements, each of which is either `True` or `False` (corresponding to the wins and losses that the Las Vegas Aces earned in their season).

Let's take a look at the line `np.count_nonzero(np.random.choice(won, 31, replace=True))`, common to the first two options. Here, we are randomly selecting 31 elements from the Series `won`, with replacement, and counting the number of `True`s (since with `np.count_nonzero`, `False` is counted as `0`). Since we are making our selections with replacement, each selected element has a $\frac{22}{31}$ chance of being `True` and a $\frac{9}{31}$ chance of being `False` (since `won` has 22 `True`s and 9 `False`s). As such, `np.count_nonzero(np.random.choice(won, 31, replace=True))` can be any integer between 0 and 31, inclusive.

Note that if we select without replacement (`replace=False`) as Option 3 would like us to, then all 31 selected elements would be the same as the 31 elements in `won`. As a result, `np.random.choice(won, 31, replace=False)` will always have 22 `True`s, just like `won`, and `np.count_nonzero(np.random.choice(won, 31, replace=True))` will always return 22. That's not random, and so that's not quite what we're looking for.

With this all in mind, let's look at the four options.

- **Option 1:** Here, each time we call `with_rep()`, we get a random number between 0 and 31 (inclusive), corresponding to the (random) number of simulated wins. Then, we are assigning `sim` to be `[with_rep(), 31 - with_rep()]`. However, it's not guaranteed that the two calls to `with_rep` return the same number of wins, so it's not guaranteed that `sum(sim)` is 31. Option 1, then, is invalid.
- **Option 2:** Correct, as we'll explain below.
- **Option 3:** As mentioned above, Option 3 uses `replace=False`, and so `without_rep()` is always 22 and `sim` is always `[22, 9]`. The outcome is not random.
- **Option 4:** Here, `perm()` always returns the same number, 22. This is because all we are doing is shuffling the entries in the `won` Series, but we aren't changing the number of wins (`True`s) and losses (`False`s). As a result, `w` is always 22 and `sim` is always `[22, 9]`, making this non-random, just like in Option 3.

By the process of elimination, **Option 2** must be the correct choice. It is similar to Option 1, but it only calls `with_rep` once and "saves" the result to the name `w`. As a result, `w` is random, and `w` and `31 - w` are guaranteed to sum to 31.

**⚠️ Note:** It turns out that none of these options run a valid hypothesis test, since the null hypothesis was that the Las Vegas Aces win 60% of their games but none of these simulation strategies use 60% anywhere (instead, they use the observation that the Aces actually won 22 games). However, this subpart was about the sampling strategies themselves, so this mistake from our end doesn't invalidate the problem.

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Consider again the four options presented in the previous subpart.

In which of the four options is it **guaranteed** that `sum(sim)` evaluates to 31? **Select all that apply.**

[ ] Option 1
[ ] Option 2
[ ] Option 3
[ ] Option 4

# BEGIN SOLN

**Answers:** Options 2, 3, and 4

- **Option 1:** As explained in the solution to the previous subpart, if the two calls to `with_rep` evaluate to different numbers (entirely possible, since it is random), then `sum(sim)` will not be 31.
- **Option 2:** Here, `sim` is defined in terms of some `w`. Specifically, `w` is some number between 0 and 31 and `sim` is `[w, 31 - w]`, so `sum(sim)` is the same as `w + 31 - w`, which is always 31.
- **Option 3:** In Option 3, `sim` is always `[22, 9]`, and `sum(sim)` is always 31.
- **Option 4:** Same as Option 3.

# END SOLN

# END SUBPROB

# END PROB