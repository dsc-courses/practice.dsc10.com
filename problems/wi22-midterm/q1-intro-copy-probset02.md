# BEGIN PROB

Below, identify the data type of the result of each of the following expressions, or select "error" if you believe the expression results in an error.

# BEGIN SUBPROB

```py
sky.sort_values('height')
```

( ) int or float
( ) Boolean
( ) string
( ) array
( ) Series
( ) DataFrame
( ) error

# BEGIN SOLN

**Answer:** DataFrame

`sky` is a DataFrame. All the `sort_values` method does is change the order of the rows in the Series/DataFrame it is called on, it does not change the data structure. As such, `sky.sort_values('height')` is also a DataFrame.

<average>87</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

```py
sky.sort_values('height').get('material').loc[0]
```

( ) int or float
( ) Boolean
( ) string
( ) array
( ) Series
( ) DataFrame
( ) error

# BEGIN SOLN

**Answer:** error

`sky.sort_values('height')` is a DataFrame, and `sky.sort_values('height').get('material')` is a Series corresponding to the `'material'` column, sorted by `'height'` in increasing order. So far, there are no errors.

Remember, the `.loc` _accessor_ is used to access elements in a Series based on their index. `sky.sort_values('height').get('material').loc[0]` is asking for the element in the `sky.sort_values('height').get('material')` Series with index 0. However, the index of `sky` is made up of building names. Since there is no building named `0`,  `.loc[0]` causes an error.

<average>79</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

```py
sky.sort_values('height').get('material').iloc[0]
```

( ) int or float
( ) Boolean
( ) string
( ) array
( ) Series
( ) DataFrame
( ) error

# BEGIN SOLN

**Answer:** string

As we mentioned above, `sky.sort_values('height').get('material')` is a Series containing values from the `'material'` column (but sorted). Remember, there is no element in this Series with an index of 0, so `sky.sort_values('height').get('material').loc[0]` errors. However, `.iloc[0]` works differently than `.loc[0]`; `.iloc[0]` will give us the first element in a Series (independent of what's in the index). So, `sky.sort_values('height').get('material').iloc[0]` gives us back a value from the `'material'` column, which is made up of strings, so it gives us a string. (Specifically, it gives us the `'material'` type of the skyscraper with the smallest `'height'`.)

<average>89</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

```py
sky.get('floors').max()
```

( ) int or float
( ) Boolean
( ) string
( ) array
( ) Series
( ) DataFrame
( ) error

# BEGIN SOLN

**Answer:** int or float

The Series `sky.get('floors')` is made up of integers, and `sky.get('floors').max()` evaluates to the largest number in the Series, which is also an integer.

<average>91</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

```py
sky.groupby('material').max()
```

( ) int or float
( ) Boolean
( ) string
( ) array
( ) Series
( ) DataFrame
( ) error

# BEGIN SOLN

**Answer:** DataFrame

When grouping and using an aggregation method, the result is always a DataFrame. The DataFrame `sky.groupby('material').max()` contains all of the columns in `sky`, minus `'material'`, which has been moved to the index. It contains one row for each unique `'material'`.

Note that no columns were "dropped", as may happen when using `.mean()`, because `.max()` can work on Series' of any type. You can take the max of strings, while you cannot take the mean of strings.

<average>78</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

```py
sky.index[0]
```

( ) int or float
( ) Boolean
( ) string
( ) array
( ) Series
( ) DataFrame
( ) error

# BEGIN SOLN

**Answer:** string

`sky.index` contains the values `'Bayard-Condict Building'`, `'The Yacht Club at Portofino'`, `'City Investing Building'`, etc. `sky.index[0]` is then `'Bayard-Condict Building'`, which is a string.

<average>91</average>

# END SOLN

# END SUBPROB

# END PROB