# BEGIN PROB

In this question, we'll write code to learn more about the skyscrapers in the beautiful city of San Diego. (Unrelated fun fact – since the San Diego Airport is so close to downtown, buildings in downtown San Diego legally cannot be taller than 152 meters.)

# BEGIN SUBPROB

Below, fill in the blank to create a DataFrame, named `san_tall`, consisting of just the skyscrapers in San Diego that are over 100 meters tall.

```py
condition = ______
san_tall = sky[(sky.get('city') == 'San Diego') & condition]
```

What goes in the blank?

# BEGIN SOLN

**Answer:** `sky.get('height') > 100`

We need to query for all of the skyscrapers that satisfy two conditions – the `'city'` must be `'San Diego'` and the `'height'` must be above 100. The first condition was already implemented for us, so we just need to construct a Boolean Series that implements the second condition.

Here, we want all of the rows where `'height'` is above 100, so we `get` the `'height'` column and compare it to 100 like so: `sky.get('height') > 100`.

<average>95</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Suppose `san_tall` from the previous part was created correctly. Fill in the blanks so that `height_many_floors` evaluates to the **height (in meters)** of the skyscraper with the **most floors**, amongst all skyscrapers in San Diego that are over 100 meters tall.

```py
height_many_floors = san_tall.______.iloc[0]
```

What goes in the blank?

# BEGIN SOLN

**Answer:** `sort_values('floors', ascending=False).get('height')`

The end of the line given to us is `.iloc[0]`. We know that `.iloc[0]` extracts the first element in whatever Series it is called on, so what comes before `.iloc[0]` must be a Series where the first element is the `'height'` of the skyscraper with the most floors, among all skyscrapers in San Diego that are over 100 meters tall. The DataFrame we are working with, `san_tall`, already only has skyscrapers in San Diego that are over 100 meters tall.

This means that in the blank, all we need to do is:

1. Sort skyscrapers by `'floors'` in decreasing order (so that the first row is the skyscraper with the most `'floors'`).
2. Extract the `'height'` column.

As such, a complete answer is `height_many_floors = san_tall.sort_values('floors', ascending=False).get('height').iloc[0]`.

<average>74</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

`height_many_floors`, the value you computed in the previous part (2.2) was a number.

**True or False:** Assuming that the DataFrame `san_tall` contains all skyscrapers in San Diego, `height_many_floors` is the height (in meters) of the **tallest** skyscraper in San Diego.

( ) True
( ) False

# BEGIN SOLN

**Answer:** False

`height_many_floors` is the height of the skyscraper with the most `'floors'`. However, this is not necessarily the tallest skyscraper (i.e. the skyscraper with the largest `'height'`)! Consider the following scenario:

- Building A: 15 floors, height of 150 feet
- Building B: 20 floors, height of 100 feet

`height_many_floors` would be 100, but it is not the `'height'` of the taller building.

<average>84</average>

# END SOLN

# END SUBPROB

# END PROB