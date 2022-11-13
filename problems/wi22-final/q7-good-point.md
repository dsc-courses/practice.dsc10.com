# BEGIN PROB

Let's switch our attention to the relationship between the number of points per game and the number of assists per game for all players in `season`. Using `season`, we compute the following information:

- The mean points per game is 7, with a standard deviation of 5
- The mean number of assists per game is 1.5, with a standard deviation of 1.5
- The correlation between points per game and assists per game is 0.65

# BEGIN SUBPROB

Let's start by using points per game ($x$) to predict assists per game ($y$).

Tina Charles had 27 points per game in 2021, the most of any player in the WNBA. What is her predicted assists per game, according to the regression line? Round your answer to 3 decimal places.

# BEGIN SOLN

**Answer:** 5.4

We need to find and use the regression line to find the predicted $y$ for an $x$ of 27. There are two ways to proceed:

1. Use the regression line in standard units. To do this, we'd need to convert 27 from original units to standard units, use the regression line $y_\text{su} = r \cdot x_\text{su}$, and convert the output back to original units.
2. Use the regression line in original units. To do this, we'd need to find the slope $m$ and intercept $b$ in the regression line $y = mx + b$, using the formulas $m = r \cdot \frac{\text{SD of }y }{\text{SD of }x}$ and $b = \text{mean of }y - m \cdot \text{mean of }x$.

Both solutions work; for the sake of completeness, we'll show both. Recall, $r$ is the correlation coefficient between $x$ and $y$, which we are told is 0.65. 

**Solution 1:**

First, we need to convert 27 points per game to standard units. Doing so yields

$$x_{\text{su}} = \frac{x - \text{mean of }x}{\text{SD of }x} = \frac{27 - 7}{5} = 4$$

Per the regression line, $y_\text{su} = r \cdot x_\text{su}$, we have $y_\text{su} = 0.65 \cdot 4 = 2.6$, which is Tina Charles' predicted assists per game in standard units. All that's left is to convert this value back to original units:

$$\begin{aligned} y_{\text{su}} &= \frac{y - \text{mean of }y}{\text{SD of }y} \\ 2.6 &= \frac{y - 1.5}{1.5} \\ 2.6 \cdot 1.5 + 1.5 &= y \\ y &= \boxed{5.4} \end{aligned}$$

So, the regression line predicts Tina Charles will have 5.4 assists per game (in original units).

<br>

**Solution 2:**

First, we need to find the slope $m$ and intercept $b$:

$$m = r \cdot \frac{\text{SD of }y }{\text{SD of }x} = 0.65 \cdot \frac{1.5}{5} = 0.195$$

$$b = \text{mean of }y - m \cdot \text{mean of }x = 1.5 - 0.195 \cdot 7 = 0.135$$

Then,

$$y = mx + b \implies y = 0.195 \cdot 27 + 0.135 = \boxed{5.4}$$

So, once again, the regression line predicts Tina Charles will have 5.4 assists per game.

**Note:** The numbers in this problem may seem ugly, but students taking this exam had access to calculators since this exam was online. It also turns out that the numbers were easier to work with in Solution 1 over Solution 2; this was intentional.

<average>81</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Tina Charles actually had 2.1 assists per game in the 2021 season.

What is the error, or residual, for the prediction in the previous subpart? Round your answer to 3 decimal places.

# BEGIN SOLN

**Answer:** -3.3

Residuals are defined as follows:

$$\text{residual} = \text{actual } y - \text{predicted }y$$

$2.1 - 5.4 = -3.3$, which gives us our answer.

**Note:** Many students answered 3.3. Pay attention to the order of the calculation!

<average>82</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Select all true statements below regarding the regression line between points per game ($x$) and assists per game ($y$).

[ ] The point (0, 0) is guaranteed to be on the regression line when both $x$ and $y$ are in standard units.
[ ] The point (0, 0) is guaranteed to be on the regression line  when both $x$ and $y$ are in original units.
[ ] The point (7, 1.5) is guaranteed to be on the regression line when both $x$ and $y$ are in standard units.
[ ] The point (7, 1.5) is guaranteed to be on the regression line when both $x$ and $y$ are in original units.
[ ] None of the above

# BEGIN SOLN

**Answers:**

