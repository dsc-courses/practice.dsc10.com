# BEGIN PROB

# BEGIN SUBPROB

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