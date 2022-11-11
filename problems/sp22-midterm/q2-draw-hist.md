# BEGIN PROB

On the graph paper below, draw the histogram that would be produced by this code.

```py
(
sungod.take(np.arange(5))
      .plot(kind='hist', density=True, 
      bins=np.arange(0, 7, 2), y='Appearance_Order');
)
```

In your drawing, make sure to label the height of each bar in the histogram on the vertical axis. You can scale the axes however you like, and the two axes don't need to be on the same scale.

<center><img src='../assets/images/sp22-midterm/graph-paper.png' width=250></center>

# BEGIN SOLUTION

**Answer: ** 

<center><img src='../assets/images/sp22-midterm/graph-paper-soln.png' width=330></center>

To draw the histogram, we first need to bin the data and figure out how many data values fall into each bin. The code includes `bins=np.arange(0, 7, 2)` which means the bin endpoints are $0, 2, 4, 6$. This gives us three bins: $[0, 2)$, $[2, 4)$, and $[4, 6]$. Remember that all bins, except for the last one, include the left endpoint but not the right. The last bin includes both endpoints. 

Now that we know what the bins are, we can count up the number of values in each bin. We need to look at the `'Appearance_Order'` column of `sungod.take(np.arange(5))`, or the first five rows of `sungod`. The values there are $1, 4, 3, 1, 3$. The two $1$s fall into the first bin $[0, 2)$. The two $3$s fall into the second bin $[2, 4)$, and the one $4$ falls into the last bin $[4, 6]$. This means the proportion of values in each bin are $\frac{2}{5}, \frac{2}{5}, \frac{1}{5}$ from left to right.

To figure out the height of each bar in the histogram, we use the fact that the area of a bar in a density histogram should equal the proportion of values in that bin. The area of a rectangle is height times width, so height is area divided by width. 

For the bin $[0, 2)$, the area is $\frac{2}{5} = 0.4$ and the width is $2$, so the height is $\frac{0.4}{2} = 0.2$.

For the bin $[2, 4)$, the area is $\frac{2}{5} = 0.4$ and the width is $2$, so the height is $\frac{0.4}{2} = 0.2$. 

For the bin $[4, 6]$, the area is $\frac{1}{5} = 0.2$ and the width is $2$, so the height is $\frac{0.2}{2} = 0.1$. 

Since the bins are all the same width, the fact that there an equal number of values in the first two bins and half as many in the third bin means the first two bars should be equally tall and the third should be half as tall. We can use this to draw the rest of the histogram quickly once we've drawn the first bar.

<average>45</average>

# END SOLUTION

# END PROB
