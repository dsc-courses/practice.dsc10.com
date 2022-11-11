# BEGIN PROB

Fill in the blank in the code below so that `chronological` is a DataFrame with the same rows as `sungod`, but ordered chronologically by appearance on stage. That is, earlier years should come before later years, and within a single year, artists should appear in the DataFrame in the order they appeared on stage at Sun God. Note that `groupby` automatically sorts the index in ascending order.

```py
chronological = sungod.groupby(___________).max().reset_index()
```


( ) `['Year', 'Artist', 'Appearance_Order']`
( ) `['Year', 'Appearance_Order']`
( ) `['Appearance_Order', 'Year']`
( ) None of the above.

# BEGIN SOLUTION

**Answer: ** `['Year', 'Appearance_Order']`

The fact that `groupby` automatically sorts the index in ascending order is important here. Since we want earlier years before later years, we could group by `'Year'`, however if we *just* group by year, all the artists who performed in a given year will be aggregated together, which is not what we want. Within each year, we want to organize the artists in ascending order of `'Appearance_Order'`. In other words, we need to group by `'Year'` with `'Appearance_Order'` as subgroups. Therefore, the correct way to reorder the rows of `sungod` as desired is `sungod.groupby(['Year', 'Appearance_Order']).max().reset_index()`. Note that we need to reset the index so that the resulting DataFrame has `'Year'` and `'Appearance_Order'` as columns, like in `sungod`.

<average>85</average>


# END SOLUTION

# END PROB
