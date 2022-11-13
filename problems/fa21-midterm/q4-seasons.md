# BEGIN PROB

We define the seasons as follows:

<center>
<table class="table" style="width:30%">
  <thead>
    <tr>
      <th scope="col">Season</th>
      <th scope="col">Month</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Spring</th>
      <td>March, April, May</td>
    </tr>
    <tr>
      <th scope="row">Summer</th>
      <td>June, July, August</td>
    </tr>
    <tr>
      <th scope="row">Fall</th>
      <td>September, October, November</td>
    </tr>
    <tr>
      <th scope="row">Winter</th>
      <td>December, January, February</td>
    </tr>
  </tbody>
</table>
</center>

# BEGIN SUBPROB

We want to create a function `date_to_season` that takes in a `date` as formatted in the `'DATE'` column of `flights` and returns the season corresponding to that date. Which of the following implementations of `date_to_season` works correctly? **Select all that apply.**

Option 1:

```python
def date_to_season(date):
    month_as_num = int(date.split('-')[1])
    if month_as_num >= 3 and month_as_num < 6:
        return 'Spring'
    elif month_as_num >= 6 and month_as_num < 9:
        return 'Summer'
    elif month_as_num >= 9 and month_as_num < 12:
        return 'Fall'
    else:
        return 'Winter'
```

Option 2:

```python
def date_to_season(date):
    month_as_num = int(date.split('-')[1])
    if month_as_num >= 3 and month_as_num < 6:
        return 'Spring'
    if month_as_num >= 6 and month_as_num < 9:
        return 'Summer'
    if month_as_num >= 9 and month_as_num < 12:
        return 'Fall'
    else:
        return 'Winter'
```

Option 3:

```python
def date_to_season(date):
    month_as_num = int(date.split('-')[1])
    if month_as_num < 3:
        return 'Winter'
    elif month_as_num < 6:
        return 'Spring'
    elif month_as_num < 9:
        return 'Summer'
    elif month_as_num < 12:
        return 'Fall'
    else:
        return 'Winter' 
```

[ ] Option 1
[ ] Option 2
[ ] Option 3
[ ] None of these implementations of `date_to_season` work correctly

# BEGIN SOLUTION

**Answer: ** Option 1, Option 2, Option 3

All three options start with the same first line of code: `month_as_num = int(date.split('-')[1])`. This takes the date, originally a string formatted such as `'2021-09-07'`, separates it into a list of three strings such as `['2021', '09', '07']`, extracts the element in position 1 (the middle position), and converts it to an `int` such as 9. Now we have the month as a number we can work with more easily.

According to the definition of seasons, the months in each season are as follows:

<center>
<table class="table" style="width:40%">
  <thead>
    <tr>
      <th scope="col">Season</th>
      <th scope="col">Month</th>
      <th scope="col">month_as_num</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Spring</th>
      <td>March, April, May</td>
      <td>3, 4, 5</td>
    </tr>
    <tr>
      <th scope="row">Summer</th>
      <td>June, July, August</td>
      <td>6, 7, 8</td>
    </tr>
    <tr>
      <th scope="row">Fall</th>
      <td>September, October, November</td>
      <td>9, 10, 11</td>
    </tr>
    <tr>
      <th scope="row">Winter</th>
      <td>December, January, February</td>
      <td>12, 1, 2</td>
    </tr>
  </tbody>
</table>
</center>

Option 1 correctly assigns months to seasons by checking if the month falls in the appropriate range for `'Spring'`, then `'Summer'`, then `'Fall'`. Finally, if all of these conditions are false, the `else` branch will return the correct answer of `'Winter'` when `month_as_num` is 12, 1, or 2.

Option 2 is also correct, and in fact, it does the same exact thing as Option 1 even though it uses `if` where Option 1 used `elif`. The purpose of `elif` is to check a condition only when all previous conditions are false. So if we have an `if` followed by an `elif`, the `elif` condition will only be checked when the `if` condition is false. If we have two sequential `if` conditions, typically the second condition will be checked regardless of the outcome of the first condition, which means two `if` statements can behave differently than an `if` followed by an `elif`. In this case, however, since the `if` statements cause the function to `return` and therefore stop executing, the only way to get to a certain `if` condition is when all previous `if` conditions are false. If any prior `if` condition was true, the function would have returned already! So this means the three `if` conditions in Option 2 are equivalent to the `if`, `elif`, `elif` structure of Option 1. Note that the `else` case in Option 1 is reached when all prior conditions are false, whereas the `else` in Option 2 is paired only with the `if` statement immediately preceding it. But since we only ever get to that third `if` statement when the first two `if` conditions are false, we still only reach the `else` branch when all three `if` conditions are false.

Option 3 works similarly to Option 1, except it separates the months into more categories, first categorizing January and February as `'Winter'`, then checking for `'Spring'`, `'Summer'`, and `'Fall'`. The only month that winds up in the `else` branch is December. We can think of Option 3 as the same as Option 1, except the Winter months have been separated into two groups, and the group containing January and February is extracted and checked first.

<average>76</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Assuming we've defined `date_to_season` correctly in the previous part, which of the following lines of code correctly computes the season for each flight in `flights`?

( ) `date_to_season(flights.get('DATE'))`
( ) `date_to_season.apply(flights).get('DATE')`
( ) `flights.apply(date_to_season).get('DATE')`
( ) `flights.get('DATE').apply(date_to_season)`

# BEGIN SOLUTION

**Answer: ** `flights.get('DATE').apply(date_to_season)`

Our function `date_to_season` takes as input a single date and converts it to a season. We cannot input a whole Series of dates, as in the first answer choice. We instead need to `apply` the function to the whole Series of dates. The correct syntax to do that is to first extract the Series of dates from the DataFrame and then use `.apply`, passing in the name of the function we wish to apply to each element of the Series. Therefore, the correct answer is `flights.get('DATE').apply(date_to_season)`.

<average>97</average>

# END SOLUTION

# END SUBPROB

# END PROB