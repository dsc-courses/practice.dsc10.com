# BEGIN PROB

Recall, the interval $[a, b)$ refers to numbers greater than or equal to $a$ and less than $b$, and the interval $[a, b]$ refers to numbers greater than or equal to $a$ and less than or equal to $b$.

Suppose we created a DataFrame, `medium_sky`, containing only the skyscrapers in `sky` whose number of floors are in the interval $[20, 60]$. Below, we've drawn a histogram of the number of floors of all skyscrapers in `medium_sky`.

<center><img src='../assets/images/wi22-midterm/floors-hist.png' width=40%></center>

# BEGIN SUBPROB

Suppose that there are 160 skyscrapers whose number of floors are in the interval $[30, 35)$.

Given this information and the histogram above, how many skyscrapers are there in `medium_sky`?

# BEGIN SOLN

**Answer:** 800

Recall, in a histogram,

$$\text{proportion of values in bin} = \text{area of bar} = \text{width of bin} \cdot \text{height of bar}$$

Also, note that:

$$\text{\# of values satisfying condition} = \text{proportion of values satisfying condition} \cdot \text{total \# of values}$$

Here, we're given the entire histogram, so we can find the proportion of values in the $[30, 35)$ bin. We are also given the number of values in the $[30, 35)$ bin (160). This means we can use the second equation above to find the total number of skyscrapers in `medium_sky`.

The first step is finding the area of the $[30, 35)$ bin's bar. Its width is $35-30 = 5$, and its height is $0.04$, so its area is $5 \cdot 0.04 = 0.2$. Then,

$$\begin{aligned} 
        \text{\# of values satisfying condition} &= \text{proportion of values satisfying condition} \cdot \text{total \# of values} \\ 
        160 &= 0.2 \cdot \text{total \# of values} \\ 
        \implies \text{total \# of values} &= \frac{160}{0.2} = 160 \cdot 5 = 800 
\end{aligned}$$

<average>62</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Again, suppose that there are 160 skyscrapers whose number of floors are in the interval $[30, 35)$.

Now suppose that there is a typo in the `medium_sky` DataFrame, and 20 skyscrapers were accidentally listed as having 53 floors each when instead they actually only have 35 floors each. The histogram drawn above contains the incorrect version of the data.

Suppose we re-draw the above histogram using the correct data. What will be the new heights of both the $[35, 40)$ bar and $[50, 55)$ bar? Select the closest answer.

( ) The $[35, 40)$ bar's height becomes 0.0325, and the $[50, 55)$ bar's height becomes 0.0105.
( ) The $[35, 40)$ bar's height becomes 0.035, and the $[50, 55)$ bar's height becomes 0.008.
( ) The $[35, 40)$ bar's height becomes 0.0375, and the $[50, 55)$ bar's height becomes 0.0055.
( ) The $[35, 40)$ bar's height becomes 0.04, and the $[50, 55)$ bar's height becomes 0.003.

# BEGIN SOLN

**Answer:** The $[35, 40)$ bar's height becomes 0.035, and the $[50, 55)$ bar's height becomes 0.008.

The current height of the $[35, 40)$ bar is 0.03, and the current height of the $[50, 55)$ bar is 0.013 (approximately; its height appears to be slightly more than halfway between 0.01 and 0.015). We need to decrease the height of the $[50, 55)$ bar and increase the height of the $[35, 40)$ bar. The combined area of both bars must stay the same, since the proportion of values in their bins (together) is not changing. This means that the amount we need to decrease the $[50, 55)$ bar's height by is the same as the amount we need to increase the $[35, 40)$ bar's height by. Note that this relationship is true in all 4 answer choices.

In the question, we were told that 20 skyscrapers were incorrectly binned. There are 800 skyscrapers total, so the proportion of skyscrapers that were incorrectly binned is $\frac{20}{800} = 0.025$. This means that the area of the $[35, 40)$ bar needs to increase by 0.025 and the area of the $[50, 55)$ bar needs to decrease by 0.025. Recall, each bar has width 5. That means that the "rectangular section" we will add to the $[35, 40)$ bar and remove from the $[50, 55)$ bar has height

$$\text{height} = \frac{\text{area}}{\text{width}} = \frac{0.025}{5} = 0.005$$

Thus, the height of the $[35, 40)$ bar becomes $0.03 + 0.005 = 0.035$ and the height of the $[50, 55)$ bar becomes $0.013 - 0.005 = 0.008$.

<average>74</average>

# END SOLN

# END SUBPROB

# END PROB