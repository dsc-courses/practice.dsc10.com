# BEGIN PROB

Laura built the LAPPLAND TV storage unit in 2 hours and 30 minutes, and she thinks she worked at an average speed. If you want to see whether the average time to build the TV storage unit is indeed 2 hours and 30 minutes using the sample of assembly times in `app_data`, which of the following tools **could** you use to help you? Select all that apply.

[ ] hypothesis testing
[ ] permutation testing
[ ] bootstrapping
[ ] Central Limit Theorem
[ ] confidence interval
[ ] regression

# BEGIN SOLUTION

**Answer: ** hypothesis testing, bootstrapping, Central Limit Theorem, confidence interval

The average time to build the LAPPLAND TV storage unit is an unknown population parameter. We're trying to figure out if this parameter could be equal to the specific value of 2 hours and 30 minutes. We can use the framework we learned in class to set this up as a hypothesis test via confidence interval. When we have a null hypothesis of the form "the parameter equals the specific value" and an alternative hypothesis of "it does not," this framework applies, and conducting the hypothesis test is equivalent to constructing a confidence interval for the parameter and seeing if the specific value falls in the interval. 

There are two ways in which we could construct the confidence interval. One is through bootstrapping, and the other is through the Central Limit Theorem, which applies in this case because our statistic is the mean. 

The only listed tools that could not be used here are permutation testing and regression. Permutation testing is used to determine whether two samples could have come from the same population, but here we only have one sample. Permutation testing would be helpful to answer a question like, "Does it take the same amount of time to assemble the LAPPLAND TV storage as it does to assemble the HAUGA TV storage unit?"

Regression is used to predict one numerical quantity based on another, not to estimate a parameter as we are doing here. Regression would be appropriate to answer a question like, "How does the assembly time for the LAPPLAND TV storage unit change with the assembler's age?"

<average>78</average>
# END SOLUTION

# END PROB