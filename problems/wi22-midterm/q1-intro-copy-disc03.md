---
lecture: 5
---

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

`.max()` can aggregate both the numeric and string columns, so every non-key column remains. For strings, it returns the last value in lexicographic order. In contrast, `.mean()` would raise an error on the remaining string columns.

<average>78</average>

# END SOLN

# END PROB