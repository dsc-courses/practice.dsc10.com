# BEGIN PROB

Raine is helping settle a debate between two friends on the "superior\"
season --- winter or summer. In doing so, they try to understand the
relationship between the number of sunshine hours per month in January
and the number of sunshine hours per month in July across all cities in
California in `sun`.

Raine finds the regression line that predicts the number of sunshine
hours in July ($y$) for a city given its number of sunshine hours in
January ($x$). In doing so, they find that the correlation between the
two variables is $\frac{2}{5}$.

# BEGIN SUBPROB

Which of these could be a scatter plot of number of sunshine
hours in July vs. number of sunshine hours in January?

<center><img src='../assets/images/sp23-final/r-values.png' width=550></center>

( ) Option 1 
( ) Option 2
( ) Option 3 
( ) Option 4

# BEGIN SOLUTION

**Answer**: Option 1

Since $r = \frac{2}{5}$, the correct option must be a scatter plot with a mild positive (up and to the right) linear association. Option 3 can be ruled out immediately, since the linear association in it is negative (down and to the right). Option 2's linear association is too strong for $r = \frac{2}{5}$, and Option 4's linear association is too weak for $r = \frac{2}{5}$, which leaves Option 1.

<average>57</average>

# END SOLUTION

# END SUBPROB


# BEGIN SUBPROB

Suppose the standard deviation of the number of sunshine hours in
January for cities in California is equal to the standard deviation of
the number of sunshine hours in July for cities in California.

Raine's hometown of Santa Clarita saw 60 more sunshine hours in January
than the average California city did. How many **more sunshine hours
than average** does the regression line predict that Santa Clarita will
have in July? Give your answer as a positive integer. *(Hint: You'll
need to use the fact that the correlation between the two variables is
$\frac{2}{5}$.)*

# BEGIN SOLUTION

**Answer**: 24

At a high level, we'll start with the formula for the regression line in standard units, and re-write it in a form that will allow us to use the information provided to us in the question.

Recall, the regression line in standard units is

$$\text{predicted }y_{\text{(su)}} = r \cdot x_{\text{(su)}}$$

Using the definitions of $\text{predicted }y_{\text{(su)}}$ and $x_{\text{(su)}}$ gives us

$$\frac{\text{predicted } y - \text{mean of }y}{\text{SD of }y} = r \cdot \frac{x - \text{mean of }x}{\text{SD of }x}$$

Here, the $x$ variable is sunshine hours in January and the $y$ variable is sunshine hours in July. Given that the standard deviation of January and July sunshine hours are equal, we can simplifies our formula to

$$\text{predicted } y - \text{mean of }y = r \cdot (x - \text{mean of }x)$$

Since we're asked how much more sunshine Santa Clarita will have in July compared to the average, we're interested in the difference $y - \text{mean of} y$. We were given that Santa Clarita had 60 more sunshine hours in January than the average, and that the correlation between the two variables(correlation coefficient) is $\frac{2}{5}$. In terms of the variables above, then, we know:

- $x - \text{mean of }x = 60$.

- $r = \frac{2}{5}$.

Then,

$$\text{predicted } y - \text{mean of }y = r \cdot (x - \text{mean of }x) = \frac{2}{5} \cdot 60 = 24$$

Therefore, the regression line predicts that Santa Clarita will have 24 more sunshine hours than the average California city in July.

<average>68</average>

# END SOLUTION

# END SUBPROB

As we know, San Diego was particularly cloudy this May. More generally, Anthony, another California native, feels that California is getting cloudier and cloudier overall.

To imagine what the dataset may look like in a few years, Anthony subtracts 5 from the number of sunshine hours in both January and July for all California cities in the dataset – i.e., he subtracts 5 from each $x$ value and 5 from each $y$ value in the dataset. He then creates a regression line to use the new $xs$ to predict the new $ys$.


# BEGIN SUBPROB

What is the slope of Anthony's new regression line?

# BEGIN SOLUTION

**Answer**: $\frac{2}{5}$

To determine the slope of Anthony's new regression line, we need to understand how the modifications he made to the dataset (subtracting 5 hours from each x and y value) affect the slope. In simple linear regression, the slope of the regression line ($m$ in $y = mx + b$) is calculated using the formula:

$$m = r \cdot \frac{\text{SD of y}}{\text{SD of x}}$$

$r$, the correlation coefficient between the two variables, remains unchanged in Anthony's modifications. Remember, the correlation coefficient is the mean of the product of the $x$ values and $y$ values when both are measured in standard units; by subtracting the same constant amount from each $x$ value, we aren't changing what the $x$ values convert to in standard units. If you're not convinced, convert the following two arrays in Python to standard units; you'll see that the results are the same.

```py
x1 = np.array([5, 8, 4, 2, 9])
x2 = x1 - 5
```

Furthermore, Anthony's modifications also don't change the standard deviations of the $x$ values or $y$ values, since the $x$s and $y$s aren't any more or less spread out after being shifted "down" by 5. So, since $r$, $\text{SD of }y$, and $\text{SD of }x$ are all unchanged, the slope of the new regression line is the same as the slope of the old regression line, pre-modification!

Given the fact that the correlation coefficient is $\frac{2}{5}$ and the standard deviation of sunshine hours in January ($\text{SD of }x$) is equal to the standard deviation of sunshine hours in July ($\text{SD of }y$), we have

$$m = r \cdot \frac{\text{SD of }y}{\text{SD of }x} = \frac{2}{5} \cdot 1 = \frac{2}{5}$$

<average>73</average>

# END SOLUTION

# END SUBPROB


# BEGIN SUBPROB

Suppose the intercept of Raine's original regression line – that is,
before Anthony subtracted 5 from each $x$ and each $y$ – was 10. What
is the intercept of Anthony's new regression line?

( ) -7 
( ) -5 
( ) -3 
( ) 0 
( ) 3 
( ) 5 
( ) 7

# BEGIN SOLUTION

**Answer**: 7

Let's denote the original intercept as $b$ and the new intercept in the new dataset as $b'$. The equation for the original regression line is $y = mx + b$, where:

- $y$ is a predicted number of sunshine hours in July, before 5 was subtracted from each number of hours.
- $m$ is the slope of the line, which we know is $\frac{2}{5}$ from the previous part.
- $x$ is a number of sunshine hours in January, before 5 was subtracted from each number of hours.
- $b$ is the original intercept. This is 10.

When Anthony subtracts 5 from each $x$ and $y$ value, the new regression line becomes $$y - 5 = m \cdot (x - 5) + b'$$

Expanding and rearrange this equation, we have

$$y = mx - 5m + 5 + b'$$

Remember, $x$ and $y$ here represent the number of sunshine hours in January and July, respectively, _before_ Anthony subtracted 5 from each number of hours. This means that the equation for $y$ above is equivalent to $y = mx + b$. Comparing, we see that

$$-5m + 5 + b' = b$$

Since $m = \frac{2}{5}$ (from the previous part) and $b = 10$, we have

$$-5 \cdot \frac{2}{5} + 5 + b' = 10 \implies b' = 10 - 5 + 2 = 7$$

Therefore, the intercept of Anthony's new regression line is 7.

<average>34</average>

# END SOLUTION

# END SUBPROB

Jasmine is trying to get as far away from Anthony as possible and has a
trip to Chicago planned after finals. Chicago is known for being very
warm and sunny in the summer but cold, rainy, and snowy in the winter.
She decides to build a regression line that uses month of the year
(where 1 is January, 2 is February, 12 is December, etc.) to predict the
number of sunshine hours in Chicago.

# END PROB