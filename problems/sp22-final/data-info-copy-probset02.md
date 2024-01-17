IKEA is a Swedish furniture company that designs and sells ready-to-assemble furniture and other home furnishings. IKEA has locations worldwide, including one in San Diego. IKEA is known for its cheap prices, modern designs, huge showrooms, and wordless instruction manuals. They also sell really good Swedish meatballs in their cafe!

Here are the DataFrames you'll be working with:

1. `ikea`
    
The `ikea` DataFrame has a row for each ready-to-assemble IKEA furniture product. The columns are:

- `'product'` (`str`): the name of the product, which includes the product line as the first word, followed by a description of the product
- `'category'` (`str`): a categorical description of the type of product
- `'price'` (`int`): the current price of the product, in dollars
- `'assembly_cost'` (`int`): the additional cost to have the product assembled, in dollars
- `'packages'` (`int`): the number of packages in which the product is boxed


The first few rows of `ikea` are shown below, though `ikea` has many more rows than pictured.

<center><img src='../assets/images/sp22-final/ikeadf.png' height=250></center>
<br>

2. `app_data`

An IKEA fan created an app where people can log the amount of time it took them to assemble their IKEA furniture. The DataFrame `app_data` has a row for each product build that was logged on the app. The columns are:

- `'product'` (`str`): the name of the product, which includes the product line as the first word, followed by a description of the product
- `'category'` (`str`): a categorical description of the type of product
- `'assembly_time'` (`str`): the amount of time to assemble the product, formatted as `'x hr, y min'` where `x` and `y` represent integers, possibly zero
-  `'minutes'` (`int`): integer values representing the number of minutes it took to assemble each product


The first few rows of `app_data` are shown below, though `app_data` has many more rows than pictured (5000 rows total).

<center><img src='../assets/images/sp22-final/appdatadf.png' height=180></center>
<br>

Assume that we have already run `import babypandas as bpd` and `import numpy as np`.


