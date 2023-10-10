# BEGIN PROB

Consider the expression `(np.arange(a, b, c) * np.arange(d, e, f))[2]`. Given the values:

* `a = 1`
* `b = 7`
* `c = 2.5`
* `d = 8`
* `e = 2`
* `f = -2`

Evalute the expression.

# BEGIN SOLN

**Answer:** `24.0`

This question although is daunting at first, is best solved by breaking up the question into parts. First, let us think about the first part, `np.arange(a, b, c)`. Given in the problem, we know that the values of a, b, and c are 1, 7, and 2.5, so let us rewrite `np.arange(a, b, c)` to `np.arange(1, 7, 2.5)`. Now, we must figure out what `np.arange()` does. What `np.arange()` does is it creates a numpy array that contains regularly spaces values between a start value and an end value (start is inclusive, end is exclusive). So in this first case, our starting value is 1, our end value is 7, and the regular interval or step size is 2.5. So this call, `np.arange(1, 7, 2.5)`, will output the numpy array `[1.0, 3.5, 6.0]` because we start at 1, and continue adding 2.5 until we hit a value that is greater than or equal to 7. Now that we have evaluated the first half, let us now solve for `np.arange(d, e, f)`. Again, we can rewrite this to be `np.arange(8, 2, -2)` because d, e, and f are given to us in the problem. Now this part may seem a little tricky because of the negative regular interval (step size), but it is the same logic as before. The output will simply be `[8, 6, 4]`. In order to get that, we start at 8, and continue to decrease our start value by 2 till we reach a number that is less than or equal to 2. Now that we have evaluated both `np.arange(a, b, c)` and `np.arange(d, e, f)`, it is now time to multiply. Multiplication of two numpy arrays is simply a pair wise multiplication. So in our case, we will be multiplying `[1.0, 3.5, 6.0] * [8, 6, 4]`, which results to `[8.0, 21.0, 24.0]`. Now that we have evaluated `(np.arange(a, b, c) * np.arange(d, e, f))` to be `[8.0, 21.0, 24.0]`, we now just need to access the element `[2]`, which is `24.0`. 

# END SOLN

# END PROB