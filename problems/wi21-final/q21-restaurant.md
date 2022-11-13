# BEGIN PROB

A restaurant keeps track of each table's number of people (average 3; standard deviation 1) and the amount of the bill (average $60, standard deviation $12). If the number of people and amount of the bill are linearly associated with correlation 0.8, what is the predicted bill for a table of 5 people? Input your answer below, **to the nearest cent**. Make sure your answer is just a number and does not include the $ symbol or any text.

# BEGIN SOLUTION

**Answer: ** 79.20

To answer this question, first find the z score for a table of 5 people. Z = (5-3)/1 = 2. 
Now having this Z score, find the price that correlated in the bill distribution by finding the value
for 2 standard deviations larger than the mean while also accounting for the correlation between the two variables.
This is calculated with mean + ((Z*SD) * r)  which is 60 + ((12 * 2) * 0.8) = 79.20.

Alternatively, we could solve for the regression line and plug our values in according to the reference sheet:

m = (0.8) * (12/1) and b = 60 - (48/5) * 3 (where m is the slope and b is the y-intercept)

Thus plugging the appropriate values in our regression line yields

y = (48/5) * 5 + 60 - (48/5)*3 = 79.2
 
<average>88</average>
# END SOLUTION



# END PROB
