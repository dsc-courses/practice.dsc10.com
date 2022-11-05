IKEA is a Swedish furniture company that designs and sells ready-to-assemble furniture and other home furnishings. 

<center><img src='../assets/images/sp22-final/wordless_instructions.png' width=40%></center>



An IKEA fan created an app where people can log the amount of time it took them to assemble their IKEA furniture. The DataFrame `app_data` has a row for each product build that was logged on the app. The columns are:

- `'product'` (`str`): the name of the product, which includes the product line as the first word, followed by a description of the product
- `'category'` (`str`): a categorical description of the type of product
- `'assembly_time'` (`str`): the amount of time to assemble the product, formatted as `'x hr, y min'` where `x` and `y` represent integers, possibly zero


The first few rows of `app_data` are shown below, though `app_data` has many more rows than pictured (5000 rows total).

<center><img src='../assets/images/sp22-final/appdatadf.png' height=180></center>

<p>&nbsp;</p>
  

Assume that we have already run `import babypandas as bpd` and `import numpy as np`.  
