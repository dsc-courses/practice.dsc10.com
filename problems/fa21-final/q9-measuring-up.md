# BEGIN PROB

We're now interested in investigating the differences between the masses of Adelie penguins and Chinstrap penguins. Specifically, our null hypothesis is that their masses are drawn from the same population distribution, and any observed differences are due to chance only.

Below, we have a snippet of working code for this hypothesis test, for a specific test statistic. Assume that `adelie_chinstrap` is a DataFrame of only Adelie and Chinstrap penguins, with just two columns – `'species'` and `'mass'`.

```py
stats = np.array([])
num_reps = 500
for i in np.arange(num_reps):
    # --- line (a) starts ---
    shuffled = np.random.permutation(adelie_chinstrap.get('species'))
    # --- line (a) ends ---
    
    # --- line (b) starts ---
    with_shuffled = adelie_chinstrap.assign(species=shuffled)
    # --- line (b) ends ---

    grouped = with_shuffled.groupby('species').mean()

    # --- line (c) starts ---
    stat = grouped.get('mass').iloc[0] - grouped.get('mass').iloc[1]
    # --- line (c) ends ---

    stats = np.append(stats, stat)
```

# BEGIN SUBPROB

Which of the following statements best describe the procedure above?

( ) This is a standard hypothesis test, and our test statistic is the total variation distance between the distribution of Adelie masses and Chinstrap masses
( ) This is a standard hypothesis test, and our test statistic is the difference between the expected proportion of Adelie penguins and the proportion of Adelie penguins in our resample
( ) This is a permutation test, and our test statistic is the total variation distance between the distribution of Adelie masses and Chinstrap masses
( ) This is a permutation test, and our test statistic is the difference in the mean Adelie mass and mean Chinstrap mass

# BEGIN SOLUTION

**Answer: ** This is a permutation test, and our test statistic is the difference in the mean Adelie mass and mean Chinstrap mass (Option 4)

solution here

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Currently, line (c) (marked with a comment) uses .iloc. Which of the following options compute the exact same statistic as line (c) currently does?

Option 1:

```py
stat = grouped.get('mass').loc['Adelie'] - grouped.get('mass').loc['Chinstrap']
```

Option 2:

```py
stat = grouped.get('mass').loc['Chinstrap'] - grouped.get('mass').loc['Adelie']
```

( ) Option 1 only
( ) Option 2 only
( ) Both options
( ) Neither option

# BEGIN SOLUTION

**Answer: ** Option 1 only

solution here

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Is it possible to re-write `line (c)` in a way that uses `.iloc[0]` twice, without any other uses of `.loc` or `.iloc`?

( ) Yes, it's possible
( ) No, it's not possible

# BEGIN SOLUTION

**Answer: ** Yes, it's possible

solution here

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

For your convenience, we copy the code for the hypothesis test below.

```py
stats = np.array([])
num_reps = 500
for i in np.arange(num_reps):
    # --- line (a) starts ---
    shuffled = np.random.permutation(adelie_chinstrap.get('species'))
    # --- line (a) ends ---
    
    # --- line (b) starts ---
    with_shuffled = adelie_chinstrap.assign(species=shuffled)
    # --- line (b) ends ---

    grouped = with_shuffled.groupby('species').mean()

    # --- line (c) starts ---
    stat = grouped.get('mass').iloc[0] - grouped.get('mass').iloc[1]
    # --- line (c) ends ---

    stats = np.append(stats, stat)
```

What would happen if we removed `line (a)`, and replaced `line (b)` with

```py
with_shuffled = adelie_chinstrap.sample(adelie_chinstrap.shape[0], replace=False)
```

Select the best answer.

( ) This would still run a valid hypothesis test
( ) This would not run a valid hypothesis test, as all values in the `stats` array would be exactly the same
( ) This would not run a valid hypothesis test, even though there would be several different values in the `stats` array
( ) This would not run a valid hypothesis test, as it would incorporate information about Gentoo penguins

# BEGIN SOLUTION

**Answer: ** This would not run a valid hypothesis test, as all values in the `stats` array would be exactly the same (Option 2)

solution here

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

For your convenience, we copy the code for the hypothesis test below.

```py
stats = np.array([])
num_reps = 500
for i in np.arange(num_reps):
    # --- line (a) starts ---
    shuffled = np.random.permutation(adelie_chinstrap.get('species'))
    # --- line (a) ends ---
    
    # --- line (b) starts ---
    with_shuffled = adelie_chinstrap.assign(species=shuffled)
    # --- line (b) ends ---

    grouped = with_shuffled.groupby('species').mean()

    # --- line (c) starts ---
    stat = grouped.get('mass').iloc[0] - grouped.get('mass').iloc[1]
    # --- line (c) ends ---

    stats = np.append(stats, stat)
```

What would happen if we removed `line (a)`, and replaced `line (b)` with

```py
with_shuffled = adelie_chinstrap.sample(adelie_chinstrap.shape[0], replace=True)
```

Select the best answer.

( ) This would still run a valid hypothesis test
( ) This would not run a valid hypothesis test, as all values in the `stats` array would be exactly the same
( ) This would not run a valid hypothesis test, even though there would be several different values in the `stats` array
( ) This would not run a valid hypothesis test, as it would incorporate information about Gentoo penguins

# BEGIN SOLUTION

**Answer: ** This would not run a valid hypothesis test, even though there would be several different values in the `stats` array (Option 3)

solution here

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

For your convenience, we copy the code for the hypothesis test below.

```py
stats = np.array([])
num_reps = 500
for i in np.arange(num_reps):
    # --- line (a) starts ---
    shuffled = np.random.permutation(adelie_chinstrap.get('species'))
    # --- line (a) ends ---
    
    # --- line (b) starts ---
    with_shuffled = adelie_chinstrap.assign(species=shuffled)
    # --- line (b) ends ---

    grouped = with_shuffled.groupby('species').mean()

    # --- line (c) starts ---
    stat = grouped.get('mass').iloc[0] - grouped.get('mass').iloc[1]
    # --- line (c) ends ---

    stats = np.append(stats, stat)
```

What would happen if we replaced `line (a)` with

```py
with_shuffled = adelie_chinstrap.assign(
    species=np.random.permutation(adelie_chinstrap.get('species')
)
```

and replaced line (b) with

```py
with_shuffled = with_shuffled.assign(
    mass=np.random.permutation(adelie_chinstrap.get('mass')
)
```

Select the best answer.

( ) This would still run a valid hypothesis test
( ) This would not run a valid hypothesis test, as all values in the `stats` array would be exactly the same
( ) This would not run a valid hypothesis test, even though there would be several different values in the `stats` array
( ) This would not run a valid hypothesis test, as it would incorporate information about Gentoo penguins

# BEGIN SOLUTION

**Answer: ** This would still run a valid hypothesis test (Option 1)

solution here

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Suppose we run the code for the hypothesis test and see the following empirical distribution for the test statistic. In red is the observed statistic.

<center><img src='../assets/images/fa21-final/measuring_up_his.png' width=40%></center>

Suppose our alternative hypothesis is that Chinstrap penguins weigh more on average than Adelie penguins. Which of the following is closest to the p-value for our hypothesis test?

( ) $0$
( ) $\frac{1}{4}$
( ) $\frac{1}{3}$
( ) $\frac{2}{3}$
( ) $\frac{3}{4}$
( ) $1$

# BEGIN SOLUTION

**Answer: ** $\frac{1}{3}$

solution here

# END SOLUTION

# END SUBPROB

# END PROB