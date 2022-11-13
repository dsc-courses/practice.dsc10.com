# BEGIN PROB

Suppose in a new cell, we type the following.

```py
    sungod.sort_values(by='Year')
```

After we run that cell, we type the following in a second cell.

```py
    sungod.get('Artist').iloc[0]
```

What is the output when we run the second cell? Note that the first Sun God festival was held in 1983.

( ) `'Blues Traveler'`
( ) The artist who appeared on stage first in 1983.
( ) An artist who appeared in 1983, but not necessarily the one who appeared first.
( ) Not enough information to tell.

# BEGIN SOLUTION

**Answer: ** `'Blues Traveler'`

In the first cell, although we seem to be sorting `sungod` by `'Year'`, we aren't actually changing the DataFrame `sungod` at all because we don't save the sorted DataFrame. Remember that DataFrame methods don't actually change the underlying DataFrame unless you explicitly make that happen by saving the output as the name of the DataFrame. So the first `'Artist'` name will still be `'Blues Traveler'`. 

Suppose we had saved the sorted DataFrame as in the code below.

```py
    sungod = sungod.sort_values(by='Year')   
    sungod.get('Artist').iloc[0]
```

In this case, the output would be the name of an artist who appeared in 1983, but not necessarily the one who appeared first. There will be several artists associated with the year 1983, and we don't know which of them will be first in the sorted DataFrame.

<average>12</average>

# END SOLUTION

# END PROB
