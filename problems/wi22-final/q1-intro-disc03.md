# BEGIN PROB

# BEGIN SUBPROB

What type of visualization is best suited for visualizing the trend in the number of points Kelsey Plum scored per game in 2021?

( ) Histogram
( ) Bar chart
( ) Line chart
( ) Scatter plot

# BEGIN SOLUTION

**Answer: ** Line chart

Here, there are two quantitative variables (number of points and game number), and one of them involves some element of time (game number). Line charts are appropriate when one quantitative variable is time.

<average>75</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Fill in the blanks below so that `total_june` evaluates to the total number of points Kelsey Plum scored in June.

```py
june_only = plum[__(a)__]
total_june = june_only.__(b)__
```

1. What goes in blank (a)?

2. What goes in blank (b)?

# BEGIN SOLUTION

**Answer:** 

1. `plum.get('Date').str.contains('-06-')`

2. `get('PTS').sum()`

To find the total number of points Kelsey Plum scored in June, one approach is to first create a DataFrame with only the rows for June. During the month of June, the `'Date'` values contain `'-06-'` (since June is the 6th month), so `plum.get('Date').str.contains('-06-')` is a Series containing `True` only for the June rows and `june_only = plum[plum.get('Date').str.contains('-06-')]` is a DataFrame containing only the June rows.

Then, all we need is the sum of the `'PTS'` column, which is given by `june_only.get('PTS').sum()`.

<average>90</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

For your convenience, we show the first few rows of `plum` again below.

<center><img src='../assets/images/wi22-final/plum.png' width=40%></center>

There is exactly one team in the WNBA that Plum's team did not win any games against during the 2021 season. Fill in the blanks below so that `never_beat` evaluates to a string containing the three-letter code of that team.

```py
never_beat = plum.groupby(__(a)__).sum().__(b)__
```

1. What goes in blank (a)?

2. What goes in blank (b)?

# BEGIN SOLUTION

**Answer:**

1. `'Opp'`

2. `sort_values('Won').index[0]`

The key insight here is that the values in the `'Won'` column are Boolean, and when Boolean values are used in arithmetic they are treated as 1s (`True`) and 0s (`False`). The `sum` of several `'Won'` values is the same as the number of wins.

If we group `plum` by `'Opp'` and use `.sum()`, the resulting `'Won'` column contains the number of wins that Plum's team had against each unique opponent. If we sort this DataFrame by `'Won'` in increasing order (which is the default behavior of `sort_values`), the row at the top will correspond to the `'Opp'` that Plum's team had no wins against. Since we grouped by `'Opp'`, team names are stored in the index, so `.index[0]` will give us the name of the desired team.

<average>67</average>

# END SOLUTION

# END SUBPROB

# END PROB