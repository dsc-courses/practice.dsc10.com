# BEGIN PROB

Write one line of code below to create a DataFrame called `openers` containing the artists that appeared first on stage at a past Sun God festival. The DataFrame `openers` should have all the same columns as `sungod`. 

It's okay if you need to write on two lines to fit into the provided space, as long as your answer would be one line of Python code.

# BEGIN SOLUTION

**Answer: ** `openers = sungod[sungod.get('Appearance_Order')==1]`

Since we want only certain rows of `sungod`, we need to query. The condition to satisfy is that the 'Appearance_Order' column should have a value of 1 to indicate that this artist performed first in a certain year's festival.

# END SOLUTION

# END PROB