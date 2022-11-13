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

# BEGIN SUBPROB

**Note:** For the rest of the exam, assume that the index of `season` is still 0, 1, 2, 3, ...

Below is a histogram showing the distribution of the number of turnovers per game for all players in `season`.

<center><img src='../assets/images/wi22-final/tpg-hist.png' width=40%></center>

Suppose, **throughout this question**, that the mean number of turnovers per game is 1.25. Which of the following is closest to the median number of turnovers per game?

( ) 0.5
( ) 0.75
( ) 1
( ) 1.25
( ) 1.5
( ) 1.75

# BEGIN SOLN

**Answer:** 1

The median of a distribution is the value that is "halfway" through the distribution, i.e. the value such that half of the values in the distribution are larger than it and half the values in the distribution are smaller than it. 

Visually, we're looking for the location on the $x$-axis where we can draw a vertical line that splits the area of the histogram in half. While it's impossible to tell the exact median of the distribution, since we don't know how the values are distributed within the bars, we can get pretty close by using this principle.

Immediately, we can rule out 0.5, 0.75, 1.5, and 1.75, since they are too far from the "center" of the distribution (imagine drawing vertical lines at any of those points on the $x$-axis; they don't split the distribution's area in half). To decide between 1 and 1.25, we can use the fact that the distribution is _right-skewed_, meaning that its mean is larger than its median (intuitively, the mean is dragged in the direction of the tail, which is to the right). This means that the median should be less than the mean. We are given that the mean of the distribution is 1.25, so the median should be 1.

<average>73</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Sabrina Ionescu and Sami Whitcomb are both players on the New York Liberty, and are both California natives.

In "original units", Sabrina Ionescu had 3.5 turnovers per game. In standard units, her turnovers per game is 3.

In standard units, Sami Whitcomb's turnovers per game is -1. How many turnovers per game did Sami Whitcomb have in **original units**? Round your answer to 3 decimal places.

**Note:** You will need the fact from the previous subpart that the mean number of turnovers per game is 1.25.

# BEGIN SOLN

**Answer:** 0.5

To convert a value $x$ to standard units (denoted by $x_{\text{su}}$), we use the following formula:

$$x_{\text{su}} = \frac{x - \text{mean of }x}{\text{SD of }x}$$

Let's look at the first line given to us: _In "original units", Sabrina Ionescu had 3.5 turnovers per game. In standard units, her turnovers per game is 3._

Substituting the information we know into the above equation gives us:

$$3 = \frac{3.5 - 1.25}{\text{SD of }x}$$

In order to convert future values from original units to standard units, we'll need to know $\text{SD of }x$, which we don't currently but can obtain by rearranging the above equation. Doing so yields

$$\text{SD of }x = \frac{3.5-1.25}{3} = \frac{2.25}{3} = 0.75$$

Now, let's look at the second line we're given: _In standard units, Sami Whitcomb's turnovers per game is -1. How many turnovers per game did Sami Whitcomb have in **original units**? Round your answer to 3 decimal places._

We have all the information we need to convert Sami Whitcomb's turnovers per game from standard units to original units! Plugging in the values we know gives us:

$$\begin{aligned} x_{\text{su}} &= \frac{x - \text{mean of }x}{\text{SD of }x} \\ -1 &= \frac{x - 1.25}{0.75} \\ -0.75 &= x - 1.25 \\ 1.25 - 0.75 &= x \\ x &= \boxed{0.5} \end{aligned}$$

Thus, in original units, Sami Whitcomb averaged 0.5 turnovers per game.

<average>87</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

What is the **smallest** possible number of turnovers per game, in **standard units**? Round your answer to 3 decimal places.

# BEGIN SOLN

**Answer:** -1.667

The smallest possible number of turnovers per game in original units is 0 (which a player would have if they never had a turnover – that would mean they're really good!). To find the smallest possible turnovers per game in standard units, all we need to do is convert 0 from original units to standard units. This will involve our work from the previous subpart.

$$\begin{aligned} x_{\text{su}} &= \frac{x - \text{mean of }x}{\text{SD of }x} \\ &= \frac{0 - 1.25}{0.75} \\ &= -\frac{1.25}{0.75} \\ &= -\frac{5}{3} = \boxed{-1.667} \end{aligned}$$

<average>82</average>

# END SOLN

# END SUBPROB

# END PROB