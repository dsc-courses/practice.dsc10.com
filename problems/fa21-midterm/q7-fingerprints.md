# BEGIN PROB

The seat-back TV on one of King Triton's more recent flights was very dirty and was full of fingerprints. The fingerprints made an interesting pattern. We've stored the x and y positions of each fingerprint in the DataFrame `fingerprints`, and created the following scatterplot using

```py
fingerprints.plot(kind='scatter', x='x', y='y')
```

<center><img src='../assets/images/fa21-midterm/mt-hist.png' width=20%></center>


# BEGIN SUBPROB

True or False: The histograms that result from the following two lines of code will look very similar.

```py
fingerprints.plot(kind='hist', 
                  y='x',
                  density=True,
                  bins=np.arange(0, 8, 2))
```
and 

```py
fingerprints.plot(kind='hist', 
                  y='y',
                  density=True,
                  bins=np.arange(0, 8, 2))
```

( ) True
( ) False

# BEGIN SOLUTION

**Answer: ** True

The only difference between the two code snippets is the data values used. The first creates a histogram of the `x`-values in `fingerprints`, and the second creates a histogram of the `y`-values in `fingerprints`. 

Both histograms use the same bins: `bins=np.arange(0, 8, 2)`. This means the bin endpoints are `[0, 2, 4, 6]`, so there are three distinct bins: $[0, 2)$, $[2, 4)$, and $[4, 6]$. Remember the right-most bin of a histogram includes both endpoints, whereas others include the left endpoint only.

Let's look at the `x`-values first. If we divide the scatterplot into nine equally-sized regions, as shown below, note that eight of the nine regions have a very similar number of data points. 

<center><img src='../assets/images/fa21-midterm/regions.png' width=20%></center>

Aside from the middle region, about $\frac{1}{8}$ of the data falls in each region. That means $\frac{3}{8}$ of the data has an `x`-value in the first bin $[0, 2)$, $\frac{2}{8}$ of the data has an `x`-value in the middle bin $[2, 4)$, and $\frac{3}{8}$ of the data has an `x`-value in the rightmost bin $[4, 6]$. This distribution of `x`-values into bins determines what the histogram will look like.

Now, if we look at the `y`-values, we'll find that $\frac{3}{8}$ of the data has a `y`-value in the first bin $[0, 2)$, $\frac{2}{8}$ of the data has a `y`-value in the middle bin $[2, 4)$, and $\frac{3}{8}$ of the data has a `y`-value in the last bin $[4, 6]$. That's the same distribution of data into bins as the `x`-values had, so the histogram of `y`-values will look just like the histogram of `y`-values.

Alternatively, an easy way to see this is to use the fact that the scatterplot is symmetric over the line $y=x$, the line that makes a 45 degree angle with the origin. In other words, interchanging the `x` and `y` values doesn't change the scatterplot noticeably, so the `x` and `y` values have very similar distributions, and their histograms will be very similar as a result.

<average>88</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB
Below, we've drawn a histogram using the line of code

```py
fingerprints.plot(kind='hist', 
                  y='x',
                  density=True,
                  bins=np.arange(0, 8, 2))
```

However, our Jupyter Notebook was corrupted, and so the resulting histogram doesn't quite look right. While the height of the first bar is correct, the histogram doesn't contain the second or third bars, and the y-axis is replaced with letters.

<center><img src='../assets/images/fa21-midterm/mt-hist-2.png' width=30%></center>

Which of the four options on the y-axis is closest to where the height of the middle bar should be?

( ) A
( ) B
( ) C
( ) D

Which of the four options on the y-axis is closest to where the height of the rightmost bar should be?

( ) A
( ) B
( ) C
( ) D

# BEGIN SOLUTION

**Answer: ** B, then C

We've already determined that the first bin should contain $\frac{3}{8}$ of the values, the middle bin should contain  $\frac{2}{8}$ of the values, and the rightmost bin should contain  $\frac{3}{8}$ of the values. The middle bar of the histogram should therefore be two-thirds as tall as the first bin, and the rightmost bin should be equally as tall as the first bin. The only reasonable height for the middle bin is B, as it's closest to two-thirds of the height of the first bar. Similarly, the rightmost bar must be at height C, as it's the only one close to the height of the first bar.

<average>94</average>

# END SOLUTION

# END SUBPROB

# END PROB