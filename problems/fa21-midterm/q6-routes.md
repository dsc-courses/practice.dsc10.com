# BEGIN PROB

We define a "route" to be a departure and arrival airport pair. For example, all flights from `'SFO'` to `'SAN'` make up the "SFO to SAN route". This is different from the "SAN to SFO route".

Fill in the blanks below so that `most_frequent.get('FROM').iloc[0]` and `most_frequent.get('TO').iloc[0]` correspond to the departure and destination airports of the route that King Triton has spent the **most time flying on**.

```py
most_frequent = flights.groupby(__(a)__).__(b)__
most_frequent = most_frequent.reset_index().sort_values(__(c)__)
```

# BEGIN SUBPROB

What goes in blank (a)?

# BEGIN SOLUTION

**Answer: ** `['FROM', 'TO']`

We want to organize flights by route. This means we need to group by both `'FROM'` and `'TO'` so any flights with the same pair of departure and arrival airports get grouped together. To group by multiple columns, we must use a list containing all these column names, as in `flights.groupby(['FROM', 'TO'])`.

<average>72</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

What goes in blank (b)?

( ) `count()`
( ) `mean()`
( ) `sum()`
( ) `max()`

# BEGIN SOLUTION

**Answer: ** `sum()`

Every `.groupby` command needs an aggregation function! Since we are asked to find the route that King Triton has spent the most time flying on, we want to total the times for all flights on a given route. 

Note that `.count()` would tell us how many flights King Triton has taken on each route. That's meaningful information, but not what we need to address the question of which route he spent the most time flying on.

<average>58</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB
What goes in blank (c)?

( ) `by='HOURS', ascending=True`
( ) `by='HOURS', ascending=False`
( ) `by='HOURS', descending=True`
( ) `by='DIST', ascending=False`

# BEGIN SOLUTION

**Answer: ** `by='HOURS', ascending=False`

We want to know the route that King Triton spent the most time flying on. After we group flights by route, summing flights on the same route, the `'HOURS'` column contains the total amount of time spent on each route. We need  `most_frequent.get('FROM').iloc[0]` and `most_frequent.get('TO').iloc[0]` to correspond with the departure and destination airports of the route that King Triton has spent the most time flying on. To do this, we need to sort in descending order of time, to bring the largest time to the top of the DataFrame. So we must sort by `'HOURS'` with `ascending=False`.

<average>94</average>

# END SOLUTION

# END SUBPROB

# END PROB