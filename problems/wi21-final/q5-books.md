# BEGIN PROBLEM

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

Some explanation

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

Some explanation

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Which of the following will produce the same value as the total number of books in the table?

( ) `books.groupby('Title').count().shape[0]`
( ) `books.groupby('Author').count().shape[0]`
( ) `books.groupby(['Author, 'Title']).count().shape[0]`
# BEGIN SOLUTION

**Answer: ** ( ) `books.groupby(['Author, 'Title']).count().shape[0]`

Some explanation

# END SOLUTION

# END SUBPROB

# END PROB