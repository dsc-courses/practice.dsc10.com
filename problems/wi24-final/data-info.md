The Olympic Games are the world’s leading international sporting event, dating back to ancient Greece. 
Today, we’ll explore data on modern Olympic medalists. Each row in the DataFrame `olympians` corresponds to a type of medal earned by one Olympic athlete in one year. 

The columns of `olympians` are as follows:

- `"Name"` (`str`): The name of the athlete. Unique for each athlete.
- `"Sex"` (`str`): The sex of the athlete, denoted by "M" or "F".
- `"Age"` (`int`): The age of the athlete at the time of the Olympics.
- `"Height"` (`float`): The height of the athlete in centimeters.
- `"Weight"` (`float`): The weight of the athlete in kilograms.
- `"Sport"` (`str`): The sport in which the athlete competed.
- `"Team"` (`str`): The team or country the athlete represented.
- `"Medal"` (`str`): The type of medal won ("Gold", "Silver", or "Bronze").
- `"Year"` (`int`): The year of the Olympic Games.
- `"Count"` (`int`): The number of medals of this type earned by this athlete in this year.

The first few rows of `olympians` are shown below, though `olympians` has many more rows than pictured.
The data in `olympians` is only a sample from the much larger population of all Olympic medalists.

<center><img src='../assets/images/wi24-final/medalists.jpg' width=45%></center>
<br>

Throughout this exam, assume that we have already run `import babypandas as bpd` and
`import numpy as np`.
