# BEGIN PROB

One way to use `np.arange` to produce the sequence `[2, 6, 10, 14]` is `np.arange(2, 15, 4)`. This gives three inputs to np.arange. 

Fill in the blanks below to show a different way to produce the same sequence, this time using only one input to np.arange.  Each blank below must be filled in with a single number only, and the final result, `x*np.arange(y)+z`, must produce the sequence `[2, 6, 10, 14]`.

Using `x*np.arange(y)+z` fill in the missing values:

`x = _`

`y = _`

`z = _`

# BEGIN SOLUTION

**Answer: ** 

`x = 4`, `y = 4`, `z = 2`

The question states that we are trying to create the sequence `[2, 6, 10, 14]` by filling in the blanks for the statement `x*np.arange(y)+z`. If we look at the sequence we are attempting to derive, we can see that each step in the sequence increments by 4. Similarly, we can see that the sequence begins at 2. We know that passing an argument by itself in `np.arange` will increment up to that number (for example `np.arange(4)` will produce the sequence `[0,1,2,3]`). Knowing this, we can create this sequence by setting y to 4. Attempting to reach the desired sequence of `[2, 6, 10, 14]` from `[0, 1, 2, 3]` we can multiply each number by 4 by setting x to 4 and instantiate the sequence at 2 by setting z as 2. 

<average>96</average>
# END SOLUTION

# END PROB
