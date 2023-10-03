# BEGIN PROB

Suppose we have imported the `math` module using `import math`. Consider the nested expression below:
<div align="center">

`int(math.sqrt(math.pow(4 * 2 ** 4, min(9 % 4, 9 / 4, 9 - 4))))`

</div>

# BEGIN SUBPROB

How many function calls are there in this expression? How many arguments does each function have?

# BEGIN SOLN

**Answer:** 4 function calls: one argument for `int()`, one for `math.sqrt()`, two for `math.pow()`, three for `min()`.

There are four function calls. One is a call to the type-conversion function `int()`, which takes one argument. Another is a call to `math.sqrt()`, which takes one argument. Another is a call to `math.pow()`, which takes two arguments. Finally is a call to the built-in function `min()`, which in this case takes three arguments, but generally can take two or more arguments.

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

What does this expression evaluate to?

# BEGIN SOLN

**Answer:** 8

For nested evaluation, it is helpful to work from the inside out. Let's evaluate some arithmetic expressions first. `9 % 4` evaluates to `1` because when we divide `9` by `4`, there is a remainder of `1`. Additionally, `9 / 4` evaluate to `2.25`, and `9 - 4` evaluates to `5`. Starting with the inner most function call, we see `min(9 % 4, 9 / 4, 9 - 4)` is equiavlent to `min(1, 2.25, 5)` which evaluates to `1`. 

The next-most inner function call is the call to `math.pow()` which takes two arguments: a number for the base, and a number for the exponent. We've already evaluated the exponent, but we need to evaluate the base of `4 * 2 ** 4`.  Using the order of operations, we know we need to evaluate the exponent first. So `4 * 2 ** 4 ` is equivalent to `4 * 16` or `64`.

Therefore, `math.pow(4 * 2 ** 4, min(9 % 4, 9 / 4, 9 - 4))` simplifies to `math.pow(64, 1)`, which Python evaluates to be `64.0`, a `float`. 

Next, `math.sqrt(64.0)` evaluates to `8.0`. Finally, the type conversion function `int(8.0)` evaluates to `8`.

# END SOLN

# END SUBPROB

# END PROB