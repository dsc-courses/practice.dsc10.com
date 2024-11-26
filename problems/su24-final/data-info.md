In this exam, you’ll work with a data set representing the results of the Tour de France, a
multi-stage, weeks-long cycling race. The Tour de France takes place over many days each
year, and on each day, the riders compete in individual races called `stages`. Each `stage` is
a standalone race, and the winner of the entire tour is determined by who performs the best
across all of the individual `stages` combined. Each row represents one stage of the Tour (or
equivalently, one day of racing). This dataset will be called `stages`.

The columns of `stages` are as follows:
- `"Stage" (int):` The stage number for the respective year.
- `"Date" (str):` The day that the stage took place, formatted as ”YYYY-MM-DD.”
- `"Distance" (float):` The distance of the stage in kilometers.
- `"Origin" (str):` The name of the city in which the stage starts.
- `"Destination" (str):` The name of the city in which the stage ends.
- `"Type" (str):` The type of the stage.
- `"Winner" (str):` The name of the rider who won the stage
- `"Winner Country" (str):` The country from which the winning rider of the stage is from

The first few rows of `stages` are shown below, though `stages` has many more rows than
pictured.

<center><img src='../assets/images/su24-final/tour_df.png' width=800></center>
<br>

Throughout this exam, we will refer to `stages` repeatedly.
Assume that we have already run `import babypandas as bpd `and `import numpy as np`.