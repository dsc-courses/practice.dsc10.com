<!-- <topics>arithmetic</topics> -->

# BEGIN PROB

You are working in a spreadsheet editor and you highlight several consecutive rows of your spreasheet. The first highlighted row is row 543 and the last highlighted row is row 897. How many rows are highlighted?

In general, if rows $n$ through $m$ are highlighted, with $n<m$, how many rows is that?

Solve this problem without a calculator.

# BEGIN SOLUTION

**Answer**: 355, or more generally, $m-n+1$

It might help to visualize the problem, as in the image below.

<center><img src='../assets/images/pretest/spreadsheet.jpg' width=40%></center>

One way to solve this problem is to count the rows and look for a pattern. Row 543 is row 1 of the highlighted section. Row 544 is row 2 of the highlighted section. Row 545 is row 3 of the highlighted section. The pattern seems to be that row $x$ is row $x$ - 542 of the highlighted section. Therefore, with $x$ = 897, row 897 is row 355 of the highlighted section. Since this is the last row of the highlighted section, there are 355 rows highlighted.

Let's also think about the problem a different way. Imagine we had highlighted all the rows up to and including row 897. That would mean we had highlighted 897 rows. But we actually highlighted 542 fewer rows than this (since the first highlighted row was row 543, the first 542 rows were not highlighted). So the total number of highlighted rows is 897 - 542 = 355.

In general, imagine highlighting all $m$ rows up to an including row $m$. That would be $m$ highlighted rows. But if we only start highlighting at row $n$, this includes $n-1$ rows that should not be counted. So there are $m-(n-1) = m - n + 1$ rows highlighted when we highlight rows $n$ through $m$.

# END SOLUTION

# END PROB