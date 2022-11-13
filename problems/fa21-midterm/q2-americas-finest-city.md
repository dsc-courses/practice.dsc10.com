# BEGIN PROB

# BEGIN SUBPROB

Which of these correctly evaluates to the number of flights King Triton took to San Diego (airport code `'SAN'`)?

( ) `flights.loc['SAN'].shape[0]`
( ) `flights[flights.get('TO') == 'SAN'].shape[0]`
( ) `flights[flights.get('TO') == 'SAN'].shape[1]`
( ) `len(flights.sort_values('TO', ascending=False).loc['SAN'])`

# BEGIN SOLUTION

**Answer: ** `flights[flights.get('TO') == 'SAN'].shape[0]`

The strategy is to create a DataFrame with only the flights that went to San Diego, then count the number of rows. The first step is to query with the condition `flights.get('TO') == 'SAN'` and the second step is to extract the number of rows with `.shape[0]`. 

Some of the other answer choices use `.loc['SAN']` but `.loc` only works with the index, and `flights` does not have airport codes in its index.

<average>95</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Fill in the blanks below so that the result also evaluates to the number of flights King Triton took to San Diego (airport code `'SAN'`).

```python
flights.groupby(__(a)__).count().get('FLIGHT').__(b)__            
```

What goes in blank (a)?

( ) `'DATE'`
( ) `'FLIGHT'`
( ) `'FROM'`
( ) `'TO'`

What goes in blank (b)?

( ) `.index[0]`
( ) `.index[-1]`
( ) `.loc['SAN']`
( ) `.iloc['SAN']`
( ) `.iloc[0]`

True or False: If we change `.get('FLIGHT')` to `.get('SEAT')`, the results of the above code block will not change. (You may assume you answered the previous two subparts correctly.)

( ) True
( ) False

# BEGIN SOLUTION

**Answer: ** `'TO'`, `.loc['SAN']`, True

The strategy here is to group all of King Triton's flights according to where they landed, and count up the number that landed in San Diego. The expression `flights.groupby('TO').count()` evaluates to a DataFrame indexed by arrival airport where, for any arrival airport, each column has a count of the number of King Triton's flights that landed at that airport. To get the count for San Diego, we need the entry in any column for the row corresponding to San Diego. The code `.get('FLIGHT')` says we'll use the `'FLIGHT'` column, but any other column would be equivalent. To access the entry of this column corresponding to San Diego, we have to use `.loc` because we know the name of the value in the index should be `'SAN'`, but we don't know the row number or integer position.

<average>89</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Consider the DataFrame `san`, defined below.

```py
san = flights[(flights.get('FROM') == 'SAN') & (flights.get('TO') == 'SAN')]
```

Which of these DataFrames **must** have the same number of rows as `san`?

( ) `flights[(flights.get('FROM') == 'SAN') and (flights.get('TO') == 'SAN')]`
( ) `flights[(flights.get('FROM') == 'SAN') | (flights.get('TO') == 'SAN')]`
( ) `flights[(flights.get('FROM') == 'LAX') & (flights.get('TO') == 'SAN')]`
( ) `flights[(flights.get('FROM') == 'LAX') & (flights.get('TO') == 'LAX')]`

# BEGIN SOLUTION

**Answer: ** `flights[(flights.get('FROM') == 'LAX') & (flights.get('TO') == 'LAX')]`

The DataFrame `san` contains all rows of `flights` that have a departure airport of `'SAN'` and an arrival airport of `'SAN'`. But as you may know, and as you're told in the data description, there are no flights from an airport to itself. So `san` is actually an empty DataFrame with no rows!

We just need to find which of the other DataFrames would necessarily be empty, and we can see that `flights[(flights.get('FROM') == 'LAX') & (flights.get('TO') == 'LAX')]` will be empty for the same reason. 

Note that none of the other answer choices are correct. The first option uses the Python keyword `and` instead of the symbol `&`, which behaves unexpectedly but does not give an empty DataFrame. The second option will be non-empty because it will contain all flights that have San Diego as the departure airport or arrival airport, and we already know from the first few rows of `flight` that there are some of these. The third option will contain all the flights that King Triton has taken from `'LAX'` to `'SAN'`.  Perhaps he's never flown this route, or perhaps he has. This DataFrame could be empty, but it's not necessarily going to be empty, as the question requires.

<average>70</average>

# END SOLUTION

# END SUBPROB

# END PROB