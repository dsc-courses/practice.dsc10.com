# BEGIN PROB

Let's suppose there are 4 different types of shots a basketball player can take – layups, midrange shots, threes, and free throws.

The DataFrame `breakdown` has 4 rows and 50 columns – one row for each of the 4 shot types mentioned above, and one column for each of 50 different players. Each column of `breakdown` describes the distribution of shot types for a single player.

The first few columns of `breakdown` are shown below.

<center><img src='../assets/images/wi22-final/head-to-head.png' width=30%></center>

For instance, 30% of Kelsey Plum's shots are layups, 30% of her shots are midrange shots, 20% of her shots are threes, and 20% of her shots are free throws.

# BEGIN SUBPROB

Below, we've drawn an overlaid bar chart showing the shot distributions of Kelsey Plum and Chiney Ogwumike, a player on the Los Angeles Sparks.

<center><img src='../assets/images/wi22-final/tvd.png' width=50%></center>

<br>

What is the **total variation distance** (TVD) between Kelsey Plum's shot distribution and Chiney Ogwumike's shot distribution? Give your answer as a **proportion** between 0 and 1 (not a percentage) rounded to three decimal places.

# BEGIN SOLUTION

**Answer:** 0.2

Recall, the TVD is the sum of the absolute differences in proportions, divided by 2. The absolute differences in proportions for each category are as follows:

- Free throws: $|0.05 - 0.2| = 0.15$
- Threes: $|0.35 - 0.2| = 0.15$
- Midrange: $|0.35 - 0.3| = 0.05$
- Layups: $|0.25 - 0.3| = 0.05$

Then, we have

$$\text{TVD} = \frac{1}{2} (0.15 + 0.15 + 0.05 + 0.05) = 0.2$$

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Recall, `breakdown` has information for 50 different players. We want to find the player whose shot distribution is the **most similar to Kelsey Plum**, i.e. has the lowest TVD with Kelsey Plum's shot distribution.

Fill in the blanks below so that `most_sim_player` evaluates to the name of the player with the most similar shot distribution to Kelsey Plum. Assume that the column named `'Kelsey Plum'` is the first column in `breakdown` (and again that `breakdown` has 50 columns total).

```py
most_sim_player = ''
lowest_tvd_so_far = __(a)__
other_players = np.array(breakdown.columns).take(__(b)__)
for player in other_players:
    player_tvd = tvd(breakdown.get('Kelsey Plum'),
                     breakdown.get(player))
    if player_tvd < lowest_tvd_so_far:
        lowest_tvd_so_far = player_tvd
        __(c)__
```

1. What goes in blank (a)?

( ) -1
( ) -0.5
( ) 0
( ) 0.5
( ) 1
( ) `np.array([])`
( ) `''`

2. What goes in blank (b)?

[____](np.arange(1, 50))

What goes in blank (c)?

[____](most_sim_player = player)

# BEGIN SOLUTION

**Answer:**

1. 1
2. `np.arange(1, 50)`
3. `most_sim_player=player`

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Let's again consider the shot distributions of Kelsey Plum and Cheney Ogwumike.

![Screen_Shot_2022-03-06_at_2.03.57_AM.png](/files/b398bcf4-eca6-4635-a944-dd752d04e57c)

We define the **maximum squared distance** (MSD) between two categorical distributions as the **largest squared difference between the proportions of any category**.

What is the MSD between Kelsey Plum's shot distribution and Chiney Ogwumike's shot distribution? Give your answer as a **proportion** between 0 and 1 (not a percentage) rounded to three decimal places.

# BEGIN SOLUTION

0.023

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

For your convenience, we show the first few columns of `breakdown` again below.

![Screen_Shot_2022-03-06_at_1.56.40_AM.png](/files/e23acc3e-726b-4b07-92b2-a30c7e4047bc)

In basketball:
- layups are worth 2 points,
- midrange shots are worth 2 points,
- threes are worth 3 points, and
- free throws are worth 1 point

Suppose that Kelsey Plum is guaranteed to shoot exactly 10 shots a game. The type of each shot is drawn from the `'Kelsey Plum'` column of `breakdown` (meaning that, for example, there is a 30% chance each shot is a layup). 

Fill in the blanks below to complete the definition of the function `simulate_points`, which simulates the number of points Kelsey Plum scores in a single game. (`simulate_points` should return a single number.)

```py
def simulate_points():
    shots = np.random.multinomial(__(a)__, breakdown.get('Kelsey Plum'))
    possible_points = np.array([2, 2, 3, 1])
    return __(b)__
```

What goes in blank (a)?

[____](10)

What goes in blank (b)?

[____]((shots * possible_points).sum())

# BEGIN SOLUTION

Just proof that we can use images in solutions!

<center><img src='../assets/images/wi22-final/test.png' width=40%></center>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

True or False: If we call `simulate_points()` 10,000 times and plot a histogram of the results, the distribution will look roughly normal.

1. True
2. False

# BEGIN SOLUTION

**True**

Recall, the central limit theorem states that the distribution of...

# END SOLUTION

# END SUBPROB

# END PROB