# BEGIN PROB

Suppose you are given a DataFrame of employees for a given company. The DataFrame, called `employees`, is indexed by `'employee_id'` (string) with a column called `'years'` (int) that contains the number of years each employee has worked for the company.

# BEGIN SUBPROB

Suppose that the code

```py
employees.sort_values(by='years', ascending=False).index[0]
```

outputs `'2476'`. 

True or False: The number of years that employee 2476 has worked for the company is greater than the number of years that any other employee has worked for the company.

( ) True
( ) False
# BEGIN SOLUTION

**Answer: ** False

This is false because there could be other employees who worked at the company equally long as employee 2476.

The code says that when the `employees` DataFrame is sorted in descending order of `'years'`, employee 2476 is in the first row. There might, however, be a tie among several employees for their value of `'years'`. In that case, employee 2476 may wind up in the first row of the sorted DataFrame, but we cannot say that the number of years employee 2476 has worked for the company is greater than the number of years that any other employee has worked for the company.

If the statement had said *greater than or equal to* instead of *greater than*, the statement would have been true.

<average>29</average>
# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

What will be the output of the following code?

```py
employees.assign(start=2021-employees.get('years'))
employees.sort_values(by='start').index.iloc[-1]
```

( ) the employee id of an employee who has worked there for the most years
( ) the employee id of an employee who has worked there for the fewest years
( ) an error message complaining about `iloc[-1]`
( ) an error message complaining about something else

# BEGIN SOLUTION

**Answer: ** an error message complaining about something else

The problem is that the first line of code does not actually add a new column to the `employees` DataFrame because the expression is not saved. So the second line tries to sort by a column, `'start'`, that doesn't exist in the `employees` DataFrame and runs into an error when it can't find a column by that name.

This code also has a problem with `iloc[-1]`, since `iloc` cannot be used on the index, but since the problem with the missing `'start'` column is encountered first, that will be the error message displayed.

<average>27</average>
# END SOLUTION

# END SUBPROB

# END PROB