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

# END PROB
