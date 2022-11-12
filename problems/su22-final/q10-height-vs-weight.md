# BEGIN PROB
Sam wants to fit a linear model to predict a dog's height using its
weight.

He first runs the following code:

```py
x = df.get('weight')
y = df.get('height')

def su(vals):
    return (vals - vals.mean()) / np.std(vals)
```

# BEGIN SUBPROB

Select all of the Python snippets that correctly compute the
correlation coefficient into the variable `r`.

Snippet 1: 
```py
r = (su(x) * su(y)).mean()
```

Snippet 2: 
```py
r = su(x * y).mean()
```

Snippet 3: 
```py
t = 0
for i in range(len(x)):
    t = t + su(x[i]) * su(y[i])
r = t / len(x)
```

Snippet 4: 
```py
t = np.array([])
for i in range(len(x)):
    t = np.append(t, su(x)[i] * su(y)[i])
r = t.mean()
```

[ ] Snippet 1
[ ] Snippet 2
[ ] Snippet 3
[ ] Snippet 4

# BEGIN SOLUTION

**Answer: ** Snippet 1 & 4

- Snippet 1: Recall from the reference sheet, the correlation coefficient is `r = (su(x) * su(y)).mean()`.

- Snippet 2: We have to standardize each variable seperately so this snippet doesnt work.

- Snippet 3: Note that for this snippet we're standardizing each data point within each variable seperately, and so we're not really standardizing the entire variable correctly. In other words, applying `su(x[i])` to a singular data point is just going to convert this data point to zero, since we're only inputting one data point into `su()`.

- Snippet 4: Note that this code is just the same as Snippet 1, except we're now directly computing the product of each corresponding data points individually. Hence this Snippet works.

<average>81</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Sam computes the following statistics for his sample:

<center><img src='../assets/images/su22-final/q10_b.png' width=30%></center>

The best-fit line predicts that a dog with a weight of 10 kg has a
height of 45 cm.

What is the SD of dog heights?

( ) 2
( ) 4.5
( ) 10
( ) 25
( ) 45
( ) None of the above

# BEGIN SOLUTION

**Answer: ** Option 3: 10

The best fit line in original units are given by `y = mx + b` where `m = r * (SD of y) / (SD of x)` and `b = (mean of y) - m * (mean of x)` (refer to reference sheet). Let `c` be the STD of y, which we're trying to find, then our best fit line is now $y = (0.8*c/8)x + (50-(0.8*c/8)*15)$. Plugging the two values they gave us into our best fit line and simplifying gives $45 = 0.1*c*10 + (50 - 1.5*c)$ which simplifies to $45 = 50 - 0.5*c$ which gives us an answer of `c = 10`.
<average>89</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Assume that the statistics in part b) still hold. Select all
of the statements below that are true. (You don't need to finish
part b) in order to solve this question.)

[ ] The relationship between dog weight and height is linear.
[ ] The root mean squared error of the best-fit line is smaller than 5.
[ ] The best-fit line predicts that a dog that weighs 15 kg will be 50 cm tall.
[ ] The best-fit line predicts that a dog that weighs 10 kg will be shorter than 50 cm.

# BEGIN SOLUTION

**Answer: ** Option 3 & 4

- Option 1: We cannot determine whether two variables are linear simply from a line of best fit. The line of best fit just happens to find the best linear relationship between two varaibles, not whether or not the variables have a linear relationship.

- Option 2: To calculate the root mean squared error, we need the actual data points so we can calculate residual values. Seeing that we don't have access to the data points, we cannot say that the root mean squared error of the best-fit line is smaller than 5.

- Option 3: This is true accrding to the problem statement given in part b

- Option 4: This is true since we expect there to be a positive correlation between dog height and weight. So dogs that are lighter will also most likely be shorter. (ie a dog that is lighter than 15 kg will most likely be shorter than 50cm)

<average>72</average>

# END SOLUTION

# END SUBPROB

# END PROB
