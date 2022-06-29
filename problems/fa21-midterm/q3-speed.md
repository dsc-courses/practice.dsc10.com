# BEGIN PROB

Fill in the blanks below so that the result is a DataFrame with the same columns as `flights` plus a new column, `'SPEED'`, containing the average speed of each flight, in miles per hour.

```python
flights.__(a)__(SPEED=__(b)__)
```

# BEGIN SUBPROB

What goes in blank (a)?

( ) `groupby`
( ) `assign`
( ) `rename`
( ) `drop`
( ) `merge`

# BEGIN SOLUTION

**Answer: ** `assign`

solution here

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

What goes in blank (b)?

# BEGIN SOLUTION

**Answer: ** `(flights.get('DIST') / flights.get('HOURS'))`

solution here

# END SOLUTION

# END SUBPROB

# END PROB