# BEGIN PROB

In this question, we'll keep working with the `art_museums` DataFrame.

# BEGIN SUBPROB

(Remember to keep the data description from the top of the exam open in another tab!)

`'Tate Modern'` is the most popular art museum in London. But what's the most popular art museum in each city?

It turns out that there's no way to answer this easily using the tools that you know about so far. To help, we've created a new Series method, `.last()`. If `s` is a Series, `s.last()` returns the last element of `s` (i.e. the element at the very end of `s`). `.last()` works with `.groupby`, too (just like `.mean()` and `.count()`).

Fill in the blanks so that the code below correctly assigns `best_per_city` to a DataFrame with one row per city, that describes the name, number of visitors, and rank of the most visited art museum in each city. `best_per_city` should be sorted in decreasing order of number of visitors. The first few rows of `best_per_city` are shown below.

<center><img src='../assets/images/fa21-final/best_per_city.png' width=40%></center>
<br>

```py
best_per_city = __(a)__.groupby(__(b)__).last().__(c)__
```

1. What goes in blank (a)?
2. What goes in blank (b)?
3. What goes in blank (c)?

# BEGIN SOLUTION

**Answers:**

1. `art_museums.sort_values('Visitors', ascending=True)`
2. `'City'`
3. `sort_values('Visitors', ascending=False)`

Let's take a look at the completed implementation.

```py
best_per_city = art_museums.sort_values('Visitors', ascending=True).groupby('City').last().sort_values('Visitors', ascending=False)
```

We first sort the row in `art_museums` by the number of `'Visitors'` in `ascending` order. Then `goupby('City')`, so that we have one row per city. Recall, we need an aggregation method after using `groupby()`. In this question, we use `last()` to only keep the one last row for each city. Since in blank (a) we have sorted the rows by `'Visitors'`, so `last()` keeps the row that contains the name of the most visited museum in that city. At last we sort this new DataFrame by `'Visitors'` in descending order to fulfill the question's requirement.

<average>65</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Assume you've defined `best_per_city` correctly.

Which of the following options evaluates to the number of visitors to the most visited art museum in Amsterdam? Select all that apply.

[ ] `best_per_city.get('Visitors').loc['Amsterdam']`
[ ] `best_per_city[best_per_city.index == 'Amsterdam'].get('Visitors').iloc[0]`
[ ] `best_per_city[best_per_city.index == 'Amsterdam'].get('Visitors').iloc[-1]`
[ ] `best_per_city[best_per_city.index == 'Amsterdam'].get('Visitors').loc['Amsterdam']`
[ ] None of the above

# BEGIN SOLUTION

**Answer:** `best_per_city.get('Visitors').loc['Amsterdam']`, `best_per_city[best_per_city.index == 'Amsterdam'].get('Visitors').iloc[0]`, `best_per_city[best_per_city.index == 'Amsterdam'].get('Visitors').iloc[-1]`, `best_per_city[best_per_city.index == 'Amsterdam'].get('Visitors').loc['Amsterdam']` (Select all except "None of the above")

`best_per_city.get('Visitors').loc['Amsterdam']` We first use `.get(column_name)` to get a series with number of visitors to the most visited art museum, and then locate the number of visitors to the most visited art museum in Amsterdam using `.loc[index]` since we have `"City"` as index.

`best_per_city[best_per_city.index == 'Amsterdam'].get('Visitors').iloc[0]`
We first query the `best_per_city` to only include the DataFrame with one row with index `'Amsterdam'`. Then, we get the `'Visitors'` column of this DataFrame. Finally, we use `iloc[0]` to access the first and the only value in this column.

`best_per_city[best_per_city.index == 'Amsterdam'].get('Visitors').iloc[-1]` We first query the `best_per_city` to only include the DataFrame with one row with index `'Amsterdam'`. Then, we get the `'Visitors'` column of this DataFrame. Finally, we use `iloc[-1]` to access the last and the only value in this column.

`best_per_city[best_per_city.index == 'Amsterdam'].get('Visitors').loc['Amsterdam']` We first query the `best_per_city` to only include the DataFrame with one row with index `'Amsterdam'`. Then, we get the `'Visitors'` column of this DataFrame. Finally, we use `loc['Amsterdam']` to access the value in this column with index `'Amsterdam'`.

<average>84</average>

# END SOLUTION

# END SUBPROB

# END PROB