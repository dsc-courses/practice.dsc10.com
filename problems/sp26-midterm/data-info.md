A college mascot is a costumed character that represents the school at athletic competitions and other major campus events. For example, you might see UCSD's mascot, King Triton, at basketball games and the upcoming Sun God Festival.

College students can apply to serve as the mascot for their school, which is quite competitive! Applicants usually need to fall within a certain height range to fit the costume. Throughout this exam, we will format heights in feet and inches, for example `"5ft 7in"` or `"6ft"`, omitting inches when the height is a whole number of feet, as in the second example. Recall that there are 12 inches in one foot.

The DataFrame `mascots` has one row for every college or university in the US with a named mascot. The columns are:

- `"school"` (`str`): The name of the school. This column has no repeated values.
- `"mascot"` (`str`): The name of the school's mascot.
- `"type"` (`str`): Mascot category, either `"human"`, `"animal"`, or `"other"`.
- `"height"` (`str`): The range of heights that fit into the mascot costume. Values consist of two heights, formatted as described above, separated by `" - "`.
- `"team"` (`str`): The general name of the school's athletic team.
- `"colors"` (`list`): A list of the school colors. Each school has at least one school color.

The first few rows of `mascots` are shown below, though `mascots` has many more rows than pictured.

<center><img src="https://raw.githubusercontent.com/dsc-courses/practice.dsc10.com/refs/heads/master/assets/images/sp26-midterm/mascots.jpg" width=650></center>

Throughout this exam, we will refer to `mascots` repeatedly. Assume that we have already run `import babypandas as bpd` and `import numpy as np`.