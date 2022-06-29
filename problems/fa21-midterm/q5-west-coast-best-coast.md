# BEGIN PROB

Suppose we create a DataFrame called `socal` containing only King Triton's flights departing from SAN, LAX, or SNA (John Wayne Airport in Orange County). `socal` has 10 rows; the bar chart below shows how many of these 10 flights departed from each airport.

<center><img src='../assets/images/fa21-midterm/socal.png' width=30%></center>

Consider the DataFrame that results from merging `socal` with itself, as follows:

```py
double_merge = socal.merge(socal, left_on='FROM', right_on='FROM')
```

How many rows does `double_merge` have?

# BEGIN SOLUTION

**Answer: ** 38

solution here

# END SOLUTION

# END PROB