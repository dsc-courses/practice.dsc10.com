# BEGIN PROB

You have a DataFrame called `prices` that contains information about food prices at 18 different grocery stores. There is column called `'broccoli'` that contains the price in dollars for one pound of broccoli at each grocery store. There is also a column called `'ice_cream'` that contains the price in dollars for a pint of store-brand ice cream.

# BEGIN SUBPROB

What should `type(prices.get('broccoli').iloc[0])` output?

( ) int
( ) float
( ) array
( ) Series

# BEGIN SOLUTION

**Answer: ** float

This code extracts the first entry of the `'broccoli'` column. Since this column contains prices in dollars for a pound of broccoli, it makes sense to represent such a price using a float, because the price of a pound of broccoli is not necessarily an integer.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

The code
`prices.plot(kind='hist', y='broccoli', bins=np.arange(0.8, 2.11, 0.1), density=True)` 
produces the histogram below.


How many grocery stores sold broccoli for a price greater than or equal to $1.30 per pound, but less than $1.40 per pound (the tallest bar)? 

# BEGIN SOLUTION

**Answer: ** 4 grocery stores

We are given that the bins start at 0.8 and have a width of 0.1, which means one of the bins has endpoints 1.3 and 1.4. This bin (the tallest bar) includes all grocery stores that sold broccoli for a price greater than or equal to $1.30 per pound, but less than $1.40 per pound.

This bar has a width of 0.1 and we'd estimate the height to be around 2.2, though we can't say exactly. Multiplying these values, the area of the bar is about 0.22, which means about 22 percent of the grocery stores fall into this bin. There are 18 grocery stores in total, as we are told in the introduction to this question. We can compute using a calculator that 22 percent of 18 is 3.96. Since the actual number of grocery stores this represents must be a whole number, this bin must represent 4 grocery stores. 

The reason for the slight discrepancy between 3.96 and 4 is that we used 2.2 for the height of the bar, a number that we determined by eye. We don't know the exact height of the bar. It is reassuring to do the calculation and get a value that's very close to an integer, since we know the final answer must be an integer.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Suppose we now plot the same data with different bins, using the code 
`prices.plot(kind='hist', y='broccoli', bins=[0.8, 1, 1.1, 1.5, 1.8, 1.9, 2.5], density=True)`.

What would be the height on the y-axis for the bin corresponding to the interval $[\$1.10, \$1.50)$? Input your answer below.

# BEGIN SOLUTION

**Answer: ** 1.25

First we need to figure out how many grocery stores the bin $[\$1.10, \$1.50)$ contains. We already know from the previous subpart that there are four grocery stores in the bin $[\$1.30, \$1.40)$. We could do similar calculations to find the number of grocery stores in each of these bins: 

- $[\$1.10, \$1.20)$
- $[\$1.20, \$1.30)$
- $[\$1.30, \$1.40)$
- $[\$1.40, \$1.50)$

However, it's much simpler and faster to use the fact that when the bins are all equally wide, the height of a bar is proportional to the number of data values it contains. So looking at the histogram in the previous subpart, since we know the $[\$1.30, \$1.40)$ bin contains 4 grocery stores, then the $[\$1.10, \$1.20)$ bin must contain 1 grocery store, since it's only a quarter as tall. Again, we're taking advantage of the fact that there must be an integer number of grocery stores in each bin when we say it's 1/4 as tall. Our only options are 1/4, 1/2, or 3/4 as tall, and among those choices, it's clear. 

Therefore, by looking at the relative heights of the bars, we can quickly determine the number of grocery stores in each bin:

- $[\$1.10, \$1.20)$: 1 grocery store
- $[\$1.20, \$1.30)$: 3 grocery stores
- $[\$1.30, \$1.40)$: 4 grocery stores
- $[\$1.40, \$1.50)$: 1 grocery store

Adding these numbers together, this means there are 9 grocery stores whose broccoli prices fall in the interval $[\$1.10, \$1.50)$. In the new histogram, these 9 grocery stores will be represented by a bar of width $1.50-1.10 = 0.4$. The area of the bar should be $\frac{9}{18} = 0.5$. Therefore the height must be $\frac{0.5}{0.4} = 1.25.$

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

part d here

# BEGIN SOLUTION

**Answer: ** 

solution here

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

part e here

# BEGIN SOLUTION

**Answer: ** 

solution here

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

part f here

# BEGIN SOLUTION

**Answer: ** 

solution here

# END SOLUTION

# END SUBPROB

# END PROB