# BEGIN PROB

Which of the following is a valid reason **not** to set the index of `sungod` to `'Artist'`? **Select all correct answers.**

[ ] Two different artists have the same name.
[ ] An artist performed at Sun God in more than one year.
[ ] Several different artists performed at Sun God in the same year.
[ ] Many different artists share the same value of `'Appearance_Order'`.
[ ] None of the above.

# BEGIN SOLUTION

**Answer: ** Two different artists have the same name., 
An artist performed at Sun God in more than one year.

The index should not contain duplicate values, so we need to consider reasons why `'Artist'` might contain two values that are the same. If two different artists had the same name, this would lead to duplicate values in the `'Artist'` column. Also, if one artist performed at Sun God in more than one year, their name would appear multiple times in the `'Artist'` column, once for each year they performed.

If several diferent artists performed at Sun God in the same year, that would not necessarily create duplicates in the `'Artist'` column, unless of course two of the artists had the same name, which we've already adressed in the first answer choice. If many different artists share the same value of `'Appearance_Order'`, this would also not create duplicates in the `'Artist'` column either.

# END SOLUTION

# END PROB