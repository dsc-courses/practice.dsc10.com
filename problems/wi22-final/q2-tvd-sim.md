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

# BEGIN SUBPROB

Let's again consider the shot distributions of Kelsey Plum and Cheney Ogwumike.

<center><img src='../assets/images/wi22-final/tvd.png' width=50%></center>

We define the **maximum squared distance** (MSD) between two categorical distributions as the **largest squared difference between the proportions of any category**.

What is the MSD between Kelsey Plum's shot distribution and Chiney Ogwumike's shot distribution? Give your answer as a **proportion** between 0 and 1 (not a percentage) rounded to three decimal places.

# BEGIN SOLUTION

**Answer:** 0.023

Recall, in the solution to the first subpart of this problem, we calculated the absolute differences between the proportions of each category.

- Free Throws: $|0.05 - 0.2| = 0.15$
- Threes: $|0.35 - 0.2| = 0.15$
- Midrange: $|0.35 - 0.3| = 0.05$
- Layups: $|0.25 - 0.3| = 0.05$

The squared differences between the proportions of each category are computed by squaring the results in the list above (e.g. for Free Throws we'd have $(0.05 - 0.2)^2 = 0.15^2$). To find the maximum squared difference, then, all we need to do is find the largest of $0.15^2$, $0.15^2$, $0.05^2$, and $0.05^2$. Since $0.15 > 0.05$, we have that the maximum squared distance is $0.15^2 = 0.0225$, which rounds to $0.023$.

<average>85</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

For your convenience, we show the first few columns of `breakdown` again below.

<center><img src='../assets/images/wi22-final/head-to-head.png' width=30%></center>

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

1. What goes in blank (a)?
2. What goes in blank (b)?

# BEGIN SOLUTION

**Answers:** `10`, `(shots * possible_points).sum()`

To simulate the number of points Kelsey Plum scores in a single game, we need to:

1. Simulate the number of shots she takes of each type (layups, midranges, threes, free throws).
2. Using the simulated distribution in step 1, find the total number of points she scores – specifically, add 2 for every layup, 2 for every midrange, 3 for every three, and 1 for every free throw.

To simulate the number of shots she takes of each type, we use `np.random.multinomial`. This is because each shot, independently of all other shots, has a 30\% chance of being a layup, a 30\% chance of being a midrange, and so on. What goes in blank (a) is the number of shots she is taking in total; here, that is 10. `shots` will be an array of length 4 containing the number of shots of each type - for instance, `shots` may be `np.array([3, 4, 2, 1])`, which would mean she took 3 layups, 4 midranges, 2 threes, and 1 free throw.

Now that we have `shots`, we need to factor in how many points each type of shot is worth. This can be accomplished by multiplying `shots` with `possible_points`, which was already defined for us. Using the example where `shots` is `np.array([3, 4, 2, 1])`, `shots * possible_points` evaluates to `np.array([6, 8, 6, 1])`, which would mean she scored 6 points from layups, 8 points from midranges, and so on. Then, to find the total number of points she scored, we need to compute the sum of this array, either using the `np.sum` function or `.sum()` method. As such, the two correct answers for blank (b) are `(shots * possible_points).sum()` and `np.sum(shots * possible_points)`.

<average>84</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

True or False: If we call `simulate_points()` 10,000 times and plot a histogram of the results, the distribution will look roughly normal.

( ) True
( ) False

# BEGIN SOLUTION

**Answer: ** True

The answer is True because of the Central Limit Theorem. Recall, the CLT states that no matter what the population distribution looks like, if you take many repeated samples with replacement, the distribution of the sample means and sample sums will be roughly normal. `simulate_points()` returns the sum of a sample of size 10 drawn with replacement from a population, and so if we generate many sample sums, the distribution of those sample sums will be roughly normal.

The distribution we are drawing from is the one below.

<center>
<table class="table" style="width:60%">
  <thead>
    <tr>
      <th scope="col">Type</th>
      <th scope="col">Points</th>
      <th scope="col">Probability</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Layups</th>
      <td>2</td>
      <td>0.3</td>
    </tr>
    <tr>
      <th scope="row">Midrange</th>
      <td>2</td>
      <td>0.3</td>
    </tr>
    <tr>
      <th scope="row">Threes</th>
      <td>3</td>
      <td>0.2</td>
    </tr>
    <tr>
      <th scope="row">Free Throws</th>
      <td>1</td>
      <td>0.2</td>
    </tr>
  </tbody>
</table>
</center>

<average>78</average>

# END SOLUTION

# END SUBPROB

# END PROB