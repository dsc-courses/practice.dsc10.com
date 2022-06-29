# BEGIN PROB

# BEGIN SUBPROB

Which of these correctly evaluates to the number of flights King Triton took to San Diego (airport code `'SAN'`)?

( ) `flights.loc['SAN'].shape[0]`
( ) `flights[flights.get('TO') == 'SAN'].shape[0]`
( ) `flights[flights.get('TO') == 'SAN'].shape[1]`
( ) `len(flights.sort_values('TO', ascending=False).loc['SAN'])`

# BEGIN SOLUTION

**Answer: ** `flights[flights.get('TO') == 'SAN'].shape[0]`

solution here

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

solution here

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

solution here

# END SOLUTION

# END SUBPROB

# END PROB