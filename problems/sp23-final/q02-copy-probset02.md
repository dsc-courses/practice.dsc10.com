# BEGIN PROB

Vanessa is a big Formula 1 racing fan, and wants to plan a trip to
Monaco, where the Monaco Grand Prix is held. Monaco is an example of a
"city-state" --- that is, a city that is its own country. Singapore is
another example of a city-state.

We'll say that a row of `sun` corresponds to a city-state if its
`"Country"` and `"City"` values are equal.

# BEGIN SUBPROB

Fill in the blanks so that the expression below is equal to the total
number of sunshine hours in October of all city-states in `sun`.

```py
    sun[__(a)__].__(b)__
```

What goes in blanks (a) and (b)?

# BEGIN SOLUTION

**Answer**: (a):  `sun.get("Country") == sun.get("City")`, (b): `.get("Oct").sum()`

**What goes in blank (a)?** `sun.get("Country") == sun.get("City")`\
This expression compares the `"Country"` column to the `"City"` column for each row in the `sun` DataFrame. It returns a Boolean Series where each value is `True` if the corresponding `"Country"` and `"City"` are the same (indicating a city-state) and `False` otherwise.

<average>79</average>

<br><br>

**What goes in blank (b)?** `.get("Oct").sum()`\
Here, we select the `"Oct"` column, which represents the sunshine hours in October, and compute the sum of its values. By using this after querying for city-states, we calculate the total sunshine hours in October across all city-states in the `sun` DataFrame.

<average>85</average>

# END SOLUTION

# END SUBPROB

# END PROB