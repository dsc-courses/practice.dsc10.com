# BEGIN PROB

What was the largest number of artists that ever performed in a single Sun God festival? **Select all expressions that evaluate to the correct answer.**

[ ] `sungod.groupby('Appearance_Order').count().get('Year').max()`
[ ] `sungod.groupby('Year').count().get('Artist').max()`
[ ] `sungod.get('Appearance_Order').max()`
[ ] `sungod.groupby('Year').max().get('Year').max()`
[ ] None of the above.

# BEGIN SOLUTION

**Answer: ** `sungod.groupby('Year').count().get('Artist').max()`, `sungod.get('Appearance_Order').max()`

Let's go through all the answer choices.

For the first option, `sungod.groupby('Appearance_Order').count()` will create a DataFrame with one row for each unique value of `'Appearance_Order'`, and each column will contain the same value, which represents the number of Sun God festivals that had at least a certain amount of performers. For example, the first row of `sungod.groupby('Appearance_Order').count()` will correspond to an `'Appearance_Order'` of 1, and each column will contain a count of the number of Sun God festivals with at least one performer. Since every festival has at least one performer, the largest count in any column, including `'Year'` will be in this first row. So `sungod.groupby('Appearance_Order').count().get('Year').max()` represents the total number of Sun God festivals, which is not the quantity we're trying to find.

For the second option, `sungod.groupby('Year').count()` will create a DataFrame with one row per year, with each column containing a count of the number of artists that performed in that year's festival. If we take the largest such count in any one column, we are finding the largest number of artists that ever performed in a single Sun God festival. Therefore,
`sungod.groupby('Year').count().get('Artist').max()` is correct. 

The third option works because we can find the desired quantity by simply looking for the largest value in the `'Appearance_Order'` column. For example, if the largest number of artists to ever perform in a Sun God festival was, say, 17, then for that year's festival, the last artist to appear would have a value of 17 in the `'Appearance_Order'` column. There can be no 18 anywhere in the `'Appearance_Order'` column, otherwise that would mean there was some festival with 18 performers. Therefore, `sungod.get('Appearance_Order').max()` is correct.

The fourth option is not even correct Python code. The DataFrame produced by `sungod.groupby('Year').max()` is indexed by `'Year'` and no longer has `'Year'` as a column. So we'd get an error if we tried to access this nonexistent column, as in `sungod.groupby('Year').max().get('Year')`. 

<average>78</average>


# END SOLUTION

# END PROB
