# BEGIN PROB

Recall, `plum` has 31 rows.

Consider the function `df_choice`, defined below.

```py
def df_choice(df):
    return df[np.random.choice([True, False], df.shape[0], replace=True)]
```

# BEGIN SUBPROB

Suppose we call `df_choice(plum)` once. What is the probability that the result is an empty DataFrame?

( ) 0
( ) 1
( ) $\frac{1}{2^{25}}$
( ) $\frac{1}{2^{30}}$
( ) $\frac{1}{2^{31}}$
( ) $\frac{2^{31} - 1}{2^{31}}$
( ) $\frac{31}{2^{30}}$
( ) $\frac{31}{2^{31}}$
( ) None of the above

# BEGIN SOLN

**Answer:** $\frac{1}{2^{31}}$

First, let's understand what `df_choice` does. It takes in one input, `df`. The line `np.random.choice([True, False], df.shape[0], replace=True)` evaluates to an array such that:

- There is one element for every row in the input DataFrame or array `df` (so if `df` has 31 rows, the output array will have length 31)
- Each element is equally likely to be `True` or `False`, since the sequence we are selecting from is `[True, False]` and we are selecting with replacement

So `np.random.choice([True, False], df.shape[0], replace=True)` is an array the same length as `df`, with each element randomly set to `True` or `False`. Note that there is a $\frac{1}{2}$ chance the first element is `True`, a $\frac{1}{2}$ chance the second element is `True`, and so on.

Then, `df[np.random.choice([True, False], df.shape[0], replace=True)]` is using Boolean indexing to keep only the rows in `df` where the array `np.random.choice([True, False], df.shape[0], replace=True)` contains the value `True`. So, the function `df_choice` returns a **DataFrame** containing somewhere between 0 and `df.shape[0]` rows. Note that there is a $\frac{1}{2}$ chance that the new DataFrame contains the first row from `df`, a $\frac{1}{2}$ chance that the new DataFrame contains the second row from `df`, and so on.

In this question, the only input ever given to `df_choice` is `plum`, which has 31 rows.

<br>

In this subpart, we're asked for the probability that `df_choice(plum)` is an empty DataFrame. There are 31 rows, and each of them have a $\frac{1}{2}$ chance of being included in the output, and so a $\frac{1}{2}$ chance of being missing. So, the chance that they are all missing is:

$$\begin{aligned} P(\text{empty DataFrame}) &= P(\text{all rows missing}) \\ &= P(\text{row 0 missing and row 1 missing and ... and row 30 missing}) \\ &= P(\text{row 0 missing}) \cdot P(\text{row 1 missing}) \cdot ... \cdot P(\text{row 30 missing}) \\ &= \frac{1}{2} \cdot \frac{1}{2} \cdot ... \cdot \frac{1}{2} \\ &= \boxed{\frac{1}{2^{31}}} \end{aligned}$$

<average>83</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Suppose we call `df_choice(plum)` once. What is the probability that the result is a DataFrame with 30 rows?

( ) 0
( ) 1
( ) $\frac{1}{2^{25}}$
( ) $\frac{1}{2^{30}}$
( ) $\frac{1}{2^{31}}$
( ) $\frac{2^{31} - 1}{2^{31}}$
( ) $\frac{31}{2^{30}}$
( ) $\frac{31}{2^{31}}$
( ) None of the above

# BEGIN SOLN

**Answer:** $\frac{31}{2^{31}}$

In order for the resulting DataFrame to have 30 rows, exactly 1 row must be missing, and the other 30 must be present.

To start, let's consider one row in particular, say, row 7. The probability that row 7 is missing is $\frac{1}{2}$, and the probability that rows 0 through 6 and 8 through 30 are all present is $\frac{1}{2} \cdot \frac{1}{2} \cdot ... \cdot \frac{1}{2} = \frac{1}{2^{30}}$ using the logic from the previous subpart. So, the probability that row 7 is missing AND all other rows are present is $\frac{1}{2} \cdot \frac{1}{2^{30}} = \frac{1}{2^{31}}$.

Then, in order for there to be 30 rows, either row 0 must be missing, or row 1 must be missing, and so on:

