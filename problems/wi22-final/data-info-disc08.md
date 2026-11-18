For this question we will use data from the 2021 Women's National Basketball Association (WNBA) season for the next several problems. In basketball, players score points by shooting the ball into a hoop. The team that scores the most points wins the game.

We have access to the `season` DataFrame, which contains statistics on all players in the WNBA in the 2021 season. The first few rows of `season` are shown below.

<center><img src='../assets/images/wi22-final/seasons.png' width=40%></center>

Each row in `season` corresponds to a single player. For each player, we have:
- `'Player'` (`str`), their name
- `'Team'` (`str`), the three-letter code of the team they play on
- `'G'` (`int`), the number of games they played in the 2021 season
- `'PPG'` (`float`), the number of points they scored per game played
- `'APG'` (`float`), the number of assists (passes) they made per game played
- `'TPG'` (`float`), the number of turnovers they made per game played

Note that all of the numerical columns in `season` must contain values that are greater than or equal to 0.