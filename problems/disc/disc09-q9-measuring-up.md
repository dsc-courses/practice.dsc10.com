# BEGIN PROB

Researchers from the San Diego Zoo, located within Balboa Park, collected physical measurements of three species of penguins (Adelie, Chinstrap, or Gentoo) in a region of Antarctica. One piece of information they tracked for each of 330 penguins was its mass in grams. The average penguin mass is 4200 grams, and the standard deviation is 840 grams.

We're interested in investigating the differences between the masses of Adelie penguins and Chinstrap penguins. Specifically, our null hypothesis is that their masses are drawn from the same population distribution, and any observed differences are due to chance only.

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

**Answer:** This is a permutation test, and our test statistic is the difference in the mean Adelie mass and mean Chinstrap mass (Option 4)

Recall, a permutation test helps us decide whether two random samples come from the same distribution. This test matches our goal of testing whether the masses of Adelie penguins and Chinstrap penguins are drawn from the same population distribution. The code above are also doing steps of a permutation test. In part (a), it shuffles `'species'` and stores the shuffled series to `shuffled`. In part (b), it assign the shuffled series of values to `'species'` column. Then, it uses ` grouped = with_shuffled.groupby('species').mean()` to calculate the mean of each species. In part (c), it computes the difference between mean mass of the two species by first getting the `'mass'` column and then accessing mean mass of each group (Adelie and Chinstrap) with positional index `0` and `1`.

<average>98</average>

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

**Answer:** This would not run a valid hypothesis test, as all values in the `stats` array would be exactly the same (Option 2)

Recall, `DataFrame.sample(n, replace = False)` (or `DataFrame.sample(n)` since `replace = False` is by default) returns a DataFrame by randomly sampling `n` rows from the DataFrame, without replacement. Since our `n` is `adelie_chinstrap.shape[0]`, and we are sampling without replacement, we will get the exactly same Dataframe (though the order of rows may be different but the `stats` array would be exactly the same).

<average>87</average>

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

**Answer:** This would not run a valid hypothesis test, even though there would be several different values in the `stats` array (Option 3)

Recall, `DataFrame.sample(n, replace = True)` returns a new DataFrame by randomly sampling `n` rows from the DataFrame, with replacement. Since we are sampling with replacement, we will have a DataFrame which produces a `stats` array with some different values. However, recall, the key idea behind a permutation test is to shuffle the group labels. So, the above code does not meet this key requirement since we only want to shuffle the `"species"` column without changing the size of the two species. However, the code may change the size of the two species.

<average>66</average>

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

**Answer:** This would still run a valid hypothesis test (Option 1)

Our goal for the permutation test is to randomly assign birth weights to groups, without changing group sizes. The above code shuffles `'species'` and `'mass'` columns and assigns them back to the DataFrame. This fulfills our goal.

<average>81</average>

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

**Answer:** $\frac{1}{3}$

Recall, the p-value is the chance, under the null hypothesis, that the test statistic is equal to the value that was observed in the data or is even further in the direction of the alternative. Thus, we compute the proportion of the test statistic that is equal or less than the observed statistic. (It is less than because less than corresponds to the alternative hypothesis "Chinstrap penguins weigh more on average than Adelie penguins". Recall, when computing the statistic, we use Adelie's mean mass minus Chinstrap's mean mass. If Chinstrap's mean mass is larger, the statistic will be negative, the direction of less than the observed statistic). 

Thus, we look at the proportion of area less than or on the red line (which represents observed statistic), it is around $\frac{1}{3}$.

<average>80</average>

# END SOLUTION

# END SUBPROB

# END PROB