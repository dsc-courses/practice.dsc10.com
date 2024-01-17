# BEGIN PROB

In addition to the `plum` DataFrame, we also have access to the `season` DataFrame, which contains statistics on all players in the WNBA in the 2021 season. The first few rows of `season` are shown below. (Remember to keep the data description from the top of the exam open in another tab!)

<center><img src='../assets/images/wi22-final/seasons.png' width=40%></center>

Each row in `season` corresponds to a single player. For each player, we have:
- `'Player'` (`str`), their name
- `'Team'` (`str`), the three-letter code of the team they play on
- `'G'` (`int`), the number of games they played in the 2021 season
- `'PPG'` (`float`), the number of points they scored per game played
- `'APG'` (`float`), the number of assists (passes) they made per game played
- `'TPG'` (`float`), the number of turnovers they made per game played

Note that all of the numerical columns in `season` must contain values that are greater than or equal to 0.

# BEGIN SUBPROB

Which of the following is the best choice for the index of `season`?

( ) `'Player'`
( ) `'Team'`
( ) `'G'`
( ) `'PPG'`

# BEGIN SOLN

**Answer:** `'Player'`

Ideally, the index of a DataFrame is unique, so that we can use it to "identify" the rows. Here, each row is about a player, so `'Player'` should be the index. `'Player'` is the only column that is likely to be unique; it is possible that two players have the same name, but it's still a _better_ choice of index than the other three options, which are definitely not unique.

<average>95</average>

# END SOLN

# END SUBPROB

# END PROB