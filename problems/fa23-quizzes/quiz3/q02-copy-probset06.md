# BEGIN PROB

Suppose we have access to a simple random sample of all US Costco
members of size **145**. Our sample is stored in a DataFrame named
`us_sample`, in which the `"Spend"` column contains the October 2023
spending of each sampled member in dollars.

# BEGIN SUBPROB

Fill in the blanks below so that `us_left` and `us_right` are the left
and right endpoints of a **46%** confidence interval for the average
October 2023 spending of all US members.

```py
costco_means = np.array([])
for i in np.arange(5000):
    resampled_spends = __(x)__
    costco_means = np.append(costco_means, resampled_spends.mean())
left = np.percentile(costco_means, __(y)__)
right = np.percentile(costco_means, __(z)__)
```

Which of the following could go in blank (x)? **Select all that apply.**

[ ] `us_sample.sample(145, replace=True).get("Spend")`
[ ] `us_sample.sample(145, replace=False).get("Spend")`
[ ] `np.random.choice(us_sample.get("Spend"), 145)`
[ ] `np.random.choice(us_sample.get("Spend"), 145, replace=True)`
[ ] `np.random.choice(us_sample.get("Spend"), 145, replace=False)`
[ ] None of the above.

What goes in blanks (y) and (z)? Give your answers as integers.

# BEGIN SOLUTION

**Answer**: 

- `x`: 
    - `us_sample.sample(145, replace=True).get("Spend")`
    - `np.random.choice(us_sample.get("Spend"), 145)`
    - `np.random.choice(us_sample.get("Spend"), 145, replace=True)`
- `y`: `27`
- `z`: `73`

<average>79</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

True or False: **46%** of all US members in `us_sample` spent between
`us_left` and `us_right` in October 2023.

( ) True 
( ) False

# BEGIN SOLUTION

**Answer**: False

<average>85</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

True or False: If we repeat the code from part (b) 200 times, each time
bootstrapping from a new random sample of 145 members drawn from all US
members, then about **92** of the intervals we create will contain the
average October 2023 spending of all US members.

( ) True 
( ) False

# BEGIN SOLUTION

**Answer**: True

<average>51</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

True or False: If we repeat the code from part (b) 200 times, each time
bootstrapping from `us_sample`, then about **92** of the intervals we
create will contain the average October 2023 spending of all US members.

( ) True 
( ) False

# BEGIN SOLUTION

**Answer**: False

<average>30</average>

# END SOLUTION

# END SUBPROB

# END PROB