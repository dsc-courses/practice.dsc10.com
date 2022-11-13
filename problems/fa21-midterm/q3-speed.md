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

We want to add a new column, so we must use `assign`. We can also tell that the answer will be `assign` because it's the only DataFrame method that takes an input of the form `SPEED=___`. Remember that when using assign, we get to call the new column anything we want, and we don't use quotes around its name.

<average>100</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

What goes in blank (b)?

# BEGIN SOLUTION

**Answer: ** `(flights.get('DIST') / flights.get('HOURS'))`

In this blank, we'll need a Series or array containing the average speed of each flight, in miles per hour. 

To calculate the average speed of an individual flight in miles per hour, we'd simply divide the total number of miles by the total amount of time in hours. For example, a flight that travels 500 miles in one hour travels at 500 miles per hour. Note that this is an *average* speed; at some points of the journey, the plane may have been moving faster than this speed, at other times slower. Because we are calculating an average speed for the whole trip by simply dividing, we don't need to use `.mean()`.

Once we know how to calculate the average speed for an individual flight, we can do the same operation on each flight all at once using Series arithmetic. `flights.get('DIST')` is a Series containing the distances of each flight, and `flights.get('HOURS')` is a Series containing the times of each flight, in the same order. When we divide these two Series, corresponding entries are divided and the result is a Series of average speeds for each flight, as desired.

<average>93</average>

# END SOLUTION

# END SUBPROB

# END PROB