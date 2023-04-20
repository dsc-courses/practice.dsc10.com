# BEGIN PROB

Suppose we create a DataFrame called `socal` containing only King Triton's flights departing from SAN, LAX, or SNA (John Wayne Airport in Orange County). `socal` has 10 rows; the bar chart below shows how many of these 10 flights departed from each airport.

<center><img src='../assets/images/fa21-midterm/socal.png' width=30%></center>
<br>

Consider the DataFrame that results from merging `socal` with itself, as follows:

```py
double_merge = socal.merge(socal, left_on='FROM', right_on='FROM')
```

How many rows does `double_merge` have?

# BEGIN SOLUTION

**Answer: ** 38

There are two flights from LAX. When we merge `socal` with itself on the `'FROM'` column, each of these flights gets paired up with each of these flights, for a total of four rows in the output. That is, the first flight from LAX gets paired with both the first and second flights from LAX. Similarly, the second flight from LAX gets paired with both the first and second flights from LAX.

Following this logic, each of the five flights from SAN gets paired with each of the five flights from SAN, for an additional 25 rows in the output. For SNA, there will be 9 rows in the output. The total is therefore $2^2 + 5^2 + 3^2 = 4 + 25 + 9 = 38$ rows.

<average>27</average>

# END SOLUTION

# END PROB