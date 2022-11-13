# BEGIN PROB

# BEGIN SUBPROB

Which of these would it make sense to use as the index of `flights`?

( ) `'DATE'`
( ) `'FLIGHT'`
( ) `'FROM'`
( ) `'TO'`
( ) None of these are good choices for the index

# BEGIN SOLUTION

**Answer: ** None of these are good choices for the index

When choosing an index, we have to make sure that the index is different for each row of the DataFrame. The index in this case should uniquely identify the flight. 

`'DATE'`does not uniquely identify a flight because there are many different flights in a single day. `'FLIGHT'` does not uniquely identify a flight because airlines reuse flight numbers on a daily basis, as we are told in the data description. Neither `'FROM'` nor `'TO'` uniquely identifies a flight, as there are many flights each day that depart from each airport and arrive at each airport. 

Therefore, there is no single column that's sufficient to uniquely identify a flight, but if we could use multiple columns to create what's called a multi-index, we'd probably want to use `'DATE'` and `'FLIGHT'` because each row of our DataFrame should have a unique pair of values in these columns. That's because airlines don't reuse flight numbers within a single day.

<average>57</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

What type of variable is `'FLIGHT'`?

( ) Categorical
( ) Numerical

# BEGIN SOLUTION

**Answer: ** Categorical

`'FLIGHT'` is a categorical variable because it doesn't make sense to do arithmetic with the values in the `'FLIGHT'` column. `'FLIGHT'` is just a label for each flight, and the fact that it includes some numbers does not make it numerical. We could have just as well used letter codes to distinguish flights.

<average>98</average>

# END SOLUTION

# END SUBPROB

# END PROB