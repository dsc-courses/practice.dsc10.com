Bill has opened a bookstore, called Bill's Book Bonanza. In the DataFrame `bookstore`, each row corresponds to a unique book available at this bookstore. The index is `"ISBN"` (`int`), which is a unique identifier for books. The columns are:

- `"title"` (`str`): The title of the book. 
- `"author"` (`str`): The author of the book.
- `"genre"` (`str`): The primary genre of the book.
- `"pages"` (`int`): The number of pages in the book.
- `"rating"` (`float`): The rating of the book, out of 5 stars. This data comes from Goodreads, a book review website.

The first three rows are shown below, though `bookstore` has many more rows than pictured.

<center><img src='../assets/images/fa24-final/short_books.jpg' width=800></center>

Additionally, we are given a dataset of `sales`, which lists all the book purchases made from Bill's Book Bonanza since it opened. The columns of `sales` are:

- `"ISBN"` (`str`): The unique identifier for the book.
- `"price"` (`float`): The price of the book at Bill's Book Bonanza.
- `"cash"` (`bool`): `True` if the purchase was made in cash and `False` if not.
- `"date"` (`str`): The date the book purchase was made, using the format `"Day of the Week, Month Day, Year"`. See below for examples.

The first three rows of `sales` are shown below, though `sales` has many more rows than this. 

<center><img src='../assets/images/fa24-final/short_sales.jpg' width=700></center>

Throughout this exam, we will refer to `bookstore` and `sales` repeatedly.

Assume that we have already run `import babypandas as bpd`, `import numpy as np`, and `import scipy`.
