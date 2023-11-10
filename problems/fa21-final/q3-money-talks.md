# BEGIN PROB

The table below shows the average amount of revenue from different sources for art museums in 2003 and 2013. 

<center><img src='../assets/images/fa21-final/means.png' width=20%></center>
<br>

# BEGIN SUBPROB

What is the total variation distance between the distribution of revenue sources in 2003 and the distribution of revenue sources in 2013? Give your answer as a proportion (i.e. a decimal between 0 and 1), **not** a percentage. Round your answer to three decimal places.

# BEGIN SOLUTION

**Answer:** 0.19

Recall, the total variation distance (TVD) is the sum of the absolute differences in proportions, divided by 2. The absolute differences in proportions for each source are as follows:

- Admissions: $|0.15 - 0.24| = 0.09$
- Restaurants and Catering: $|0.09 - 0.12| = 0.03$
- Store: $|0.52 - 0.33| = 0.19$
- Other: $|0.24 - 0.31| = 0.07$

Then, we have

$$\text{TVD} = \frac{1}{2} (0.09 + 0.03 + 0.19 + 0.07) = 0.19$$

<average>95</average>

# END SOLUTION

# END SUBPROB
# BEGIN SUBPROB

Which type of visualization would be best suited for comparing the two distributions in the table?

( ) Scatter plot
( ) Line plot
( ) Overlaid histogram
( ) Overlaid bar chart

# BEGIN SOLUTION

**Answer:** Overlaid bar chart

A **scatter plot** visualizes the relationship between two numerical variables. In this problem, we only have to visualize the distribution of a categorical variable.

A **line plot** shows trends in numerical variables over time. In this problem, we only have categorical variables. Moreover, when it says over time, it is suitable for plotting change in multiple years (e.g. 2001, 2002, 2003, ... , 2013), or even with data of days. In this question, we only want to compare the distribution of 2003 and 2013, this makes the line plot not useful. In addition, if you try to draw a line plot for this question, you will find the line plot fails to visualize distribution (e.g. the idea of 15%, 9%, 52%, and 24% add up to 100%).

An overlaid graph is useful in this question since this visualizes comparison between the two distributions.

However, an **overlaid histogram** is not useful in this problem. The key reason is the differences between a histogram and a bar chart.

Bar Chart: Space between the bars; 1 categorical axis, 1 numerical axis; order does not matter                           
Histogram: No space between the bars; intervals on axis; 2 numerical axes; order matters

In the question, we are plotting 2003 and 2013 distributions of four categories (Admissions, Restaurants and Catering, Store, and Other). 
Thus, an **overlaid bar chart** is more appropriate. 

<average>74</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

<span style="color:red"><b>Note: This problem is out of scope; it covers material no longer included in the course.</b></span>

Notably, there was an economic recession in 2008-2009. Which of the following can we conclude was an effect of the recession?

( ) The increase in revenue from admissions, as more people were visiting museums.
( ) The decline in revenue from museum stores, as people had less money to spend.
( ) The decline in total revenue, as fewer people were visiting museums.
( ) None of the above

# BEGIN SOLUTION

**Answer:** None of the above

Since we are only given the distribution of the revenue, and have no information about the amount of revenue in 2003 and 2013, we cannot conclude how the revenue has changed from 2003 to 2013 after the recession. 

For instance, if the total revenue in 2003 was 100 billion USD and the total revenue in 2013 was 50 billion USD, revenue from admissions in 2003 was 100 * 15% = 15 billion USD, and revenue from admissions in 2003 was 50 * 24% = 12 billion USD. In this case, we will have 15 > 12, the revenue from admissions has declined rather than increased (As stated by 'The increase in revenue from admissions, as more people were visiting museums.'). Similarly, since we don't know the total revenue in 2003 and 2013, we cannot conclude  'The decline in revenue from museum stores, as people had less money to spend.' or 'The decline in total revenue, as fewer people were visiting museums.'

<average>72</average>

# END SOLUTION

# END SUBPROB

# END PROB