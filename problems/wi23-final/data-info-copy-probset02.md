The DataFrame `games` contains information about a sample of popular games, including board games, dice games, and card games. The data comes from Board Game Geek, a popular website and vibrant online community for game enthusiasts.

The columns of games are as follows.

- `"Name"` (`str`): The name of the game.
- `"Mechanics"` (`str`): A sequence of descriptors for how the game is played. A game can have several descriptors, each of which is separated by a comma.
- `"Domains"` (`str`): A sequence of domains to which the game belongs. A game can belong to multiple domains.
- `"Play Time"` (`int`): The average play time of the game, in minutes, as suggested by the game’s creators.
- `"Complexity"` (`float`): The average complexity of the game, on a scale of 1 to 5 points, as reported by Board Game Geek community members.
- `"Rating"` (`str`): The average rating of the game, on a scale of 1 to 10 points, as rated by Board Game Geek community members. Note that while this data should be numerical, it is actually stored as a string, because some entries use a comma in place of a decimal point. For example 8,79 actually represents the number 8.79.
- `"BGG Rank"` (`int`): The rank of the game in Board Game Geek’s database. The formula for how this rank is calculated is not publicly known, but it likely includes many factors, such as `"Rating"`, number of registered owners of the game, and number of reviews.

The first few rows of `games` are shown below (though `games` has many more rows than pictured here).

<center><img src='../assets/images/wi23-final/preview.jpg' width=100%></center>
<br>

Assume that we have already run `import babypandas as bpd` and `import numpy as np`.