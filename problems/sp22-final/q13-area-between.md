# BEGIN PROB

Suppose you have correctly implemented the function `area_between(x, y)` so that it returns the area under the armchair curve between `x` and `y`, assuming the inputs satisfy `-4 <= x <= y <= 12`. 

**Note:** You can still do this question, even if you didn't know how to do the previous one. 

# BEGIN SUBPROB

What is the approximate value of `area_between(-2, 10)`?

( ) 1.9
( ) 1.95
( ) 1.975
( ) 2

# BEGIN SOLUTION

**Answer: ** 1.95

The area we want to find is shown below in two colors. We can find the area in each half of the armchair curve separately and add the results.

<center><img src='../assets/images/sp22-final/armchair-between-1.png' width=80%></center>

For the yellow area, we know that the area within 2 standard deviations of the mean on the standard normal curve is 0.95. The remaining 0.05 is split equally on both sides, so the yellow area is 0.975.

The blue area is the same by symmetry so the total shaded area is $0.975*2 = 1.95$. 

Equivalently, we can use the fact that the total area under the armchair curve is 2, and the amount of unshaded area on either side is 0.025, so the total shaded area is $2 - (0.025*2) = 1.95.$

<average>76</average>
# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

What is the approximate value of `area_between(0.37, 8.37)`?

( ) 0.68
( ) 0.95
( ) 1
( ) 1.5

# BEGIN SOLUTION

**Answer: ** 1

The area we want to find is shown below in two colors. 

<center><img src='../assets/images/sp22-final/armchair-between-2.png' width=80%></center>

As we saw in Problem 12.2, the point on the left half of the armchair curve that corresponds to 8.37 is 0.37. This means that if we move the blue area from the right half of the armchair curve to the left half, it will fit perfectly, as shown below. 

<center><img src='../assets/images/sp22-final/armchair-between-3.png' width=80%></center>

Therefore the total of the blue and yellow areas is the same as the area under one standard normal curve, which is 1.

<average>76</average>
# END SOLUTION

# END SUBPROB

# END PROB