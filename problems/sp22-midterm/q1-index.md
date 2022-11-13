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

For this question, it is crucial to know that an index should not contain duplicate values, so we need to consider reasons why `'Artist'` might contain two values that are the same. Let's go through the answer choices in order.


For the first option, if two different artists had the same name, this would lead to duplicate values in the `'Artist'` column. Therefore, this is a valid reson not to index `sungod` by `'Artist'`.

For the second option, if one artist performed at Sun God in more than one year, their name would appear multiple times in the `'Artist'` column, once for each year they performed. This would also be a valid reason not to index `sungod` by `'Artist'`.

For the third option, if several different artists performed at Sun God in the same year, that would not necessarily create duplicates in the `'Artist'` column, unless of course two of the artists had the same name, which we've already addressed in the first answer choice. This is not a valid reason to avoid indexing `sungod` by `'Artist'`.

For the last answer choice, if many different artists share the same value of `'Appearance_Order'`, this would not create duplicates in the `'Artist'` column. Therefore, this is also not a valid reason to avoid indexing `sungod` by `'Artist'`.

<average>83</average>

# END SOLUTION

# END PROB
