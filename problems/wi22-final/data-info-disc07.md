For this question, we will use data from the 2021 Women's National Basketball Association (WNBA) season for the next several problems. In basketball, players score points by shooting the ball into a hoop. The team that scores the most points wins the game.

Kelsey Plum, a WNBA player, attended La Jolla Country Day School, which is adjacent to UCSD's campus. Her current team is the Las Vegas Aces (three-letter code `'LVA'`). **In 2021, the Las Vegas Aces played 31 games, and Kelsey Plum played in all 31.**

The DataFrame `plum` contains her stats for all games the Las Vegas Aces played in 2021. The first few rows of `plum` are shown below (though the full DataFrame has 31 rows, not 5):

<center><img src='../assets/images/wi22-final/plum.png' width=40%></center>

Each row in `plum` corresponds to a single game. For each game, we have:

- `'Date'` (`str`), the date on which the game was played
- `'Opp'` (`str`), the three-letter code of the opponent team
- `'Home'` (`bool`), `True` if the game was played in Las Vegas ("home") and `False` if it was played at the opponent's arena ("away")
- `'Won'` (`bool`), `True` if the Las Vegas Aces won the game and `False` if they lost
- `'PTS'` (`int`), the number of points Kelsey Plum scored in the game
- `'AST'` (`int`), the number of assists (passes) Kelsey Plum made in the game
- `'TOV'` (`int`), the number of turnovers Kelsey Plum made in the game (a turnover is when you lose the ball – turnovers are bad!)
