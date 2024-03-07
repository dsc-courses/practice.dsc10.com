# BEGIN PROB

We use the regression line to predict a game’s `"Rating"` based on its `"Complexity"`. We find that for the game *Wingspan*, which has a `"Complexity"` that is 2 points higher than the average, the predicted `"Rating"` is 3 points higher than the average.

# BEGIN SUBPROB
What can you conclude about the correlation coefficient r?

( ) $r < 0$
( ) $r = 0$
( ) $r > 0$
( ) We cannot make any conclusions about the value of $r$ based on this information alone.

# BEGIN SOLUTION

**Answer:** $r > 0$

To answer this problem, it's useful to recall the regression line in standard units:

$$\text{predicted } y_{\text{(su)}} = r \cdot x_{\text{(su)}}$$

If a value is positive in standard units, it means that it is above the average of the distribution that it came from, and if a value is negative in standard units, it means that it is below the average of the distribution that it came from. Since we're told that *Wingspan* has a `"Complexity"` that is 2 points higher than the average, we know that $x_{\text{(su)}}$ is positive. Since we're told that the predicted `"Rating"` is 3 points higher than the average, we know that $\text{predicted } y_{\text{(su)}}$ must also be positive. As a result, $r$ must also be positive, since you can't multiply a positive number ($x_{\text{(su)}}$) by a negative number and end up with another positive number.

<average>74</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB
What can you conclude about the standard deviations of "Complexity" and "Rating"?

( ) SD of `"Complexity"` < SD of `"Rating"`
( ) SD of `"Complexity"` = SD of `"Rating"`
( ) SD of `"Complexity"` > SD of `"Rating"`
( ) We cannot make any conclusions about the relationship between these two standard deviations based on this information alone.

# BEGIN SOLUTION

**Answer:** SD of `"Complexity"` < SD of `"Rating"`

Since the distance of the predicted `"Rating"` from its average is larger than the distance of the `"Complexity"` from its average, it might be reasonable to guess that the values in the `"Rating"` column are more spread out. This is true, but let's see concretely why that's the case.

Let's start with the equation of the regression line in standard units from the previous subpart. Remember that here, $x$ refers to `"Complexity"` and $y$ refers to `"Rating"`.

$$\text{predicted } y_{\text{(su)}} = r \cdot x_{\text{(su)}}$$

We know that to convert a value to standard units, we subtract the value by the mean of the column it came from, and divide by the standard deviation of the column it came from. As such, $x_{\text{(su)}} = \frac{x - \text{mean of } x}{\text{SD of } x}$. We can substitute this relationship in the regression line above, which gives us

$$\frac{\text{predicted } y - \text{mean of } y}{\text{SD of } y} = r \cdot \frac{x - \text{mean of } x}{\text{SD of } x}$$

To simplify things, let's use what we were told. We were told that the predicted `"Rating"` was 3 points higher than average. This means that the numerator of the left side, $\text{predicted } y - \text{mean of } y$, is equal to 3. Similarly, we were told that the `"Complexity"` was 2 points higher than average, so $x - \text{mean of } x$ is 2. Then, we have:

$$\frac{3}{\text{SD of } y} = \frac{2r}{\text{SD of }x}$$

Note that for convenience, we included $r$ in the numerator on the right-hand side.

Remember that our goal is to compare the SD of `"Rating"` ($y$) to the SD of `"Complexity"` ($x$). We now have an equation that relates these two quantities! Since they're both currently on the denominator, which can be tricky to work with, let's take the reciprocal (i.e. "flip") both fractions.

$$\frac{\text{SD of } y}{3} = \frac{\text{SD of }x}{2r}$$

Now, re-arranging gives us

$$\text{SD of } y \cdot \frac{2r}{3} = \text{SD of }x$$

Since we know that $r$ is somewhere between 0 and 1, we know that $\frac{2r}{3}$ is somewhere between 0 and $\frac{2}{3}$. This means that $\text{SD of } x$ is somewhere between 0 and two-thirds of the value of $\text{SD of } y$, which means that no matter what, $\text{SD of } x < \text{SD of } y$. Remembering again that here `"Complexity"` is our $x$ and `"Rating"` is our $y$, we have that the SD of `"Complexity"` is less than the SD of `"Rating"`.

<average>42</average>

# END SOLUTION

# END SUBPROB

# END PROB
