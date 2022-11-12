# BEGIN PROB

Suppose `df` is a DataFrame and `b` is any boolean array whose length is the same as the number of rows of `df`. 

True or False: For any such boolean array `b`, `df[b].shape[0]` is less than or equal to `df.shape[0]`.

( ) True
( ) False

# BEGIN SOLUTION

**Answer: ** True

The brackets in `df[b]` perform a query, or filter, to keep only the rows of `df` for which `b` has a `True` entry. Typically, `b` will come from some condition, such as the entry in a certain column of `df` equaling a certain value. Regardless, `df[b]` contains a subset of the rows of `df`, and `.shape[0]` counts the number of rows, so `df[b].shape[0]` must be less than or equal to `df.shape[0]`.

<average>86</average>
# END SOLUTION

# END PROB