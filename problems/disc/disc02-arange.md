# BEGIN PROB

Evaluate the expression `(np.arange(1, 7, 2.5) * np.arange(8, 2, -2))[2]` .

# BEGIN SOLN

**Answer:** `24.0`

This question although is daunting at first, is best solved by breaking up the question into parts. First, let us think about the first part, `np.arange(1, 7, 2.5)`. In order to answer this, we must figure out what `np.arange()` does. What `np.arange()` does is it creates a `numpy` array that contains regularly spaces values between a start value and an end value (start is inclusive, end is exclusive). So in this first case, our starting value is 1, our end value is 7, and the regular interval or step size is 2.5. So this call, `np.arange(1, 7, 2.5)`, will output the `numpy` array `np.array([1.0, 3.5, 6.0])` because we start at 1, and continue adding 2.5 stopping at the last value that's less than 7. The reason the resulting `np.array([])` containts all `float` values is because one of the numbers is not an `int`, and all elements in the array have to have the same data type. Now that we have evaluated the first half, let us now solve for `np.arange(8, 2, -2)`. Now this part may seem a little tricky because of the negative regular interval (step size), but it is the same logic as before. The output will simply be `np.array([8, 6, 4])`. In order to get that, we start at 8, and continue to decrease our start value by 2 stopping before we reach 2. Now that we have evaluated both `np.arange(1, 7, 2.5)` and `np.arange(8, 2, -2)`, it is now time to multiply. 

Multiplication of two `numpy` arrays is simply a pair wise multiplication. So in our case, we will be multiplying `np.array([1.0, 3.5, 6.0]) * np.array([8, 6, 4])`, which results to `np.array([8.0, 21.0, 24.0])`. Again, paying attention to the datatypes, the reason that `np.array([8.0, 21.0, 24.0])` contains `float` values rather than `int` values is because when you multiply an `int` by a `float`, your answer will be a `float`. Now that we have evaluated `(np.arange(1, 7, 2.5) * np.arange(8, 2, -2))` to be `np.array([8.0, 21.0, 24.0])`, we now just need to access the element in position 2, which is `24.0`. 

# END SOLN

# END PROB