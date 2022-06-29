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

solution here

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

solution here

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

solution here

# END SOLUTION

# END SUBPROB

# END PROB