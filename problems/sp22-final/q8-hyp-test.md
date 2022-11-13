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
Which of the following is a valid way to generate one value of the test statistic according to the null model? Select all that apply.

Way 1: 

```py
multi = np.random.multinomial(2500, [0.5,0.5]) 
(multi[0] - multi[1])/2500
```

Way 2: 

```py
outdoor = np.random.multinomial(2500, [0.5,0.5])[0]/2500 
bed = np.random.multinomial(2500, [0.5,0.5])[1]/2500 
outdoor - bed 
```

Way 3:

 ```py
choice = np.random.choice([0, 1], 2500, replace=True) 
choice_sum = choice.sum( ) 
(choice_sum - (2500 - choice_sum))/2500
```

Way 4: 

```py
choice = np.random.choice(['bed', 'outdoor'], 2500, replace=True) 
bed = np.count_nonzero(choice=='bed')
outdoor = np.count_nonzero(choice=='outdoor')
outdoor/2500 - bed/2500
```

Way 5: 

```py
outdoor = (app_data.get('category')=='outdoor') 
bed = (app_data.get('category')=='bed')
samp = app_data[outdoor|bed].sample(2500, replace=True) 
samp[samp.get('category')=='outdoor'].shape[0]/2500 -  samp[samp.get('category')=='bed'].shape[0]/2500)
```

Way 6: 

```py
outdoor = (app_data.get('category')=='outdoor') 
bed = (app_data.get('category')=='bed')
samp = (app_data[outdoor|bed].groupby('category').count( ).reset_index( ).sample(2500, replace=True))    
samp[samp.get('category')=='outdoor'].shape[0]/2500 - samp[samp.get('category')=='bed'].shape[0]/2500
```

[ ] Way 1
[ ] Way 2
[ ] Way 3
[ ] Way 4
[ ] Way 5
[ ] Way 6


# BEGIN SOLUTION

**Answer: ** Way 1, Way 3, Way 4, Way 6

Let's consider each way in order.

Way 1 is a correct solution. This code begins by defining a variable `multi` which will evaluate to an array with two elements representing the number of items in each of the two categories, after 2500 items are drawn randomly from the two categories, with each category being equally likely. In this case, our categories are beds and outdoor furniture, and the null hypothesis says that each category is equally likely, so this describes our scenario accurately. We can interpret `multi[0]` as the number of outdoor furniture items and `multi[1]` as the number of beds when we draw 2500 of these items with equal probability. Using the same mathematical fact from the solution to Problem 8.2, we can calculate the difference in proportions as the difference in number divided by the total, so it is correct to calculate the test statistic as `(multi[0] - multi[1])/2500`. 

Way 2 is an incorrect solution. Way 2 is based on a similar idea as Way 1, except it calls `np.random.multinomial` twice, which corresponds to two separate random processes of selecting 2500 items, each of which is equally likely to be a bed or an outdoor furniture item. However, is not guaranteed that the number of outdoor furniture items in the first random selection plus the number of beds in the second random selection totals 2500. Way 2 calculates the proportion of outdoor furniture items in one random selection minus the proportion of beds in another. What we want to do instead is calculate the difference between the proportion of outdoor furniture and beds in a single random draw.

Way 3 is a correct solution. Way 3 does the random selection of items in a different way, using `np.random.choice`. Way 3 creates a variable called `choice` which is an array of 2500 values. Each value is chosen from the list `[0,1]` with each of the two list elements being equally likely to be chosen. Of course, since we are choosing 2500 items from a list of size 2, we must allow replacements. We can interpret the elements of `choice` by thinking of each 1 as an outdoor furniture item and each 0 as a bed. By doing so, this random selection process matches up with the assumptions of the null hypothesis. Then the sum of the elements of `choice` represents the total number of outdoor furniture items, which the code saves as the variable `choice_sum`. Since there are 2500 beds and outdoor furniture items in total, `2500 - choice_sum` represents the total number of beds. Therefore, the test statistic here is correctly calculated as the number of outdoor furniture items minus the number of beds, all divided by the total number of items, which is 2500.

Way 4 is a correct solution. Way 4 is similar to Way 3, except instead of using 0s and 1s, it uses the strings `'bed'` and `'outdoor'` in the `choice` array, so the interpretation is even more direct. Another difference is the way the number of beds and number of outdoor furniture items is calculated. It uses `np.count_nonzero` instead of sum, which wouldn't make sense with strings. This solution calculates the proportion of outdoor furniture minus the proportion of beds directly.

Way 5 is an incorrect solution. As described in the solution to Problem 8.2, `app_data[outdoor|bed]` is a DataFrame containing just the outdoor furniture items and the beds from `app_data`. Based on the given information, we know `app_data[outdoor|bed]` has 2500 rows, 1000 of which correspond to beds and 1500 of which correspond to furniture items. This code defines a variable `samp` that comes from sampling this DataFrame 2500 times with replacement. This means that each row of `samp` is equally likely to be any of the 2500 rows of `app_data[outdoor|bed]`. The fraction of these rows that are beds is $1000/2500 = 2/5$ and the fraction of these rows that are outdoor furniture items is $1500/2500 = 3/5$. This means the random process of selecting rows randomly such that each row is equally likely does not make each item equally likely to be a bed or outdoor furniture item. Therefore, this approach does not align with the assumptions of the null hypothesis. 

Way 6 is a correct solution. Way 6 essentially modifies Way 5 to make beds and outdoor furniture items equally likely to be selected in the random sample. As in Way 5, the code involves the DataFrame `app_data[outdoor|bed]` which contains 1000 beds and 1500 outdoor furniture items. Then this DataFrame is grouped by `'category'` which results in a DataFrame indexed by `'category'`, which will have only two rows, since there are only two values of `'category'`, either `'outdoor'` or `'bed'`. The aggregation function `.count()` is irrelevant here. When the index is reset, `'category'` becomes a column. Now, randomly sampling from this two-row grouped DataFrame such that each row is equally likely to be selected *does* correspond to choosing items such that each item is equally likely to be a bed or outdoor furniture item. The last line simply calculates the proportion of outdoor furniture items minus the proportion of beds in our random sample drawn according to the null model.


<average>59</average>
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