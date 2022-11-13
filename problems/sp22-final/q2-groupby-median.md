# BEGIN PROB

Complete the expression below so that it evaluates to a DataFrame indexed by `'category'` with one column called `'price'` containing the median cost of the products in each category.

```py
ikea.___(a)___.get(___(b)___)
```

# BEGIN SUBPROB

What goes in blank (a)?

# BEGIN SOLUTION

**Answer: ** `groupby('category').median()`

The question prompt says that the resulting DataFrame should be indexed by `'category'`, so this is a hint that we may want to group by `'category'`. When using `groupby`, we need to specify an aggregation function, and since we're looking for the median cost of all products in a category, we use the `.median()` aggregation function. 

<average>90</average>
# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

What goes in blank (b)?

# BEGIN SOLUTION

**Answer: ** `['price']`

The question prompt also says that the resulting DataFrame should have just one column, the `'price'` column. To keep only certain columns in a DataFrame, we use `.get`, passing in a list of columns to keep. Remember to include the square brackets, otherwise `.get` will return a Series instead of a DataFrame.

<average>76</average>
# END SOLUTION

# END SUBPROB

# END PROB