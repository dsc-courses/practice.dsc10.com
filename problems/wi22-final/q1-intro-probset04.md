---
lecture: 9
---

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
home_won = plum.drop(columns=['Date', 'Opp']).groupby(['Home', 'Won']).mean().reset_index()
``` 

1. How many rows does `home_won` have?

2. How many columns does `home_won` have?

# BEGIN SOLUTION

**Answer:** 4 rows and 5 columns.

`plum.drop(columns=['Date', 'Opp']).groupby(['Home', 'Won']).mean()` contains one row for every unique combination of `'Home'` and `'Won'`. There are two values of `'Home'` - `True` and `False` – and two values of `'Won'` – `True` and `False` – leading to 4 combinations. We can assume that there was at least one row in `plum` for each of these 4 combinations due to the assumption given in the problem:

_Suppose that Plum's team, the Las Vegas Aces, won at least one game in Las Vegas and lost at least one game in Las Vegas. Also, suppose they won at least one game in an opponent's arena and lost at least one game in an opponent's arena._

`.drop(columns=['Date', 'Opp'])` removes the two string columns, so `.mean()` can run. After grouping by `['Home', 'Won']`, those two columns become the index, and the remaining columns are `'PTS'`, `'AST'`, and `'TOV'`. `.reset_index()` restores `'Home'` and `'Won'` as regular columns, so `home_won` has $2 + 3 = 5$ columns.

<average>78</average>

# END SOLUTION

# END SUBPROB

# END PROB