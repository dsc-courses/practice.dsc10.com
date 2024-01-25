# BEGIN PROB

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

# END PROB