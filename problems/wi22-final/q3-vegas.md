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

[X] Option 1
[X] Option 2
[ ] Option 3
[X] Option 4
[ ] Option 5

# END SUBPROB

# END PROB