# BEGIN PROB

Which of the following best describes the input and output types of the `.apply` Series method?

( ) input: string, output: Series
( ) input: Series, output: function
( ) input: function, output: Series
( ) input: function, output: function

# BEGIN SOLUTION

**Answer: ** input: function, output: Series

It helps to think of an example of how we typically use `.apply`. Consider a DataFrame called `books` and a function called `year_to_century` that converts a year to the century it belongs to. We might use `.apply` as follows:

`books.assign(publication_century = books.get('publication_year').apply(year_to_century))`

`.apply` is called a Series method because we use it on a Series. In this case that Series is `books.get('publication_year')`. `.apply` takes one input, which is the name of the function we wish to apply to each element of the Series. In the example above, that function is `year_to_century`. The result is a Series containing the centuries for each book in the `books` DataFrame, which we can then assign back as a new column to the DataFrame. So `.apply` therefore takes as input a function and outputs a Series.

<average>98</average>
# END SOLUTION

# END PROB