# BEGIN PROB
Suppose the price of an IKEA product and the cost to have it assembled are linearly associated with a correlation of 0.8. Product prices have a mean of 140 dollars and a standard deviation of 40 dollars. Assembly costs have a mean of 80 dollars and a standard deviation of 10 dollars. We want to predict the assembly cost of a product based on its price using linear regression.

# BEGIN SUBPROB

The NORDMELA 4-drawer dresser sells for 200 dollars. How much do we predict its assembly cost to be?

# BEGIN SOLUTION

**Answer: ** 92 dollars

We first use the formulas for the slope, $m$, and intercept, $b$, of the regression line to find the equation. For our application, $x$ is the price and $y$ is the assembly cost since we want to predict the assembly cost based on price.

$$\begin{aligned} 
        m &= r*\frac{\text{SD of }y}{\text{SD of }x} \\
                     &= 0.8*\frac{10}{40} \\
                     &= 0.2\\
        b &= \text{mean of }y - m*\text{mean of }x  \\
                     &= 80 - 0.2*140 \\
                     &= 80 - 28 \\
                     &= 52
\end{aligned}$$

Now we know the formula of the regression line and we simply plug in $x=200$ to find the associated $y$ value.

$$\begin{aligned} 
        y &= mx+b \\
        y &= 0.2x+52 \\
         &= 0.2*200+52 \\
         &= 92
\end{aligned}$$

<average>76</average>
# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

The IDANÄS wardrobe sells for 80 dollars more than the KLIPPAN loveseat, so we expect the IDANÄS wardrobe will have a greater assembly cost than the KLIPPAN loveseat. How much do we predict the difference in assembly costs to be?

# BEGIN SOLUTION

**Answer: ** 16 dollars

The slope of a line describes the change in $y$ for each change of 1 in $x$. The difference in $x$ values for these two products is 80, so the difference in $y$ values is $m*80 = 0.2*80 = 16$ dollars.

An equivalent way to state this is:

$$\begin{aligned} 
        m &= \frac{\text{ rise, or change in } y}{\text{ run, or change in } x} \\
        0.2 &= \frac{\text{ rise, or change in } y}{80} \\
        0.2*80 &= \text{ rise, or change in } y \\
	16 &= \text{ rise, or change in } y 
\end{aligned}$$

<average>65</average>
# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

If we create a 95% prediction interval for the assembly cost of a 100 dollar product and another 95% prediction interval for the assembly cost of a 120 dollar product, which prediction interval will be wider?

( ) The one for the 100 dollar product.
( ) The one for the 120 dollar product.

# BEGIN SOLUTION

**Answer: ** The one for the 100 dollar product.

Prediction intervals get wider the further we get from the point $(\text{mean of } x, \text{mean of } y)$ since all regression lines must go through this point. Since the average product price is 140 dollars, the prediction interval will be wider for the 100 dollar product, since it's the further of 100 and 120 from 140.
<average>45</average>
# END SOLUTION

# END SUBPROB

# END PROB