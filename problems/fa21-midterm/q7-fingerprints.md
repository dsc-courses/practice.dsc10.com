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

solution here

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
(X) B
( ) C
( ) D

Which of the four options on the y-axis is closest to where the height of the right-most bar should be?

( ) A
( ) B
(X) C
( ) D

# BEGIN SOLUTION

**Answer: ** B, then C

solution here

# END SOLUTION

# END SUBPROB

# END PROB