# BEGIN PROB

The command `.set_index` can take as input one column, to be used as the index, or a sequence of columns to be used as a nested index (sometimes called a MultiIndex). A MultiIndex is the default behavior of the dataframe returned by .groupby with multiple columns.

You are given a dataframe called restaurants that contains information on a variety of local restaurants' daily number of customers and daily income. There is a row for each restaurant for each date in a given five-year time period.

The columns of restaurants are `'name'` (`str`), `'year'` (`int`),  `'month'` (`int`), `'day'` (`int`), `'num_diners'` (`int`), and `'income'` (`float`).

Assume that in our data set, there are not two different restaurants that go by the same name (chain restaurants, for example).

Which of the following would be the best way to set the index for this dataset?

( ) `restaurants.set_index('name')`
( ) `restaurants.set_index(['year', 'month', 'day'])`
( ) `restaurants.set_index(['name', 'year', 'month', 'day'])`

# BEGIN SOLUTION

**Answer: ** `restaurants.set_index(['name', 'year', 'month', 'day'])`

The correct answer is to create an index with the `'name'`, `'year'`, '`month`', and '`day`' columns. The question provides that there
is a row for each restaurant for each data in the five year span. Therefore, we are interested in the granularity of a 
specific day (the day, the month, and the year). In order to have this information available in this index, we must set
the index to be a multi index with columns `['name', 'year', 'month', 'day']`. Looking at the other options, simply looking 
at the `'name'` column would not account for the fact the dataframe contains daily data on customers and income for each
restaurant. Similarly, the second option of `['name', 'month', 'day']` would not account for the fact that the data comes 
in a five year span so there will naturally be five overlaps (one for each year) for each unique date that must be accounted for. 

<average>53</average>
# END SOLUTION

# END PROB
