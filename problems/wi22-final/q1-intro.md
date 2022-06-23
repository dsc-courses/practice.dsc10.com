# BEGIN PROB

Welcome to the Final Exam for DSC 10 this quarter! In this exam, we will use data from the 2021 Women's National Basketball Association (WNBA) season. In basketball, players score points by shooting the ball into a hoop. The team that scores the most points wins the game.

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

# BEGIN SUBPROB

What type of visualization is best suited for visualizing the trend in the number of points Kelsey Plum scored per game in 2021?

1. Histogram
2. Bar chart
3. Line chart
4. Scatter plot

# BEGIN SOLUTION

3. Line chart

Here, there are two quantitative variables (number of points and game number), and one of them involves some element of time (game number). Line charts are appropriate when one quantitative variable is time.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Fill in the blanks below so that `total_june` evaluates to the total number of points Kelsey Plum scored in June.

```py
june_only = plum[__(a)__]
total_june = june_only.__(b)__
```

1. What goes in blank (a)?

2. What goes in blank (b)?

# BEGIN SOLUTION

1. Blank (a): `plum.get('Date').str.contains('-06-')`

2. Blank (b): `get('PTS').sum()`

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Consider the function `unknown`, defined below.

```py
def unknown(df):
    grouped = plum.groupby('Opp').max().get(['Date', 'PTS'])
    return np.array(grouped.reset_index().index)[df]
```

What does `unknown(3)` evaluate to?

1. `'2021-06-05'`
2. `'WAS'`
3. The date on which Kelsey Plum scored the most points
4. The three-letter code of the opponent on which Kelsey Plum scored the most points
5. The number 0
6. The number 3
7. An error

# BEGIN SOLUTION

6. The number 3

Here's why...

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

`home_won` has $n$ rows and $d$ columns.

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

1. `home_won` and `puzzle` have the same number of rows and columns
2. `home_won` and `puzzle` have the same number of rows, but a different number of columns
3. `home_won` and `puzzle` have the same number of columns, but a different number of rows
4. `home_won` and `puzzle` have both a different number of rows and a different number of columns

# BEGIN SOLUTION

2. `home_won` and `puzzle` have the same number of rows, but a different number of columns

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

For your convenience, we show the first few rows of `plum` again below.

<center><img src='../assets/images/wi22-final/plum.png' width=40%></center>

There is exactly one team in the WNBA that Plum's team did not win any games against during the 2021 season. Fill in the blanks below so that `never_beat` evaluates to a string containing the three-letter code of that team.

```py
never_beat = plum.groupby(__(a)__).sum().__(b)__
```

1. What goes in blank (a)?

2. What goes in blank (b)?

# BEGIN SOLUTION

1. Blank (a): `'Opp'`

2. Blank (b): `sort_values('Won').index[0]`

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Recall that `plum` has 31 rows, one corresponding to each of the 31 games Kelsey Plum's team played in the 2021 WNBA season.

Fill in the blank below so that `win_bool` evaluates to `True`.

```py
def modify_series(s):
    return __(a)__

n_wins = plum.get('Won').sum()
win_bool = n_wins == (31 + modify_series(plum.get('Won')))
```

What goes in blank (a)?

1. `-s.sum()`
2. `-(s == False).sum()`
3. `len(s) - s.sum()`
4. `not s.sum()`
5. `-s[s.get('Won') == False].sum()`

# BEGIN SOLUTION

2. `-(s == False).sum()`

# END SOLUTION

# END SUBPROB

# END PROB