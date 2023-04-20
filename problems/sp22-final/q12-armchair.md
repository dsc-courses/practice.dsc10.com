# BEGIN PROB

An IKEA chair designer is experimenting with some new ideas for armchair designs. She has the idea of making the arm rests shaped like bell curves, or normal distributions. A cross-section of the armchair design is shown below. 

<center><img src='../assets/images/sp22-final/armchair.png' width=80%></center>
<br>

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

**Answer: ** `z>4` or `z>=4`

The body of the function contains an `if` statement followed by a `return` statement, which executes only when the `if` condition is false. In that case, the function returns `scipy.stats.norm.cdf(z)`, which is the area under the standard normal curve to the left of `z`. When `z` is in the left half of the armchair curve, the area under the armchair curve to the left of `z` is the area under the standard normal curve to the left of `z` because the left half of the armchair curve is a standard normal curve, centered at 0. So we want to execute the `return` statement in that case, but not if `z` is in the right half of the armchair curve, since in that case the area to the left of `z` under the armchair curve should be more than 1, and `scipy.stats.norm.cdf(z)` can never exceed 1. This means the `if` condition needs to correspond to `z` being in the right half of the armchair curve, which corresponds to `z>4` or `z>=4`, either of which is a correct solution. 

<average>72</average>
# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

What goes in blank (b)?

# BEGIN SOLUTION

**Answer: ** `1+scipy.stats.norm.cdf(z-8)`

This blank should contain the value we want to return when `z` is in the right half of the armchair curve. In this case, the area under the armchair curve to the left of `z` is the sum of two areas:

1. the area under the entire left half of the armchair curve, which is 1, and
2. the area under the portion of the right half of the armchair curve that falls to the left of `z`. 

Since the right half of the armchair curve is just a standard normal curve that's been shifted to the right by 8 units, the area under that normal curve to the left of `z` is the same as the area to the left of `z-8` on the standard normal curve that's centered at 0. Adding the portion from the left half and the right half of the armchair curve gives `1+scipy.stats.norm.cdf(z-8)`.

For example, if we want to find the area under the armchair curve to the left of 9, we need to total the yellow and blue areas in the image below. 

<center><img src='../assets/images/sp22-final/armchair-shaded.png' width=80%></center>

The yellow area is 1 and the blue area is the same as the area under the standard normal curve (or the left half of the armchair curve) to the left of 1 because 1 is the point on the left half of the armchair curve that corresponds to 9 on the right half. In general, we need to subtract 8 from a value on the right half to get the corresponding value on the left half.

<average>54</average>
# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

What goes in blank (c)?

# BEGIN SOLUTION

**Answer: ** `area_left_of(y) - area_left_of(x)`

In general, we can find the area under *any* curve between `x` and `y` by taking the area under the curve to the left of `y` and subtracting the area under the curve to the left of `x`. Since we have a function to find the area to the left of any given point in the armchair curve, we just need to call that function twice with the appropriate inputs and subtract the result. 

<average>60</average>
# END SOLUTION

# END SUBPROB

# END PROB