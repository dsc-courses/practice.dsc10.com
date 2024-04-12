# BEGIN PROB

Suppose `x` and `y` are both `int`s that have been previously defined,
with `x < y`. Now, define:

    peach = np.arange(x, y, 2)

Say that the *spread* of `peach` is the difference between the largest
and smallest values in `peach`. The spread should be a non-negative
integer.

# BEGIN SUBPROB

**Using array methods**, write an expression that evaluates to the
spread of `peach`.

# BEGIN SOLUTION

**Answer:** `peach.max() - peach.min()`

<average>62</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

**Without using any methods or functions**, write an expression that
evaluates to the spread of `peach`.\
*Hint:* Use `[ ]`.

# BEGIN SOLUTION

**Answer:** `peach[len(peach) - 1] - peach[0]`  or `peach[-1] - peach[0]`

<average>36</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Choose the correct way to fill in the blank in this sentence:

::: center
*The spread of* `peach` *is* ______ *the value of* `y - x`.
:::

( ) always less than
( ) sometimes less than and sometimes equal to
( ) always greater than
( ) sometimes greater than and sometimes equal to
( ) always equal to

# BEGIN SOLUTION

**Answer:** always less than

<average>48</average>

# END SOLUTION

# END SUBPROB

# END PROB