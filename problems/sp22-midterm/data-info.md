Welcome to Sun God!

<center><img src='../assets/images/sp22-midterm/cartoon.png' width=20%></center>

After a two-year hiatus due to the pandemic, UCSD's annual music festival, the Sun God festival, is back this year! In this exam, we'll be looking at a DataFrame named `sungod` that contains information on the artists who have performed at Sun God in years past. **For each year that the festival was held, we have one row for each artist that performed that year.** The columns are:

- `'Year'` (`int`): the year of the festival
- `'Artist'` (`str`): the name of the artist
- `'Appearance_Order'` (`int`): the order in which the artist appeared in that year's festival (1 means they came onstage first)

The rows of `sungod` are arranged in **no particular order**. The first few rows of `sungod` are shown below (though `sungod` has **many more rows** than pictured here).

<center><img src='../assets/images/sp22-midterm/sungod.png' width=30%></center>

Assume:

- Only one artist ever appeared at a time (for example, we can't have two separate artists with a `'Year'` of 2015 and an `'Appearance_Order'` of 3). 
- An artist may appear in multiple different Sun God festivals (they could be invited back).
- We have already run `import babypandas as bpd` and `import numpy as np`.

**Throughout this exam, we will refer to `sungod` repeatedly.**

**Tip:** Open this page in another tab, so that it is easy to refer to this data description as you work through the exam.