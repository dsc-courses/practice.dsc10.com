# BEGIN PROB

# BEGIN SUBPROB

The DataFrame `plum` contains Kelsey Plum's stats for all games the Las Vegas Aces played in 2021. The first few rows of `plum` are shown below (though the full DataFrame has 31 rows, not 5):

<center><img src='../assets/images/wi22-final/plum.png' width=40%></center>

Each row in `plum` corresponds to a single game. For each game, we have:

- `'Date'` (`str`), the date on which the game was played
- `'Opp'` (`str`), the three-letter code of the opponent team
- `'Home'` (`bool`), `True` if the game was played in Las Vegas ("home") and `False` if it was played at the opponent's arena ("away")
- `'Won'` (`bool`), `True` if the Las Vegas Aces won the game and `False` if they lost
- `'PTS'` (`int`), the number of points Kelsey Plum scored in the game
- `'AST'` (`int`), the number of assists (passes) Kelsey Plum made in the game
- `'TOV'` (`int`), the number of turnovers Kelsey Plum made in the game (a turnover is when you lose the ball – turnovers are bad!)

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

# END PROB