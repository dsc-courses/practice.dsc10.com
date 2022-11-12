# BEGIN PROB

The `sums` function takes in an array of numbers and outputs the
cumulative sum for each item in the array. The cumulative sum for an
element is the current element plus the sum of all the previous
elements in the array.

For example:

```py
>>> sums(np.array([1, 2, 3, 4, 5]))
array([1, 3, 6, 10, 15])
>>> sums(np.array([100, 1, 1]))
array([100, 101, 102])
```

The incomplete definition of `sums` is shown below.

```py
def sums(arr):
    res = _________
             (a)
    res = np.append(res, arr[0])
    for i in _________:
                (b)
        res = np.append(res, _________)
                                (c)
    return res
```

# BEGIN SUBPROB

Fill in blank (a).

# BEGIN SOLUTION

**Answer: ** `np.array([])` or `[]`

`res` is the list in which we'll be storing each cumulative sum. Thus 
we start by initializing `res` to an empty array or list. 

<average>100</average>
# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Fill in blank (b).

# BEGIN SOLUTION

**Answer: ** `range(1, len(arr))` or `np.arange(1, len(arr))`

We're trying to loop through the indices of `arr` and calculate the cumulative
sum corresponding to each entry. To access each index in sequential order, we simply 
use `range()` or `np.arange()`. However, notice that we have already appended the first entry of `arr` 
to `res` on line 3 of the code snippet. (Note that the first entry of `arr` is 
the same as the first cumulative sum.) Thus the lower bound of `range()` (or `np.arange()`) actually 
starts at 1, not 0. The upper bound is still `len(arr)` as usual. 

<average>64</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Fill in blank (c).

# BEGIN SOLUTION

**Answer: ** `res[i - 1] + arr[i]` or `sum(arr[:i + 1])`

Looking at the syntax of the problem, the blank we have to fill essentially
requires us to calculate the current cumulative sum, since the rest of line will 
already append the blank to `res` for us. One way to think of a cumulative sum is 
to add the "current" `arr` element to the previous cumulative sum, 
since the previous cumulative sum encapsulates all the previous elements. 
Because we have access to both of those values, we can easily represent it as 
`res[i - 1] + arr[i]`. The second answer is more a more direct approach. Because the cumulative 
sum is just the sum of all the previous elements up to the current element, we 
can directly compute it with `sum(arr[:i + 1])`

<average>71</average>

# END SOLUTION

# END SUBPROB

# END PROB
