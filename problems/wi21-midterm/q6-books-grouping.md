# BEGIN PROB

You are given a DataFrame called `books` that contains columns `'author'` (string), `'title'` (string), `'num_chapters'` (int), and `'publication_year'` (int).

Suppose that after doing `books.groupby('Author').max()`, one row says

| author               | title       |  num_chapters | publication_year |    
| -----------          | ----------- | -----------   | -----------      |
| Charles Dickens      | Oliver Twist| 53            | 1838             |

# BEGIN SUBPROB

Based on this data, can you conclude that Charles Dickens is the alphabetically last of all author names in this dataset?

( ) Yes
( ) No

# BEGIN SOLUTION

**Answer: ** No

When we group by `'Author'`, all books by the same author get aggregated together into a single row. The aggregation function is applied separately to each other column besides the column we're grouping by. Since we're grouping by `'Author'` here, the `'Author'` column never has the `max()` function applied to it. Instead, each unique value in the `'Author'` column becomes a value in the index of the grouped DataFrame. We are told that the Charles Dickens row is just one row of the output, but we don't know anything about the other rows of the output, or the other authors. We can't say anything about where Charles Dickens falls when authors are ordered alphabetically (but it's probably not last!)

<average>94</average>
# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Based on this data, can you conclude that Charles Dickens wrote *Oliver Twist*?

( ) Yes
( ) No

# BEGIN SOLUTION

**Answer: ** Yes

Grouping by  `'Author'` collapses all books written by the same author into a single row. Since we're applying the `max()` function to aggregate these books, we can conclude that *Oliver Twist* is alphabetically last among all books in the `books` DataFrame written by Charles Dickens. So Charles Dickens did write *Oliver Twist* based on this data.

<average>95</average>
# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Based on this data, can you conclude that *Oliver Twist* has 53 chapters?

( ) Yes
( ) No

# BEGIN SOLUTION

**Answer: ** No

The key to this problem is that `groupby` applies the aggregation function, `max()` in this case, independently to each column. The output should be interpreted as follows:

- Among all books in `books` written by Charles Dickens, *Oliver Twist* is the title that is alphabetically last.
- Among all books in `books` written by Charles Dickens, 53 is the greatest number of chapters.
- Among all books in `books` written by Charles Dickens, 1838 is the latest year of publication.

However, the book titled *Oliver Twist*, the book with 53 chapters, and the book published in 1838 are not necessarily all the same book. We cannot conclude, based on this data, that *Oliver Twist* has 53 chapters.

<average>74</average>
# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Based on this data, can you conclude that Charles Dickens wrote a book with 53 chapters that was published in 1838?

( ) Yes
( ) No

# BEGIN SOLUTION

**Answer: ** No

As explained in the previous question, the `max()` function is applied separately to each column, so the book written by Charles Dickens with 53 chapters may not be the same book as the book written by Charles Dickens published in 1838.

<average>73</average>
# END SOLUTION

# END SUBPROB

# END PROB