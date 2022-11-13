# BEGIN PROB

```py
sky.groupby('material').max()
```

( ) int or float
( ) Boolean
( ) string
( ) array
( ) Series
( ) DataFrame
( ) error

# BEGIN SOLN

**Answer:** DataFrame

When grouping and using an aggregation method, the result is always a DataFrame. The DataFrame `sky.groupby('material').max()` contains all of the columns in `sky`, minus `'material'`, which has been moved to the index. It contains one row for each unique `'material'`.

Note that no columns were "dropped", as may happen when using `.mean()`, because `.max()` can work on Series' of any type. You can take the max of strings, while you cannot take the mean of strings.

<average>78</average>

# END SOLN

# END PROB