# BEGIN PROB

Suppose we have access to another DataFrame, `new_york`, that contains the latitude and longitude of every single skyscraper in New York City that is also in `sky`. The first few rows of `new_york` are shown below.

<center><img src='../assets/images/wi22-midterm/ny.png' width=40%></center>

Below, we define a new DataFrame, `sky_with_location`, that merges together both `sky` and `new_york`.

```py
sky_with_location = sky.merge(new_york, left_index=True, right_on='name')
```

Given that:

- `sky` has $s$ rows,
- `new_york` has $n$ rows, and 
- building names are spelled and formatted the exact same way in both `sky` and `new_york`, i.e. that there are no typos in either DataFrame,

select the true statement below.

( ) `sky_with_location` has exactly $s$ rows.
( ) `sky_with_location` has exactly $n$ rows.
( ) `sky_with_location` has exactly $s - n$ rows.
( ) `sky_with_location` has exactly $s + n$ rows.
( ) `sky_with_location` has exactly $s \times n$ rows.

# BEGIN SOLN

**Answer:** `sky_with_location` has exactly $n$ rows.

Here, we are merging `sky` and `new_york` on skyscraper names (stored in the index in `sky` and in the `'name'` column in `new_york`). The resulting DataFrame, `sky_with_location`, will have one row for each "match" between skyscrapers in `sky` and `new_york`. Since skyscraper names are presumably unique, `sky_with_location` will have one row for each skyscraper that is in both `sky` and `new_york`.

The skyscrapers that are in both `sky` and `new_york` are just the skyscrapers in `new_york`, since all of the non-New York skyscrapers in `sky` won't be in `new_york`. As such, `sky_with_location` has the same number of rows as `new_york`. `new_york` has $n$ rows, so `sky_with_location` also has $n$ rows.

<average>64</average>

# END SOLN

# END PROB