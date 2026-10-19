---
lecture: 22
---

# BEGIN PROB
Answer the following true/false questions.

# BEGIN SUBPROB

`df.groupby("kind").mean()` will have 5 columns.

( ) True
( ) False

# BEGIN SOLUTION

**Answer: ** False

`df` has five numeric columns, but it also has the string column `'size'`. Grouping by `'kind'` moves `'kind'` into the index and leaves `'size'` in the table. `.mean()` tries to average every remaining column, including `'size'`, and raises an error. It does not return a DataFrame with 5 columns.

<average>74</average>

# END SOLUTION

# END SUBPROB

# END PROB
