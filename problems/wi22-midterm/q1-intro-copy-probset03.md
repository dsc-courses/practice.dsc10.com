# BEGIN PROB

Below, identify the data type of the result of each of the following expressions, or select "error" if you believe the expression results in an error.

# BEGIN SUBPROB

```py
sky.get('city').apply(len)
```

( ) int or float
( ) Boolean
( ) string
( ) array
( ) Series
( ) DataFrame
( ) error

# BEGIN SOLN

**Answer:** Series

The `.apply` method takes in a function and evaluates that function on every element in a Series. Here, `sky.get('city').apply(len)` is using the function `len` on every element in the Series `sky.get('city')`. The result is also a Series, containing the lengths of the names of each `'city'`.

<average>79</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

```py
sky.get('city').apply(max)
```

( ) int or float
( ) Boolean
( ) string
( ) array
( ) Series
( ) DataFrame
( ) error

# BEGIN SOLN

**Answer:** Series

This is a tricky problem!

The function that `apply` takes in must work on individual elements in a Series, i.e. it must work with just a single argument. We saw this in the above subpart, where `sky.get('city').apply(len)` applied `len` on each `'city'` name.

Here, we are trying to apply the `max` function on each `'city'` name. The `max` of a single item does not work in Python, because taking the `max` requires comparing two or more elements. Try it out - in a notebook, run the expression `max(5)`, and you'll see an error. So, if we tried to use `.apply(max)` on a Series of numbers, we'd run into an error.

**However**, we are using `.apply(max)` on a Series of strings, and it turns out that Python **does** allow us to take the `max` of a string! The `max` of a string in Python is defined as the last character in the string alphabetically, so `max('hello')` evaluates to `'o'`. This means that `sky.get('city').apply(max)` does actually run without error; it evaluates to a Series containing the last element in the name of each `'city'`.

(This subpart was trickier than we intended – we ended up giving credit to both "error" and "Series".)

<average>89</average>

# END SOLN

# END SUBPROB

# END PROB