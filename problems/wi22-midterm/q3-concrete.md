# BEGIN PROB

Note that each part of Question 3 depends on previous parts of Question 3.

In this question, we'll take a closer look at the `'material'` column of `sky`.

# BEGIN SUBPROB

Below, fill in the blank to complete the implementation of the function `majority_concrete`, which takes in the name of a `city` and returns `True` if the majority of the skyscrapers in that city are made of concrete, and `False` otherwise. **We define "majority" to mean "at least 50%".**

```py
def majority_concrete(city):
    all_city = sky[sky.get('city') == city]
    concrete_city = all_city[all_city('material') == 'concrete']
    proportion = ______
    return proportion >= 0.5
```

What goes in the blank?

# BEGIN SOLN

**Answer:** `concrete_city.shape[0] / all_city.shape[0]`

Let's first understand the code that is already provided for us. Note that `city` is a string corresponding to the name of a city.

`all_city` contains only the rows for the passed in `city`. Note that `all_city.shape[0]` or `len(all_city)` is the number of rows in `all_city`, i.e. it is the number of skyscrapers in `city`. Then, `concrete_city` contains only the rows in `all_city` corresponding to `'concrete'` skyscrapers, i.e. it contains only the rows corresponding to `'concrete'` skyscrapers in `city`. Note that `concrete_city.shape[0]` or `len(concrete_city)` is the number of skyscrapers in `city` that are made of `'concrete'`.

We want to return `True` only if at least 50% of the skyscrapers in `city` are made of concrete. The last line in the function, `return proportion >= 0.5`, is already provided for us, so all we need to do is compute the proportion of skyscrapers in `city` that are made of concrete. This is `concrete_city.shape[0] / all_city.shape[0]`.

Another possible answer is `len(concrete_city) / len(all_city)`.

<average>85</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Below, we create a DataFrame named `by_city`.

```py
by_city = sky.groupby('city').count().reset_index()
```

Below, fill in the blanks to add a column to `by_city`, called `'is_majority'`, that contains the value `True` for each city where the majority of skyscrapers are concrete, and `False` for all other cities. You may need to use the function you defined in the previous subpart.

```py
by_city = by_city.assign(is_majority = ______)
```

What goes in the blank?

# BEGIN SOLN

**Answer:** `by_city.get('city').apply(majority_concrete)`

We are told to add a column to `by_city`. Recall, the way that `.assign` works is that the name of the new column comes before the `=` symbol, and a Series (or array) containing the values for the new column comes after the `=` symbol. As such, a Series needs to go in the blank.

`majority_concrete` takes in the name of a single `city` and returns either `True` or `False` accordingly. All we need to do here then is use the `majority_concrete` function on every element in the `'city'` column. After accessing the `'city'` column using `by_city.get('city')`, we need to use the `.apply` method using the argument `majority_concrete`. Putting it all together yields `by_city.get('city').apply(majority_concrete)`, which is a Series.

Note: Here, `by_city.get('city')` only works because `.reset_index()` was used in the line where `by_city` was defined. If we did not reset the index, `'city'` would not be a column!

<average>86</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

`by_city` now has a column named `'is_majority'` as described in the previous subpart. Now, suppose we create another DataFrame, `mystery`, below:

```py
mystery = by_city.groupby('is_majority').count()
```

What is the largest possible value that `mystery.shape[0]` could evaluate to?

# BEGIN SOLN

**Answer:** 2

Recall, the `'is_majority'` column we created in the previous subpart contains only two possible values – `True` and `False`. When we group `by_city` by `'is_majority'`, we create two "groups" – one for `True` and one for `False`. As such, no matter what aggregation method we use (here we happened to use `.count()`), the resulting DataFrame will only have 2 rows (again, one for `True` and one for `False`).

Note: The question asked for the "largest possible value" that `mystery.shape[0]`, because it is possible that `mystery` only has 1 row. This can only happen in two cases:

1. It is true in **all cities** that the majority of skyscrapers are made of `'concrete'`.
2. It is true in **no cities** that the majority of skyscrapers are made of `'concrete'`.

<average>76</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Suppose `mystery.get('city').iloc[0] == mystery.get('city').iloc[1]` evaluates to `True`.

**True or False:** In exactly half of the cities in `sky`, it is true that a majority of skyscrapers are made of `'concrete'`. (**_Tip:_** Walk through the manipulations performed in the previous three subparts to get an idea of what `mystery` looks like and contains.)

( ) True
( ) False

# BEGIN SOLN

**Answer:** True

In the solution to the previous subpart, we noted that `mystery` contains at most 2 rows, one corresponding to cities where `'is_majority'` is `True` and one corresponding to cities where `'is_majority'` is `False`. Furthermore, recall that we used the `.count()` aggregation method, which means that the entries in each column of `mystery` contain the **number** of cities where `'is_majority'` is `True` and the **number** of cities where `'is_majority'` is `False`.

If `mystery.get('city').iloc[0] == mystery.get('city').iloc[1]`, it must be the case that the number of cities where `'is_majority'` is `True` and `False` are equal. This must mean that in exactly half of the cities in `sky`, it is true that the majority of skyscrapers are made of `'concrete'`. 

<average>69</average>

# END SOLN

# END SUBPROB

# END PROB