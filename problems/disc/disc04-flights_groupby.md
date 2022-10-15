# BEGIN PROB

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

# END SOLUTION

# END PROB