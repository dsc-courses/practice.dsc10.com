One month ago today, President Donald Trump announced his plan to impose so-called "reciprocal" tariffs on goods imported into the US from other countries. Tariffs are taxes charged by a government on imported goods, at a specific percentage of the value of the goods.

At a "Liberation Day" ceremony outside the White House, Trump held up a printed chart of countries, the tariffs they charge to the US, and the planned reciprocal tariff on goods from that country into the US. We have the data from that printed chart stored in the `tariffs` DataFrame, whose first few rows are shown below. `tariffs` contains 50 rows in total.

<center><img src="../assets/images/sp25-midterm/preview.jpg" width=500></center>

Note that the `"Tariffs Charged to USA"` and `"Reciprocal Tariff"` columns contain `int` values representing percentages. For example, a  $\$200$ product from China would be subject to a $34\%$ tariff, which is a $\$68$ tax. 

Assume that we have already run `import babypandas as bpd` and `import numpy as np`.