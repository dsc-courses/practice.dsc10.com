# BEGIN PROB

# BEGIN SUBPROB

Consider the function `unknown`, defined below.

```py
def unknown(df):
    grouped = plum.groupby('Opp').max().get(['Date', 'PTS'])
    return np.array(grouped.reset_index().index)[df]
```

What does `unknown(3)` evaluate to?

( ) `'2021-06-05'`
( ) `'WAS'`
( ) The date on which Kelsey Plum scored the most points
( ) The three-letter code of the opponent on which Kelsey Plum scored the most points
( ) The number 0
( ) The number 3
( ) An error

# BEGIN SOLUTION

**Answer:** The number 3

`plum.groupby('Opp').max()` finds the largest value in the `'Date'`, `'Home'`, `'Won'`, `'PTS'`, `'AST'`, and `'TOV'` columns for each unique `'Opp'` (independently for each column). `grouped = plum.groupby('Opp').max().get(['Date', 'PTS'])` keeps only the `'Date'` and `'PTS'` columns. Note that in `grouped`, the index is `'Opp'`, the column we grouped on.

When `grouped.reset_index()` is called, the index is switched back to the default of 0, 1, 2, 3, 4, and so on. Then, `grouped.reset_index().index` is an `Index` containing the numbers `[0, 1, 2, 3, 4, ...]`, and `np.array(grouped.reset_index().index)` is `np.array([0, 1, 2, 3, 4, ...])`. In this array, the number at position `i` is just `i`, so the number at position `df` is `df`. Here, `df` is the argument to `unknown`, and we were asked for the value of `unknown(3)`, so the correct answer is the number at position 3 in `np.array([0, 1, 2, 3, 4, ...])` which is 3.

Note that if we asked for `unknown(50)` (or `unknown(k)`, where `k` is any integer above 30), the answer would be "An error", since `grouped` could not have had 51 rows. `plum` has 31 rows, so `grouped` has at most 31 rows (but likely less, since Kelsey Plum's team likely played the same opponent multiple times).

<average>72</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

For your convenience, we show the first few rows of `plum` again below.

<center><img src='../assets/images/wi22-final/plum.png' width=40%></center>

Suppose that Plum's team, the Las Vegas Aces, won at least one game in Las Vegas and lost at least one game in Las Vegas. Also, suppose they won at least one game in an opponent's arena and lost at least one game in an opponent's arena.

Consider the DataFrame `home_won`, defined below.

```py
home_won = plum.groupby(['Home', 'Won']).mean().reset_index()
``` 

1. How many rows does `home_won` have?

2. How many columns does `home_won` have?

# BEGIN SOLUTION

**Answer:** 4 rows and 5 columns.

`plum.groupby(['Home', 'Won']).mean()` contains one row for every unique combination of `'Home'` and `'Won'`. There are two values of `'Home'` - `True` and `False` – and two values of `'Won'` – `True` and `False` – leading to 4 combinations. We can assume that there was at least one row in `plum` for each of these 4 combinations due to the assumption given in the problem:

_Suppose that Plum's team, the Las Vegas Aces, won at least one game in Las Vegas and lost at least one game in Las Vegas. Also, suppose they won at least one game in an opponent's arena and lost at least one game in an opponent's arena._

`plum` started with 7 columns: `'Date'`, `'Opp'`, `'Home'`, `'Won'`, `'PTS'`, `'AST'`, and `'TOV'`. After grouping by `['Home', 'Won']` and using `.mean()`, `'Home'` and `'Won'` become the index. The resulting DataFrame contains all of the columns that the `.mean()` aggregation method can work on. We cannot take the mean of `'Date'` and `'Opp'`, because those columns are strings, so `plum.groupby(['Home', 'Won']).mean()` contains a `MultiIndex` with 2 "columns" – `'Home'` and `'Won'` – and 3 regular columns – `'PTS'` `'AST'`, and `'TOV'`. Then, when using `.reset_index()`, `'Home'` and `'Won'` are restored as regular columns, meaning that `plum.groupby(['Home', 'Won']).mean().reset_index()` has $2 + 3 = 5$ columns.

<average>78</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Consider the DataFrame `home_won` once again.

```py
home_won = plum.groupby(['Home', 'Won']).mean().reset_index()
``` 

Now consider the DataFrame `puzzle`, defined below. Note that the only difference between `home_won` and `puzzle` is the use of `.count()` instead of `.mean()`.

```py
puzzle = plum.groupby(['Home', 'Won']).count().reset_index()
``` 

How do the number of rows and columns in `home_won` compare to the number of rows and columns in `puzzle`?

( ) `home_won` and `puzzle` have the same number of rows and columns
( ) `home_won` and `puzzle` have the same number of rows, but a different number of columns
( ) `home_won` and `puzzle` have the same number of columns, but a different number of rows
( ) `home_won` and `puzzle` have both a different number of rows and a different number of columns

# BEGIN SOLUTION

**Answer: ** `home_won` and `puzzle` have the same number of rows, but a different number of columns

All that changed between `home_won` and `puzzle` is the aggregation method. The aggregation method has no influence on the number of rows in the output DataFrame, as there is still one row for each of the 4 unique combinations of `'Home'` and `'Won'`.

However, `puzzle` has 7 columns, instead of 5. In the solution to the above subpart, we noticed that we could not use `.mean()` on the `'Date'` and `'Opp'` columns, since they contained strings. However, we can use `.count()` (since `.count()` just determines the number of non-NA values in each group), and so the `'Date'` and `'Opp'` columns are not "lost" when aggregating. Hence, `puzzle` has 2 more columns than `home_won`.

<average>85</average>

# END SOLUTION

# END SUBPROB

# END PROB