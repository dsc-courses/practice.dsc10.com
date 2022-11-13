# BEGIN PROB

For this question, let's think of the data in `app_data` as a random sample of all IKEA purchases and use it to test the following hypotheses.

**Null Hypothesis**: IKEA sells an equal amount of beds (category `'bed'`) and outdoor furniture (category `'outdoor'`). 

**Alternative Hypothesis**: IKEA sells more beds than outdoor furniture.

The DataFrame `app_data` contains 5000 rows, which form our sample. Of these 5000 products,

- 1000 are beds,
- 1500 are outdoor furniture, and
- 2500 are in another category.

# BEGIN SUBPROB

Which of the following **could** be used as the test statistic for this hypothesis test? Select all that apply.

[ ] Among 2500 beds and outdoor furniture items, the absolute difference between the proportion of beds and the proportion of outdoor furniture.
[ ] Among 2500 beds and outdoor furniture items, the proportion of beds.
[ ] Among 2500 beds and outdoor furniture items, the number of beds.
[ ] Among 2500 beds and outdoor furniture items, the number of beds plus the number of outdoor furniture items.

# BEGIN SOLUTION

**Answer: ** Among 2500 beds and outdoor furniture items, the proportion of beds. <br>
Among 2500 beds and outdoor furniture items, the number of beds.

Our test statistic needs to be able to distinguish between the two hypotheses. The first option does not do this, because it includes an absolute value. If the absolute difference between the proportion of beds and the proportion of outdoor furniture were large, it could be because IKEA sells more beds than outdoor furniture, but it could also be because IKEA sells more outdoor furniture than beds. 

The second option is a valid test statistic, because if the proportion of beds is large, that suggests that the alternative hypothesis may be true.

Similarly, the third option works because if the number of beds (out of 2500) is large, that suggests that the alternative hypothesis may be true.

The fourth option is invalid because out of 2500 beds and outdoor furniture items, the number of beds plus the number of outdoor furniture items is always 2500. So the value of this statistic is constant regardless of whether the alternative hypothesis is true, which means it does not help you distinguish between the two hypotheses.

<average>78</average>
# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Let's do a hypothesis test with the following test statistic: among 2500 beds and outdoor furniture items, the proportion of outdoor furniture minus the proportion of beds.

Complete the code below to calculate the observed value of the test statistic and save the result as `obs_diff`.

```py
    outdoor = (app_data.get('category')=='outdoor') 
    bed = (app_data.get('category')=='bed')
    obs_diff = ( ___(a)___ - ___(b)___ ) / ___(c)___
```

The table below contains several Python expressions. Choose the correct expression to fill in each of the three blanks. Three expressions will be used, and two will be unused.

<center><img src='../assets/images/sp22-final/q8-table.jpg' width=50%></center>

# BEGIN SOLUTION

**Answer: ** Reading the table from top to bottom, the five expressions should be used in the following blanks: None, (b), (a), (c), None.

The correct way to define `obs_diff` is

```py
    outdoor = (app_data.get('category')=='outdoor') 
    bed = (app_data.get('category')=='bed')
    obs_diff = (app_data[outdoor].shape[0] - app_data[bed].shape[0]) / app_data[outdoor | bed].shape[0]
```

The first provided line of code defines a boolean Series called `outdoor` with a value of `True` corresponding to each outdoor furniture item in `app_data`. Using this as the condition in a query results in a DataFrame of outdoor furniture items, and using `.shape[0]` on this DataFrame gives the number of outdoor furniture items. So `app_data[outdoor].shape[0]` represents the number of outdoor furniture items in `app_data`. Similarly, `app_data[bed].shape[0]` represents the number of beds in `app_data`. Likewise, `app_data[outdoor | bed].shape[0]` represents the total number of outdoor furniture items and beds in `app_data`. Notice that we need to use an *or* condition (`|`) to get a DataFrame that contains both outdoor furniture and beds.

We are told that the test statistic should be the proportion of outdoor furniture minus the proportion of beds. Translating this directly into code, this means the test statistic should be calculated as

```py
    obs_diff = app_data[outdoor].shape[0]/app_data[outdoor | bed].shape[0] - app_data[bed].shape[0]) / app_data[outdoor | bed].shape[0]
```

Since this is a difference of two fractions with the same denominator, we can equivalently subtract the numerators first, then divide by the common denominator, using the mathematical fact $$\frac{a}{c} - \frac{b}{c} = \frac{a-b}{c}.$$

This yields the answer

```py
    obs_diff = (app_data[outdoor].shape[0] - app_data[bed].shape[0]) / app_data[outdoor | bed].shape[0]
```

Notice that this is the *observed* value of the test statistic because it's based on the real-life data in the `app_data` DataFrame, not simulated data.

<average>90</average>
# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Suppose we generate 10,000 simulated values of the test statistic according to the null model and store them in an array called `simulated_diffs`. Complete the code below to calculate the p-value for the hypothesis test.

```py
    np.count_nonzero(simulated_diffs _________ obs_diff)/10000
```

What goes in the blank?

( )  `<`
( )  `<=`
( )  `>`
( )  `>=`

# BEGIN SOLUTION

**Answer: ** `<=`

To answer this question, we need to know whether small values or large values of the test statistic indicate the alternative hypothesis. The alternative hypothesis is that IKEA sells more beds than outdoor furniture. Since we're calculating the proportion of outdoor furniture minus the proportion of beds, this difference will be small (negative) if the alternative hypothesis is true. Larger (positive) values of the test statistic mean that IKEA sells more outdoor furniture than beds. A value near 0 means they sell beds and outdoor furniture equally.

The p-value is defined as the proportion of simulated test statistics that are equal to the observed value or more extreme, where extreme means in the direction of the alternative. In this case, since small values of the test statistic indicate the alternative hypothesis, the correct answer is `<=`.

<average>43</average>
# END SOLUTION

# END SUBPROB

# END PROB