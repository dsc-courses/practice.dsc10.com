# BEGIN PROB

In the next few parts, consider the following answer choices.

A.  The name of the country with the most cities.

B.  The name of the country with the fewest cities.

C.  The number of cities in the country with the most cities.

D.  The number of cities in the country with the fewest cities.

E.  The last city, alphabetically, in the first country, alphabetically.

F.  The first city, alphabetically, in the first country, alphabetically.

G.  Nothing, because it errors.

# BEGIN SUBPROB

What does the following expression evaluate to?

```py
sun.groupby("Country").max().get("City").iloc[0]
```

( ) A 
( ) B 
( ) C 
( ) D 
( ) E 
( ) F 
( ) G

# BEGIN SOLUTION

**Answer**: E. The last city, alphabetically, in the first country, alphabetically.\

Let's break down the code:

- `sun.groupby("Country").max()`: This line of code groups the `sun` DataFrame by the `"Country"` column and then determines the **maximum** for every other column within each country group. Since the values in the `"City"` column are stored as strings, and the maximum of a Series of strings is the last string alphabetically, the values in the `"City"` column of this DataFrame will contain the last city, alphabetically, of each country.

- `.get("City")`: `.get("City")` accesses the `"City"` column. 

- `.iloc[0]`: Finally, `.iloc[0]` selects the `"City"` value from the first row. The first row corresponds to the first country alphabetically because `groupby` sorted the DataFrame by `"Country"` in ascending order. The value in the `"City"` column that `.iloc[0]` selects, then, is the name of the last city, alphabetically, in the first country, alphabetically. 

<average>36</average>

# END SOLUTION

# END SUBPROB


# BEGIN SUBPROB

What does the following expression evaluate to?

```py
sun.groupby("Country").sum().get("City").iloc[0]
```

( ) A 
( ) B 
( ) C 
( ) D 
( ) E 
( ) F 
( ) G

# BEGIN SOLUTION

**Answer**: G. Nothing, because it errors.\

Let's break down the code:

- `sun.groupby("Country").sum()`: This groups the `sun` DataFrame by the `"Country"` column and computes the sum for each numeric column within each country group. Since `"City"` is non-numeric, it will be dropped.

- `.get("City")`: This operation attempts to retrieve the `"City"` column from the resulting DataFrame. However, since the `"City"` column was dropped in the previous step, this will raise a KeyError, indicating that the column is not present in the DataFrame.

<average>73</average>

# END SOLUTION

# END SUBPROB


# BEGIN SUBPROB

What does the following expression evaluate to?

```py
sun.groupby("Country").count().sort_values("Jan").index[-1]
```

( ) A 
( ) B 
( ) C 
( ) D 
( ) E 
( ) F 
( ) G

# BEGIN SOLUTION

**Answer**: A. The name of the country with the most cities.\

Let's break down the code:

- `sun.groupby("Country").count()`: This groups the sun DataFrame by the `"Country"` column. The `.count()` method then returns the number of rows in each group for each column. Since we're grouping by `"Country"`, and since the rows in `sun` correspond to cities, this is counting the number of cities in each country.

- `.sort_values("Jan")`: The result of the previous operation is a DataFrame with `"Country"` as the index and the number of cities per country stored in every other column. The `"City`, `"Jan"`, `"Feb"`, `"Mar"`, etc. columns in the resulting DataFrame all contain the same information. Sorting by `"Jan"` sorts the DataFrame by the number of cities each country has in ascending order.

- `.index[-1]`: This retrieves the last index value from the sorted DataFrame, which corresponds to the name of the country with the most cities.

<average>61</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

What does the following expression evaluate to?

```py
sun.groupby("Country").count().sort_values("City").get("City").iloc[-1]
```

( ) A 
( ) B 
( ) C 
( ) D 
( ) E 
( ) F 
( ) G

# BEGIN SOLUTION

**Answer**: C. The number of cities in the country with the most cities.\

Let's break down the code:

- `sun.groupby("Country").count()`: This groups the sun DataFrame by the `"Country"` column. The `.count()` method then returns the number of rows in each group for each column. Since we're grouping by `"Country"`, and since the rows in `sun` correspond to cities, this is counting the number of cities in each country.

- `.sort_values("City")`: The result of the previous operation is a DataFrame with `"Country"` as the index and the number of `"City"`s per `"Country"` stored in every other column. The `"City`, `"Jan"`, `"Feb"`, `"Mar"`, etc. columns in the resulting DataFrame all contain the same information. Sorting by `"City"` sorts the DataFrame by the number of cities each country has in ascending order.

- `.get("City")`: This retrieves the `"City"` column from the sorted DataFrame, which contains the number of cities in each country.

- `.iloc[-1]`: This gets the last value from the `"City"` column, which corresponds to the number of cities in the country with the most cities.

<average>57</average>

# END SOLUTION

# END SUBPROB

# END PROB