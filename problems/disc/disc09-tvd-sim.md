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

- Free Throws: $|0.05 - 0.2| = 0.15$
- Threes: $|0.35 - 0.2| = 0.15$
- Midrange: $|0.35 - 0.3| = 0.05$
- Layups: $|0.25 - 0.3| = 0.05$

Then, we have

$$\text{TVD} = \frac{1}{2} (0.15 + 0.15 + 0.05 + 0.05) = 0.2$$

<average>84</average>

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

3. What goes in blank (c)?

# BEGIN SOLUTION

**Answers:** 1, `np.arange(1, 50)`, `most_sim_player = player`

Let's try and understand the code provided to us. It appears that we're looping over the names of all other players, each time computing the TVD between Kelsey Plum's shot distribution and that player's shot distribution. If the TVD calculated in an iteration of the `for`-loop (`player_tvd`) is less than the previous lowest TVD (`lowest_tvd_so_far`), the current player (`player`) is now the most "similar" to Kelsey Plum, and so we store their TVD and name (in `most_sim_player`).

Before the `for`-loop, we haven't looked at any other players, so we don't have values to store in `most_sim_player` and `lowest_tvd_so_far`. On the first iteration of the `for`-loop, both of these values need to be updated to reflect Kelsey Plum's similarity with the first player in `other_players`. This is because, if we've only looked at one player, that player is the most similar to Kelsey Plum. `most_sim_player` is already initialized as an empty string, and we will specify how to "update" `most_sim_player` in blank (c). For blank (a), we need to pick a value of `lowest_tvd_so_far` that we can **guarantee** will be updated on the first iteration of the `for`-loop. Recall, TVDs range from 0 to 1, with 0 meaning "most similar" and 1 meaning "most different". This means that no matter what, the TVD between Kelsey Plum's distribution and the first player's distribution will be less than 1*, and so if we initialize `lowest_tvd_so_far` to 1 before the `for`-loop, we know it will be updated on the first iteration. 

- It's possible that the TVD between Kelsey Plum's shot distribution and the first other player's shot distribution is equal to 1, rather than being less than 1. If that were to happen, our code would still generate the correct answer, but `lowest_tvd_so_far` and `most_sim_player` wouldn't be updated on the first iteration. Rather, they'd be updated on the first iteration where `player_tvd` is strictly less than 1. (We'd expect that the TVDs between all pairs of players are neither exactly 0 nor exactly 1, so this is not a practical issue.) To avoid this issue entirely, we could change `if player_tvd < lowest_tvd_so_far` to `if player_tvd <= lowest_tvd_so_far`, which would make sure that even if the first TVD is 1, both `lowest_tvd_so_far` and `most_sim_player` are updated on the first iteration.
- Note that we could have initialized `lowest_tvd_so_far` to a value larger than 1 as well. Suppose we initialized it to 55 (an arbitrary positive integer). On the first iteration of the `for`-loop, `player_tvd` will be less than 55, and so `lowest_tvd_so_far` will be updated.

Then, we need `other_players` to be an array containing the names of all players other than Kelsey Plum, whose name is stored at position 0 in `breakdown.columns`. We are told that there are 50 players total, i.e. that there are 50 columns in `breakdown`. We want to `take` the elements in `breakdown.columns` at positions 1, 2, 3, ..., 49 (the last element), and the call to `np.arange` that generates this sequence of positions is `np.arange(1, 50)`. (Remember, `np.arange(a, b)` does not include the second integer!)

In blank (c), as mentioned in the explanation for blank (a), we need to update the value of `most_sim_player`. (Note that we only arrive at this line if `player_tvd` is the lowest pairwise TVD we've seen so far.) All this requires is `most_sim_player = player`, since `player` contains the name of the player who we are looking at in the current iteration of the `for`-loop.

<average>70</average>

# END SOLUTION

# END SUBPROB

# END PROB