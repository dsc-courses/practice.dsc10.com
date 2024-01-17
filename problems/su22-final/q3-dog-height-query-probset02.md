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
interested in whether each unique `'kind'` of dog fits some sort of constraint.
We don't quite perform querying yet since we need to group the DataFrame first. 
In other words, we first need to group the DataFrame into each 
`'kind'` before we could apply any sort of boolean conditionals.

<average>97</average>
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

<average>94</average>
# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Fill in blank (c).

# BEGIN SOLUTION

**Answer: ** `(foo.get('weight') > 20 | foo.get(`height`) > 40)`

Once we have grouped the dogs by `'kind'` and have calculated the average 
stats of each kind of dog, we can do some querying with two conditionals:
`foo.get('weight') > 20` gets the kinds of dogs that are heavier 
than 20 kg on average and `foo.get('height') > 40)` gets the kinds of dogs that
 are taller than 40 cm on average. We combine these two conditions with the 
`|` operator since we want the kind of dogs that satisfy either condition.

<average>93</average>
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

Note that earlier, we did `groupby('kind')`, which automatically sets each unique
 `'kind'` as the index. Since this is what we want anyways, simply doing `.index`
 will give us all the kinds of dogs that satisfy the given conditions.

 <average>94</average>
# END SOLUTION

# END SUBPROB

# END PROB
