# BEGIN PROB

Now let's study the relationship between a penguin's bill length (in millimeters) and mass (in grams). Suppose we're given that

* bill length and body mass have a correlation coefficient of 0.55
* the average bill length is 44 mm and the standard deviation of bill lengths is 6 mm
* as before, the average body mass is 4200 grams and the standard deviation of body mass is 840 grams

# BEGIN SUBPROB

Which of the four scatter plots below describe the relationship between bill length and body mass, based on the information provided in the question?

<center><img src='../assets/images/fa21-final/bills_scatter.png' width=40%></center>
<br>

( ) Option 1
( ) Option 2
( ) Option 3
( ) Option 4

# BEGIN SOLUTION

**Answer** Option 3

Given the correlation coefficient is 0.55, bill length and body mass has a moderate positive correlation. We eliminate Option 1 (strong correlation) and Option 4 (weak correlation). 

Given the average bill length is 44 mm, we expect our x-axis to have 44 at the middle, so we eliminate Option 2

<average>91</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Suppose we want to find the regression line that uses bill length, $x$, to predict body mass, $y$. The line is of the form $y = mx +\ b$. What are $m$ and $b$?

What is $m$? Give your answer as a number without any units, rounded to three decimal places.

What is $b$? Give your answer as a number without units, rounded to three decimal places. 

# BEGIN SOLUTION

**Answer:** $m = 77$, $b = 812$

$$m = r \cdot \frac{\text{SD of }y }{\text{SD of }x} = 0.55 \cdot \frac{840}{6} = 77$$
$$b = \text{mean of }y - m \cdot \text{mean of }x = 4200-77 \cdot 44 = 812 $$

<average>92</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

What is the predicted body mass (in grams) of a penguin whose bill length is 44 mm? Give your answer as a number without any units, rounded to three decimal places.

# BEGIN SOLUTION

**Answer:** 4200

$$y = mx\ +\ b = 77 \cdot 44 + 812 = 3388 +812 = 4200$$

<average>95</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

A particular penguin had a predicted body mass of 6800 grams. What is that penguin's bill length (in mm)? Give your answer as a number without any units, rounded to three decimal places. 

# BEGIN SOLUTION

**Answer:** 77.766

In this question, we want to compute x value given y value
$$y = mx\ +\ b$$
$$y - b = mx$$
$$\frac{y - b}{m} = x\ \ \text{(m is nonzero)}$$
$$x = \frac{y - b}{m} = \frac{6800 - 812}{77} = \frac{5988}{77} \approx 77.766$$

<average>88</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Below is the residual plot for our regression line.

<center><img src='../assets/images/fa21-final/bills_residual.png' width=40%></center>

Which of the following is a valid conclusion that we can draw solely from the residual plot above?

( ) For this dataset, there is another line with a lower root mean squared error
( ) The root mean squared error of the regression line is 0
( ) The accuracy of the regression line's predictions depends on bill length
( ) The relationship between bill length and body mass is likely non-linear
( ) None of the above

# BEGIN SOLUTION

**Answer:** The accuracy of the regression line's predictions depends on bill length

The vertical spread in this residual plot is uneven, which implies that the regression line's predictions aren't equally accurate for all inputs. This doesn't necessarily mean that fitting a nonlinear curve would be better. It just impacts how we interpret the regression line's predictions. 

<average>40</average>

# END SOLUTION

# END SUBPROB

# END PROB