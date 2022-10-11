# BEGIN PROB

The following code computes an array containing the unique kinds of
dogs that are heavier than 20 kg **or** taller than 40 cm on
average.

```py
foo = df.__(a)__.__(b)__
np.array(foo[__(c)__].__d__)
```

# BEGIN SUBPROB

Fill in blank (a).

# BEGIN SOLUTION

**Answer: ** `groupby('kind')` 

We start this problem by grouping the dataframe by `'kind'` since we're only 
focusing on whether each unique `'kind'` of dog fits some sort of constraint.
We don't quite perform querying yet since we need to sort the data frame into 
groups first. In other words, we first need to group the data frame into each 
`'kind'` before we could apply any sort of boolean conditionals.


# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Fill in blank (b).

# BEGIN SOLUTION

**Answer: ** `.mean()` 

After we do `.groupby('kind')`, we need to apply `.mean()` since the problem asks if 
each unique `'kind'` of dog satisfies certain constraints **on average**. 
`.mean()` calculates the average of each column of each group which is what 
we want.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Fill in blank (c).

# BEGIN SOLUTION

**Answer: ** `(foo.get('weight') > 20 | foo.get(`height`) > 40)`

Once we have grouped the dogs by `'kind'` and have calculated the average 
stats of each kind of dog, we can do some querying with two conditionals:
`foo.get('weight') > 20` filters out the kinds of dogs that have an average 
weight of at least 20 and `foo.get('height') > 40)` filters out the kinds of 
dogs that have a height at least 40. We combine these two conditions with the 
`|` operator since we want the kind of dogs that satisfy either condition.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Which of the following should fill in blank (d)?

( ) `.index`
( ) `.unique()`
( ) `.get('kind')`
( ) `.get(['kind'])`

# BEGIN SOLUTION

**Answer: ** `.index` 

Finally, we take the indeces of the final data frame since we're left with a
bunch of rows of which the kind of dog satisfies the given conditions. Note 
that we use `.index` instead of `.get('kind')` because early we did 
`groupby('kind')`, which automatically creates a data frame with `'kind'` as 
the index.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Let's say that right after blank (b), we added `reset_index()`. 
Now, which of the following should fill in blank (d)?

( ) `.index`
( ) `.unique()`
( ) `.get('kind')`
( ) `.get(['kind'])`

# BEGIN SOLUTION

**Answer: ** `.get('kind')`

Now that we have reset the index of the dataframe, `kind` is once again its
own column so we could simply do `.get('kind')`.

# END SOLUTION

# END SUBPROB

# END PROB
