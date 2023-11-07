An IKEA fan created an app where people can log the amount of time it took them to assemble their IKEA furniture. The DataFrame `app_data` has a row for each product build that was logged on the app. The columns are:

- `'product'` (`str`): the name of the product, which includes the product line as the first word, followed by a description of the product
- `'category'` (`str`): a categorical description of the type of product
- `'assembly_time'` (`str`): the amount of time to assemble the product, formatted as `'x hr, y min'` where `x` and `y` represent integers, possibly zero
-  `'minutes'` (`int`): integer values representing the number of minutes it took to assemble each product