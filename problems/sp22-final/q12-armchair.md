# BEGIN PROB

An IKEA chair designer is experimenting with some new ideas for armchair designs. She has the idea of making the arm rests shaped like bell curves, or normal distributions. A cross-section of the armchair design is shown below. 

<center><img src='../assets/images/sp22-final/armchair.png' width=80%></center>

This was created by taking the portion of the standard normal distribution from $z=-4$ to $z=4$ and adjoining two copies of it, one centered at $z=0$ and the other centered at $z=8$. Let's call this shape the armchair curve.

Since the area under the standard normal curve from $z=-4$ to $z=4$ is approximately 1, the total area under the armchair curve is approximately 2.

Complete the implementation of the two functions below:

1. `area_left_of(z)` should return the area under the armchair curve to the left of `z`, assuming `-4 <= z <= 12`, and 
2. `area_between(x, y)` should return the area under the armchair curve between `x` and `y`, assuming `-4 <= x <= y <= 12`. 


```py
import scipy

def area_left_of(z):
    '''Returns the area under the armchair curve to the left of z.
       Assume -4 <= z <= 12'''
    if ___(a)___: 
        return ___(b)___ 
    return scipy.stats.norm.cdf(z)

def area_between(x, y):
    '''Returns the area under the armchair curve between x and y. 
    Assume -4 <= x <= y <= 12.'''
    return ___(c)___
```


# BEGIN SUBPROB

What goes in blank (a)?

# BEGIN SOLUTION

**Answer: ** `z>4`

solution here

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

What goes in blank (b)?

# BEGIN SOLUTION

**Answer: ** `scipy.stats.norm.cdf(z-8)+1`

solution here

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

What goes in blank (c)?

# BEGIN SOLUTION

**Answer: ** `area_left_of(y) - area_left_of(x)`

solution here

# END SOLUTION

# END SUBPROB

# END PROB