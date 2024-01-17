You may have noticed that San Diego was quite cloudy in May (2023). In fact, according to the National Weather Service, San Diego was the single cloudiest city in the contiguous United States in May, with clouds covering the sky 82% of the time. (Only a remote town in Alaska was cloudier!)

We will work with the DataFrame `sun`, which describes the number of sunshine hours per month in various cities around the world. Each number in `sun` is an average across multiple years and multiple sensors.

The first 2 columns in `sun` are `"Country"` and `"City"`, which are strings describing a particular city. The next 12 columns are `"Jan"`, `"Feb"`, `"Mar"`, ..., `"Dec"`, which describe the number of sunshine hours seen each month. The last column, `"Year"`, is the sum of the month-specific columns.

The first few rows of `sun` are shown below, though `sun` has many more rows than are shown below.

<center><img src='../assets/images/sp23-final/sun.png' width=1000></center>
<br>

For instance, we see that Tashkent, Uzbekistan sees 164.3 sunshine hours in March.

Assume that we have already run `import babypandas as bpd` and `import numpy as np`.