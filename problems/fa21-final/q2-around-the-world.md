# BEGIN PROB

(Remember to keep the data description from the top of the exam open in another tab!)

`'Tate Modern'` is the most popular art museum in London. But what's the most popular art museum in each city?

It turns out that there's no way to answer this easily using the tools that you know about so far. To help, we've created a new Series method, `.last()`. If `s` is a Series, `s.last()` returns the last element of `s` (i.e. the element at the very end of `s`). `.last()` works with `.groupby`, too (just like `.mean()` and `.count()`).

Fill in the blanks so that the code below correctly assigns `best_per_city` to a DataFrame with one row per city, that describes the name, number of visitors, and rank of the most visited art museum in each city. `best_per_city` should be sorted in decreasing order of number of visitors. The first few rows of `best_per_city` are shown below.

<center><img src='../assets/images/fa21-final/best_per_city.png' width=40%></center>

```py
best_per_city = __(a)__.groupby(__(b)__).last().__(c)__
```

1. What goes in blank (a)?
2. What goes in blank (b)?
3. What goes in blank (c)?

# BEGIN SOLN

**Answers:**

1. `art_museums.sort_values('Visitors', ascending=True)`
2. `'City'`
3. `sort_values('Visitors', ascending=False)`

Let's take a look at the completed implementation.

```py
best_per_city = art_museums.sort_values('Visitors', ascending=True).groupby('City').last().sort_values('Visitors', ascending=False)
```

# END SOLN

# END PROB