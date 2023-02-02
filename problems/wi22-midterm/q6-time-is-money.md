# BEGIN PROB

Consider the following line plot, which depicts the number of skyscrapers built per year.

<center><img src='../assets/images/wi22-midterm/sky-per-year.png' width=40%></center>

# BEGIN SUBPROB

We created the line plot above using the following line of code: 

```py
sky.groupby('year').count().plot(kind='line', y='height');
```

Which of the following could we replace `'height'` with in the line of code above, such that the resulting line of code creates the same line plot? **Select all that apply.**

[ ] `'name'`
[ ] `'material'`
[ ] `'city'`
[ ] `'floors'`
[ ] `'year'`
[ ] None of the above

# BEGIN SOLN

**Answers:** `'material'`, `'city'`, and `'floors'`

Recall that when we use the `.count()` aggregation method while grouping, the values in all resulting columns are the same (they all contain the number of values in each unique group). This means that any column of `sky.groupby('year').count()` can replace `'height'` in the provided line.

`'name'` is not a column in `sky.groupby('year').count()`. `'name'` was the index in `sky`, but is not present at all in `sky.groupby('year').count()` (the original index is lost completely). `'year'` is also not a column in `sky.groupby('year').count()`, since it is the index. The remaining three columns – `'material'`, `'city'`, and `'floors'` – would all work.

<average>74</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

<span style="color:red"><b>Note: This problem is out of scope; it covers material no longer included in the course.</b></span>

Now let's look at the number of skyscrapers built each year since 1975 in New York City 🗽.

<center><img src='../assets/images/wi22-midterm/ny-per-year.png' width=40%></center>

Which of the following is a valid conclusion we can make using this graph alone?

( ) No city in the dataset had more skyscrapers built in 2015 than New York City.
( ) The decrease in the number of skyscrapers built in 2012 over previous years was due to the 2008 economic recession, and the reason the decrease is seen in 2012 rather than 2008 is because skyscrapers usually take 4 years to be built.
( ) The decrease in the number of skyscrapers built in 2012 over previous years was due to something other than the 2008 economic recession.
( ) The COVID-19 pandemic is the reason that so few skyscrapers were built in 2020.
( ) None of the above.

# BEGIN SOLN

**Answer:** None of the above.

Let's look at each answer choice.

- "No city in the dataset had more skyscrapers built in 2015 than New York City." is not necessarily true, because the graph provided only shows information for New York City. For all we know, 10000 skyscrapers were built in San Diego in 2015.
- "The decrease in the number of skyscrapers built in 2012 over previous years was due to the 2008 economic recession, and the reason the decrease is seen in 2012 rather than 2008 is because skyscrapers usually take 4 years to be built." is not necessarily true, and we have no information that suggests that it is.
- "The decrease in the number of skyscrapers built in 2012 over previous years was due to something other than the 2008 economic recession." is also not necessarily true – it _could_ be the case that the recession was the reason, but the graph doesn't tell us whether or not it is.
- "The COVID-19 pandemic is the reason that so few skyscrapers were built in 2020.", for similar reasons, is also not necessarily true.

**Tip:** This is a typical "cause-and-effect" problem that you'll see in DSC 10 exams quite often. In order to establish that some treatment had an effect, we need to run a randomized controlled trial, or have some other guarantee that there is no difference between the naturally-observed control and treatment groups.

<average>90</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

In which of the following scenarios would it make sense to draw a overlaid histogram?

( ) To visualize the number of skyscrapers of each material type, separately for New York City and Chicago.
( ) To visualize the distribution of the number of floors per skyscraper, separately for New York City and Chicago.
( ) To visualize the average height of skyscrapers built per year, separately for New York City and Chicago.
( ) To visualize the relationship between the number of floors and height for all skyscrapers.

# BEGIN SOLN

**Answer:** To visualize the distribution of the number of floors per skyscraper, separately for New York City and Chicago.

Recall, we use a histogram to visualize the distribution of a numerical variable. Here, we have a numerical variable (number of floors) that is split across two categories (New York City and Chicago), so we need to draw two histograms, or an overlaid histogram.

In the three incorrect answer choices, another visualization type is more appropriate. Given the descriptions here, see if you can draw what each of these three visualizations should look like.

- To visualize the number of skyscrapers of each material type, separately for New York City and Chicago, we'd need to draw an overlaid bar chart. For each material type, there would be two bars – one for New York City, and one for Chicago. The length of each bar would correspond to the number of skyscrapers of that material type in that city. We could color the New York City and Chicago bars in different colors.
- To visualize the average height of skyscrapers built per year, separately for New York City and Chicago, we'd need to draw an overlaid line chart. There would be two lines, one for New York City and one for Chicago (this would look similar to the plot in the previous subpart, but with another line).
- To visualize the relationship between the number of floors and height for all skyscrapers, we'd need to draw a scatter plot. This is because scatter plots are the correct tool to use to visualize the relationship between two numerical variables, and both "number of floors" and "height" are numerical variables.

<average>62</average>

# END SOLN

# END SUBPROB

# END PROB