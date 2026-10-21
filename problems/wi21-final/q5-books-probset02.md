---
lecture: 9
---

# BEGIN PROB

You are given a table called books that contains columns `'author'` (`str`), `'title'` (`str`), `'num_chapters'` (`int`), and `'publication_year'` (`int`).
# BEGIN SUBPROB

What will be the output of the following code?
`books.get(['publication_year', 'num_chapters']).groupby('publication_year').mean().shape[1]`

( ) `1`
( ) `2`
( ) `3`
( ) `4`

# BEGIN SOLUTION

**Answer: ** `1`

The output will return 1. `.shape[1]` is the number of columns in the result. `.get(['publication_year', 'num_chapters'])` keeps the grouping column and `'num_chapters'`. `'author'` and `'title'` are strings, so they are left out and `.mean()` can run. Grouping by `'publication_year'` moves that column to the index, leaving `'num_chapters'` as the only column. 

<average>67</average>

# END SOLUTION

# END SUBPROB

# END PROB
