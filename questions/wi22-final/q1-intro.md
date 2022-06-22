Welcome to the Final Exam for DSC 10 this quarter! In this exam, we will use data from the 2021 Women's National Basketball Association (WNBA) season. In basketball, players score points by shooting the ball into a hoop. The team that scores the most points wins the game.

Kelsey Plum, a WNBA player, attended La Jolla Country Day School, which is adjacent to UCSD's campus. Her current team is the Las Vegas Aces (three-letter code `'LVA'`). **In 2021, the Las Vegas Aces played 31 games, and Kelsey Plum played in all 31.**

The DataFrame `plum` contains her stats for all games the Las Vegas Aces played in 2021. The first few rows of `plum` are shown below (though the full DataFrame has 31 rows, not 5):

<center><img src='../assets/images/fa21-final/plum.png' width=30%></center>

Each row in `plum` corresponds to a single game. For each game, we have:

- `'Date'` (`str`), the date on which the game was played
- `'Opp'` (`str`), the three-letter code of the opponent team
- `'Home'` (`bool`), `True` if the game was played in Las Vegas ("home") and `False` if it was played at the opponent's arena ("away")
- `'Won'` (`bool`), `True` if the Las Vegas Aces won the game and `False` if they lost
- `'PTS'` (`int`), the number of points Kelsey Plum scored in the game
- `'AST'` (`int`), the number of assists (passes) Kelsey Plum made in the game
- `'TOV'` (`int`), the number of turnovers Kelsey Plum made in the game (a turnover is when you lose the ball – turnovers are bad!)

#### Part A

What type of visualization is best suited for visualizing the trend in the number of points Kelsey Plum scored per game in 2021?

- Histogram
- Bar chart
- Line chart
- Scatter plot

#### Part B

Fill in the blanks below so that `total_june` evaluates to the total number of points Kelsey Plum scored in June.

```py
june_only = plum[__(a)__]
total_june = june_only.__(b)__
```

- What goes in blank (a)?

- What goes in blank (b)?

#### Part C

Consider the function `unknown`, defined below.

```py
def unknown(df):
    grouped = plum.groupby('Opp').max().get(['Date', 'PTS'])
    return np.array(grouped.reset_index().index)[df]
```

What does `unknown(3)` evaluate to?

- `'2021-06-05'`
- `'WAS'`
- The date on which Kelsey Plum scored the most points
- The three-letter code of the opponent on which Kelsey Plum scored the most points
- The number 0
- The number 3
- An error

#### Part D

For your convenience, we show the first few rows of `plum` again below.

<center><img src='../assets/images/fa21-final/plum.png' width=30%></center>

Suppose that Plum's team, the Las Vegas Aces, won at least one game in Las Vegas and lost at least one game in Las Vegas. Also, suppose they won at least one game in an opponent's arena and lost at least one game in an opponent's arena.

Consider the DataFrame `home_won`, defined below.

```py
home_won = plum.groupby(['Home', 'Won']).mean().reset_index()
``` 

- How many rows does `home_won` have?

- How many columns does `home_won` have?


### BEGIN SOLUTION

<h4>Part A</h4>

Line chart.

Here, there are two quantitative variables (number of points and game number), and one of them involves some element of time (game number). Line charts are appropriate when one quantitative variable is time.

<br>

<h4>Part B</h4>

Blank (a): <code>plum.get('Date').str.contains('-06-')</code>

Blank (b): <code>get('PTS').sum()</code>

<br>

<h4>Part C</h4>

The number 3.

When we group by ... Then, ...

<br>

<h4>Part D</h4>

<code>home_won</code> has n rows and d columns.

### END SOLUTION