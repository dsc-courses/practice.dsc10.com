# BEGIN PROB

You are given a table called books that contains columns `'author'` (`str`), `'title'` (`str`), `'num_chapters'` (`int`), and `'publication_year'` (`int`).
# BEGIN SUBPROB

What will be the output of the following code?
`books.groupby(“publication_year”).mean().shape[1]`

( ) `1`
( ) `2`
( ) `3`
( ) `4`

# BEGIN SOLUTION

**Answer: ** `1`

The output will return 1. Notice that the final function call is to `.shape[1]`. We know
that `.shape[1]` is a call to see how many columns are in the resulting data frame. When we 
group by publication year, there is only one column that will be aggregated by the groupby call (which
is the `'num_chapters'` column). The other columns are string, and therefore, will not be aggregated in the groupby
call (since you can't take the mean of a string). Consequently `.shape[1]` will only result one column for the mean of the `'num_chapters'` 
column. 

<average>67</average>
# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Which of the following strategies would work to compute the absolute difference in the average number of chapters per book for authors "Dean Koontz" and "Charles Dickens"?

( ) group by `'author'`, aggregate with `.mean()`, use `get` on `'num_chapters'` column compute the absolute value of the difference between `iloc["Charles Dickens"]` and `iloc["Dean Koontz"]`
( ) do two queries to get two separate tables (one for each of "Dean Koontz" and "Charles Dickens"), use `get` on the `'num_chapters'` column of each table, use the Series method `.mean()` on each, compute the absolute value of the difference in these two means
( ) group by both `'author'` and `'title'`, aggregate with `.mean()`, use get on `'num_chapters'` column, use `loc` twice to find values in that column corresponding to "Dean Koontz" and "Charles Dickens", compute the absolute value of the difference in these two values
( ) query using a compound condition to get all books corresponding to "Dean Koontz" or "Charles Dickens", group by `'author'`, aggregate with `.mean()`, compute absolute value of the difference in `index[0]` and `index[1]`
# BEGIN SOLUTION

**Answer: ** do two queries to get two separate tables (one for each of "Dean Koontz" and "Charles Dickens"), use `get` on the `'num_chapters'` column of each table, use the Series method `.mean()` on each, compute the absolute value of the difference in these two means

Logically, we want to somehow separate data for author "Dean Koontz" and "Charles Dickens". (If we don't we'll be taking a mean that includes the chapters of books from both authors.) To achieve this separation, we can create two separate tables with a query that specifies a value on the `'author'` column. Now having two separate
tables, we can aggregate on the `'num_chapters'` (the column of interest). To get the `'num_chapters'` column we can use
the `get` method. To actually acquire the mean of the `'num_chapters'` column we can evoke the `.mean()` call.
<average>80</average>
# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Which of the following will produce the same value as the total number of books in the table?

( ) `books.groupby('Title').count().shape[0]`
( ) `books.groupby('Author').count().shape[0]`
( ) `books.groupby(['Author, 'Title']).count().shape[0]`
# BEGIN SOLUTION

**Answer: ** `books.groupby(['Author, 'Title']).count().shape[0]`

The key in this question is to understand that different authors can create books with the same name. The first two options
check for each unique book title (the first response) and check for each unique other (the second response). To ensure we
have all unique author and title pairs we must group based on both `'Author'` and `'Title'`. To actually get the number of rows
we can take `.shape[0]`.
<average>56</average>
# END SOLUTION

# END SUBPROB

# END PROB
