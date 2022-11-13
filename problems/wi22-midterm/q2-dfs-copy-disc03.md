# BEGIN PROB

In this question, we'll write code to learn more about the skyscrapers in the beautiful city of San Diego. (Unrelated fun fact – since the San Diego Airport is so close to downtown, buildings in downtown San Diego legally cannot be taller than 152 meters.)

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

# END PROB