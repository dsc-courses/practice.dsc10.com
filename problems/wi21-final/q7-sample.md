# BEGIN PROB

Assume `df` is a DataFrame with distinct rows. Which of the following best describes `df.sample(10)`?

( ) an array of length 10, where some of the entries might be the same
( ) an array of length 10, where no two entries can be the same
( ) a DataFrame with 10 rows, where some of the rows might be the same
( ) a DataFrame with 10 rows, where no two rows can be the same

# BEGIN SOLUTION

**Answer: ** a DataFrame with 10 rows, where no two rows can be the same

Looking at the documentation for `.sample()` we can see that it accepts a few arguments. The first argument
specifies the number of rows (which is why we specify 10). The next argument is a boolean that specifies if the sampling
happens with or without replacement. By default, the sampling will occur without replacement (which happens in this question since
no argument is specified so the default is evoked). Looking at the return, we can see that since we are sampling a dataframe,
a dataframe will also be returned which is why a DataFrame with 10 rows, where no two rows can be the same is correct.

<average>94</average>
# END SOLUTION

# END PROB
