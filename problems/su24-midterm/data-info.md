In this exam, you’ll work with a data set representing the results of the Collegiate Mario Kart League. Each row represents a team and their performance in the league.
The columns of `kart` are as follows:
- `"Ranking" (int):` The team’s ranking within their division. Rankings are from 1
to 6, with the best teams receiving rank 1 and the worst teams receiving rank 6.
- `"Team" (str):` The name of the team.
- `"University" (str):` The university the team represents.
- `"Division" (str):` The division in which the team competes (Division 1 or Division 2). Each division includes six teams.
- `"Total Points" (int):` The total points scored by the team during the season.
- `"Races Won" (int):` The total number of races won by the team.
- `"Region" (str):` The geographic region of the university.

The first few rows of `kart` are shown below, though `kart` has `12` rows in total (since there
are `12` teams total, `6` in each division).

<center><img src='../assets/images/su24-midterm/kart_dataframe.png' width=20%></center>
<br>

Assume that we have already run `import babypandas as bpd` and `import numpy as np.`
