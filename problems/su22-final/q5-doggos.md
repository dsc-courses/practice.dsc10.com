# BEGIN PROB
Shivani wrote a function called `doggos` defined as follows:

```py
def doggos(n, lower, upper):
    t = df.sample(n, replace=True).get('longevity')
    return sum(lower <= t < upper)
```

This plot shows a density histogram of the `'longevity'` column.

<center><img src='../assets/images/su22-final/q5_hist.png' width=50%></center>

Answer each of these questions by either writing a **single number** in the box
or selecting "Not enough information", but **not both**. What is the 
probability that:

# BEGIN SUBPROB

`doggos(1, 10, 11) == 1` is `True`?

# BEGIN SOLUTION

**Answer: ** 0.15

Let's first understand the function. The function takes inputs `n`, `lower`, and `upper`
and randomly takes a sample of `n` rows with replacement from DataFrame `df`, gets column 
`longevity` from the sample and saves it as a Series `t`. The `n` entries of `t` are randomly
generated according to the density histogram shown in the picture. That is, 
the probability of a particular value being generated in Series `t` for a given 
entry can be visualized by the density histogram in the picture. `lower <= t < upper`
takes `t` and generates a Series of boolean values, either `True` or `False`
depending on whether the corresponding entry in `t` lies within the range. And so 
`sum(lower <= t < upper)` returns the number of entries in `t` that lies between the range values. (This is because `True` has a value of 1 and `False` has a value of 0, so summing Booleans is a quick way to count how many `True` there are.)

Now part a is just asking for the probability that we'll draw a `longevity` value (given that `n` is `1`, so we only draw one `longevity` value)
between 10 and 11 given the density plot. Note that the probability of a bar is 
given by the width of the bar multiplied by the height. Now looking at the bar 
with bin of range 10 to 11, we can see that the probability is just $(11-10) * 0.15 = 1 * 0.15 = 0.15$.

<average>86</average>
# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

`doggos(2, 0, 12) == 2` is `True`?

# BEGIN SOLUTION

**Answer: ** 0.36

Part b is essentially asking us: What is the probability that after drawing two
`longevity` values according to the density plot, both of them will lie in between
0 and 12?

Let's first start by considering the probability of drawing 1 `longevity` value
that lies between `0` and `12`. This is simply just the sum of the areas of the
three bars of range 6-10, 10-11, and 11-12, which is just 
$(4*0.05) + (1*0.15) + (1*0.25) = 0.6$
 
Now because we draw each value independently from one another, we simply 
square this probability which gives us an answer of $0.6*0.6 = 0.36$

<average>81</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

`doggos(2, 13, 20) > 0` is `True`?

# BEGIN SOLUTION

**Answer: ** 0.19

Part c is essentially asking us: What is the probability that after drawing two
`longevity` values according to the density plot, at least one of them will lie in between
12 and 20?

While you can directly solve for this probability, a faster method would be to 
solve for the complementary of this problem. That is, we can solve for the 
probability that **none** of them lie in between the given ranges. And once we 
solve this, we can simply subtract our answer from one, because the only options 
for this scenario is that either at least one of the values lie in between the 
range, or neither of the values do.

Again, let's solve for the probability of drawing 1 `longevity` value that isn't
between the range. Staying true to our complementary strategy, this is just 1 
minus the probability of drawing a `longevity` value that **is** in the range,
which is just $1 - (1*0.05+1*0.05) = 0.9$

Again, because we draw each value independently, squaring this probability 
gives us the probability that neither of our drawn values are in the range, or
$0.9*0.9 = 0.81$. Finally, subtracting this from 1 gives us our desired answer or
$1 - 0.81 =0.19$

<average>66</average>
# END SOLUTION

# END SUBPROB

# END PROB