$$\begin{aligned} P(\text{exactly one row missing}) &= P(\text{only row 0 is missing or only row 1 is missing or ... or only row 30 is missing}) \\ &= P(\text{only row 0 is missing}) + P(\text{only row 1 is missing}) + ... + P(\text{only row 30 is missing}) \\ &= \frac{1}{2^{31}} + \frac{1}{2^{31}} + ... + \frac{1}{2^{31}} \\ &= \boxed{\frac{31}{2^{31}}}  \end{aligned}$$

<average>48</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Suppose we call `df_choice(plum)` once.

**True or False:** The probability that the result is a DataFrame that consists of **just** row 0 from `plum` (and no other rows) is equal to the probability you computed in the first subpart of this problem.

( ) True
( ) False

# BEGIN SOLN

**Answer:** True

An important realization to make is that all **subsets** of the rows in `plum` are equally likely to be returned by `df_choice(plum)`, and they all have probability $\frac{1}{2^{31}}$. For instance, one subset of `plum` is the subset where rows 2, 5, 8, and 30 are missing, and the rest are all present. The probability that this subset is returned by `df_choice(plum)` is $\frac{1}{2^{31}}$.

This is true because for each individual row, the probability that it is present or missing is the same – $\frac{1}{2}$ – so the probability of any subset is a product of 31 $\frac{1}{2}$s, which is $\frac{1}{2^{31}}$. (The answer to the previous subpart was not $\frac{1}{2^{31}}$ because it was asking about multiple subsets – the subset where only row 0 was missing, and the subset where only row 1 was missing, and so on).

So, the probability that `df_choice(plum)` consists of just row 0 is $\frac{1}{2^{31}}$, and this is the same as the answer to the first subpart ($\frac{1}{2^{31}}$); in both situations, we are calculating the probability of one specific subset.

<average>63</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Suppose we call `df_choice(plum)` once.

What is the probability that the resulting DataFrame has 0 rows, or 1 row, or 30 rows, or 31 rows?

( ) 0
( ) 1
( ) $\frac{1}{2^{25}}$
( ) $\frac{1}{2^{30}}$
( ) $\frac{1}{2^{31}}$
( ) $\frac{2^{31} - 1}{2^{31}}$
( ) $\frac{31}{2^{30}}$
( ) $\frac{31}{2^{31}}$
( ) None of the above

# BEGIN SOLN

**Answer:** $\frac{1}{2^{25}}$

Here, we're not being asked for the probability of one specific subset (like the subset containing just row 0); rather, we're being asked for the probability of various different subsets, so our calculation will be a bit more involved.

We can break our problem down into four pieces. We can find the probability that there are 0 rows, 1 row, 30 rows, and 31 rows individually, and add these probabilities up, since only one of them can happen at a time (it's impossible for a DataFrame to have both 1 and 30 rows at the same time; these events are "mutually exclusive"). It turns out we've already calculated two of these probabilities:

- From the first subpart, the probability that 0 rows are returned is $\frac{1}{2^{31}}$. This corresponds to a single subset, the subset where all rows are missing.
- From the second subpart, the probability that 30 rows are returned is $\frac{31}{2^{31}}$.

The other two possibilities are _symmetric_ with the above two!

- The probability that 31 rows are returned is the same as the probability that 0 rows are returned, since the probability of a row being missing and a row being present is the same. This is $\frac{1}{2^{31}}$.
- The probability that 1 row is returned is the same as the probability that 1 row is missing, i.e. the probability that 30 rows are returned. This, from the second subpart, is $\frac{31}{2^{31}}$.

Putting it all together, we have:

$$\begin{aligned} P(\text{number of returned rows is 0, 1, 30, or 31}) &= P(\text{0 rows are returned}) + P(\text{1 row is returned}) + P(\text{30 rows are returned}) + P(\text{31 rows are returned}) \\ &= \frac{1}{2^{31}} + \frac{31}{2^{31}} + \frac{31}{2^{31}} + \frac{1}{2^{31}} \\ &= \frac{1 + 31 + 31 + 1}{2^{31}} \\ &= \frac{64}{2^{31}} \\ &= \frac{2^6}{2^{31}} \\ &= \frac{1}{2^{31 - 6}} \\ &= \boxed{\frac{1}{2^{25}}} \end{aligned}$$

<average>35</average>

# END SOLN

# END SUBPROB

# END PROB