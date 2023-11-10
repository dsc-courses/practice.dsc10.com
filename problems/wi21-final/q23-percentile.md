# BEGIN PROB

<span style="color:red"><b>Note: This problem is out of scope; it covers material no longer included in the course.</b></span>

Recall the mathematical definition of percentile and how we calculate it.

| Let *p* be a number between 0 and 100. The *p*th percentile of a collection is the smallest 
| value in the collection that is at least as large as *p*% of all the values. 

By this definition, any percentile between 0 and 100 can be computed for any collection of values and is always an element of the collection. Suppose there are *n* elements in the collection. To find the 
*p*th percentile:

1. Sort the collection in increasing order.
2. Find *p*% of *n*: (*p*/100) *n*. Call that *h*. If *h* is an integer, define *k*=*h*. Otherwise, let *k* be the smallest integer greater than *h*.
3. Take the *k*th element of the sorted collection.

You have a dataset of 7 values, which are ``[3, 6, 7, 9, 10, 15, 18]``. Using the mathematical definition of percentile above, find the smallest and largest integer values of p so that the pth percentile of this dataset corresponds to the value 10. Input your answers below, **as integers between 0 and 100**.

# BEGIN SUBPROB

`Smallest = _`

# BEGIN SOLUTION

**Answer: ** 58

From the definition provided in the question, we want all values of (p/100) * n which will yield
an integer larger than 4, but less than or equal to 5 because we want the 5th element (10) in the dataset. To approach this problem
we can find how many percentiles each piece of data falls within by taking 100 / 7 which yields around
14.3. Wanting to find the percentiles for the range of 4 to 5 we can multiple (100/7) by 4 to get our lower bound.
(100/7) * 4 = 57.14 which is rounded up to 58 since the 57th percentile belongs to the 4th element
while 58 belongs to the fifth element. 

<average>73</average>
# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

`Largest = _`
# BEGIN SOLUTION

**Answer: ** 71

To find the largest we will take (100/7) * 5 which yields 71.43. We will round down since the 72th percentile belongs
to the sixth element in the data set. For more information look at the solution above.

<average>74</average>
# END SOLUTION

# END SUBPROB

# END PROB
