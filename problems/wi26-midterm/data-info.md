Living in San Diego, we have a plethora of great food options, especially pizza!

In this exam, we'll work with a dataset of pizza slices sold at fictional pizza shops in San Diego. Each row in the DataFrame `pizza` corresponds to a type of pizza slice, specific to the store in which it is sold.

The DataFrame `pizza` contains the following columns:

- `"store"` (`str`): The name of the pizza store.
- `"kind"` (`str`): The kind of pizza slice (cheese, pepperoni, supreme, etc).
- `"price_per_slice"` (`float`): The price of a single slice of pizza.
- `"gluten_free"` (`bool`): Whether or not the pizza slice is also offered in a gluten-free version.
- `"num_ingredients"` (`int`): The number of ingredients required to make the pizza slice.
- `"rating"` (`float`): The average rating—out of 5—of the pizza slice.
- `"neighborhood"` (`str`): The neighborhood where the pizza store is located.

The first 10 rows of the DataFrame `pizza` are shown below, but the full DataFrame is much larger.

<center><img src="../assets/images/wi26-midterm/pizza_dataframe.png" width=800></center>


Assume that we have already run `import babypandas as bpd` and `import numpy as np`.
