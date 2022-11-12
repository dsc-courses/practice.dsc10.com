# BEGIN PROB

You are given a DataFrame called `restaurants` that contains information on a variety of local restaurants' daily number of customers and daily income. There is a row for each restaurant for each date in a given five-year time period.

The columns of `restaurants` are `'name'` (string), `'year'` (int),  `'month'` (int), `'day'` (int), `'num_diners'` (int), and `'income'` (float).

Assume that in our data set, there are not two different restaurants that go by the same `'name'` (chain restaurants, for example).

# BEGIN SUBPROB

What type of visualization would be best to display the data in a way that helps to answer the question "Do more customers bring in more income?"

( ) scatterplot
( ) line plot
( ) bar chart
( ) histogram

# BEGIN SOLUTION

**Answer: **  scatterplot

The number of customers is given by `'num_diners'` which is an integer, and `'income'` is a float. Since both are numerical variables, neither of which represents time, it is most appropriate to use a scatterplot.
<average>87</average>
# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

What type of visualization would be best to display the data in a way that helps to answer the question "Have restaurants' daily incomes been declining over time?"

( ) scatterplot
( ) line plot
( ) bar chart
( ) histogram

# BEGIN SOLUTION

**Answer: ** line plot

Since we want to plot a trend of a numerical quantity (`'income'`) over time, it is best to use a line plot. 

<average>95</average>
# END SOLUTION

# END SUBPROB

# END PROB