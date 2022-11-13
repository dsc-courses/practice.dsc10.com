# BEGIN PROB

You order 25 large pizzas from your local pizzeria. The pizzeria claims that these pizzas are 16 inches in diameter, but you’re not so sure. You measure each pizza’s diameter and collect a dataset of 25 actual pizza diameters. You want to run a hypothesis test to determine whether the pizzeria’s claim is accurate.

# BEGIN SUBPROB

What would your Null Hypothesis be?

What would your Alternative Hypothesis be?

# BEGIN SOLUTION

**Answer: ** 

Null Hypothesis: The mean pizza diameter at the local pizzeria is 16 inches.

Alternative Hypothesis: The mean pizza diameter at the local pizzeria is not 16 inches.

The null hypothesis is the hypothesis where there is no significant difference from some statement.
In this case, the statement of interest is the pizzeria's claims of pizzas are 16 inches in diameter.

The alternative hypothesis is a statement that contradicts the null hypothesis. In this case this statement
is that the mean pizza diameter at the local pizzeria is not 16 inches. (ie. the other option to the null hypothesis)
<average>35</average>
# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

What test statistic would you use?

# BEGIN SOLUTION

**Answer: ** Mean Pizza Diameter, or other valid statistics such as the (absolute) difference between each pizza's diameter and 16 (expected value)

Looking at the null and alternative hypothesis we can see we are directly interested in the mean pizza diameter, so it is most 
likely the best measurement for the test statistic. The main idea is that we somehow want to show the difference in distribution of the pizza diameters.

<average>70</average>
# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Explain how you would do your hypothesis test and how you would draw a conclusion from your results.

# BEGIN SOLUTION

**Answer: ** Answers vary, should include the following

- Generate confidence interval for population mean (or equivalent) by bootstrapping (or by calculating directly with the sample).

- Correctly describe how to reject or fail to reject the null hypothesis (depending on whether interval contains 16, for example).

When conducting the hypothesis test, we first want to create a confidence interval either by using bootstrapping or constructing a 95% confidence
interval to understand the true mean diameter of pizzas. The next step is to define the rejection criteria,
failing to reject the null if 16 is within the 95% confidence interval (since we believe the true population mean) is within 
this range with 95% confidence. We will reject the null hypothesis if 16 is not within the 95% confidence interval. Note that
this assumes you used true mean diameter of pizzas as your test statistic. 

<average>38</average>
# END SOLUTION

# END SUBPROB


# END PROB
