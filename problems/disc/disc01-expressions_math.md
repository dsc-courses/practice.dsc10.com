# BEGIN PROB

Suppose we have imported the `math` module using `import math`. Consider the nested expression below:
`int(math.sqrt(math.pow(4 * 2 ** 4, min(9 % 4, 9 / 4, 9 - 4))))`

# BEGIN SUBPROB

1. How many function calls are there in this expression? How many arguments does each function have?

# BEGIN SOLN

There are four function calls. One is a call to the type-conversion function `int`, which takes one argument. Another is a call to `math.sqrt()`, which takes one argument. Another is a call to `math.pow()`, which takes two arguments. Finally is a call to the built-in function `min()`, which in this case takes three arguments, but generally can take two or more arguments.

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

2. What does this expression evaluate to?

# BEGIN SOLN

8

For these questions, it is helpful to work from the inside out. Starting with the inner most function call, we see `min(9 % 4, 9 / 4, 9 - 4)`, which will output to 1 because 9 % 4 outputs to 1, 9 / 4 outputs to 2.25, and 9 - 4 outputs to 5, and because we would like the minimum of those three expressions, 1 is the output. Now working from the next most inner function call, we see that we are calling `math.pow(4 * 2 ** 4, min(9 % 4, 9 / 4, 9 - 4))`. Because we have already solved for the innermost function, we can rewrite this to be `math.pow(4 * 2 ** 4, 1)`. This will evaluate to 64.0, because `4 * 2 ** 4` evaluates to 64.0 (4 * 2^4), and we are raising 64.0 to the first power which is simply just 64.0 . Now working to the next most inner function, we see that we have `math.sqrt(math.pow(4 * 2 ** 4, min(9 % 4, 9 / 4, 9 - 4)))`. Again, we can rewrite the inside of `math.sqrt(math.pow(4 * 2 ** 4, min(9 % 4, 9 / 4, 9 - 4)))` to just `math.sqrt(64.0)` because we have just evaluated that `math.pow(4 * 2 ** 4, min(9 % 4, 9 / 4, 9 - 4))` outputs to 64.0 . Now solving for `math.sqrt(64.0)` we get 8.0 because the squareroot of 64.0 is 8.0 . Now to solve for the last function call, we see that we have `int(math.sqrt(math.pow(4 * 2 ** 4, min(9 % 4, 9 / 4, 9 - 4))))`. For the last time, we can rewrite that call as simply `int(8.0)` because we have just evaluated that `math.sqrt(math.pow(4 * 2 ** 4, min(9 % 4, 9 / 4, 9 - 4)))` ouputs to 8.0. Now evaluating for `int(8.0)`, it simply ouputs to 8 because we are changing the datatype of 8.0 from a float to an int. 

# END SOLN

# END SUBPROB

# END PROB