- The point (0, 0) is guaranteed to be on the regression line when both $x$ and $y$ are in standard units (Option 1).
- The point (7, 1.5) is guaranteed to be on the regression line when both $x$ and $y$ are in original units (Option 4).

The main idea being assessed here is the fact that the point $(\text{mean of }x, \text{mean of }y)$ always lies on the regression line. Indeed, in original units, 7 is the average $x$ (PPG) and 1.5 is the average $y$ (APG); this information was provided to us at the start of the problem. The nuance behind this problem lies in the units that are being used in the regression line.

When the regression line is in **standard units**:

- In standard units, 0 means "0 standard deviations above the average", i.e. 0 means "average". When the regression line is in standard units, we have $y_\text{su} = r \cdot x_\text{su}$. If $x$ is average, i.e. if $x_\text{su} = 0$, then $y_\text{su} = r \cdot x_\text{su} = r \cdot 0 = 0$, regardless of what $r$ is. So the point $(0, 0)$ is on the regression line when both $x$ and $y$ are in standard units, meaning that **Option 1 is correct**.
- The point $(7, 1.5)$ is not on the regression line when $x$ and $y$ are in standard units. We know this because in this problem $r = 0.65$, and if $x_\text{su} = 7$, then $y_\text{su} = r \cdot x_\text{su} = 0.65 \cdot 7 = 4.55 \neq 1.5$. This means that **Option 3 is incorrect**.

When the regression line is in **original units**:

- In original units, the average $x$ is 7 and the average $y$ is 1.5. From class, we may remember that this automatically means that $(7, 1.5)$ is on the regression line in original units. If we didn't remember that, we can look to the formula for the slope $m$ and intercept $b$ in $y = mx + b$. The formula for the slope is actually not relevant here; what's relevant is the fact that $b = \text{mean of }y - m \cdot \text{mean of }x$. Substituting the formula for $b$ into $y = mx + b$ yields

$$y = mx + b = mx + \text{mean of }y - m \cdot \text{mean of }x$$

- If $x = \text{mean of }x$, then the above simplifies to: $y = m \cdot \text{mean of }x + \text{mean of }y - m \cdot \text{mean of }x = \text{mean of }y$, meaning that $(\text{mean of }x, \text{mean of }y)$ — which is $(7, 1.5)$ in this case — is on the regression line in original units, so **Option 4 is correct**. 
- In the above equation, if $x = 0$, then $y = \text{mean of }y - m \cdot \text{mean of }x$, which in this case simplifies to $1.5 - 0.195 \cdot 7 = 0.135 \neq 0$. This means that (0, 0) is not on the regression line in original units and **Option 2 is incorrect**.

<average>87</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

So far, we've been using points per game ($x$) to predict assists per game ($y$). Suppose we found the regression line (when both $x$ and $y$ are in original units) to be $y = ax + b$.

Now, let's reverse $x$ and $y$. That is, we will now use assists per game ($x$) to predict points per game ($y$). The resulting regression line (when both $x$ and $y$ are in original units) is $y = cx + d$.

Which of the following statements is guaranteed to be true?

( ) $a = c$
( ) $a > c$
( ) $a < c$
( ) Using just the information given in this problem, it is impossible to determine the relationship between $a$ and $c$.

# BEGIN SOLN

**Answer:** $a < c$

The formula for the slope of the regression line is $m = r \cdot \frac{\text{SD of }y}{\text{SD of }x}$. Note that the correlation coefficient $r$ is symmetric, meaning that the correlation between $x$ and $y$ is the same as the correlation between $y$ and $x$.

In the two regression lines mentioned in this problem, we have

$$\begin{aligned} a &= r \cdot \frac{\text{SD of assists per game}}{\text{SD of points per game}} \\ c &= r \cdot \frac{\text{SD of points per game}}{\text{SD of assists per game}}  \end{aligned}$$

We're told in the problem that the SD of points per game is 5 and the SD of assists per game is 1.5. So, $a = r \cdot \frac{1.5}{5}$ and $c = r \cdot \frac{5}{1.5}$; since $\frac{1.5}{5} < \frac{5}{1.5}$, $a < c$.

<average>74</average>

# END SOLN

# END SUBPROB

# END PROB