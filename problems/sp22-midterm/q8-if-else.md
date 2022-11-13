# BEGIN PROB

Consider an artist that has only appeared once at Sun God. At the time of their Sun God performance, we'll call the artist 

- **outdated** if their top hit came out more than five years prior,
- **trending** if their top hit came out within the five years prior, and
- **up-and-coming** if their top hit came out after they appeared at Sun God.

Complete the function below so it outputs the appropriate description for any input artist who has appeared exactly once at Sun God.

```py
def classify_artist(artist):
    filtered = merged[merged.get('Artist') == artist]
    year = filtered.get('Year').iloc[0]
    top_hit_year = filtered.get('Top_Hit_Year').iloc[0]
    if ___(a)___ > 0:
        return 'up-and-coming'
    elif ___(b)___:
        return 'outdated'
    else:
        return 'trending'
```


# BEGIN SUBPROB
What goes in blank (a)?
# BEGIN SOLUTION
**Answer: ** `top_hit_year - year`

Before we can answer this question, we need to understand what the first three lines of the `classify_artist` function are doing. The first line creates a DataFrame with only one row, corresponding to the particular artist that's passed in as input to the function. We know there is just one row because we are told that the artist being passed in as input has appeared exactly once at Sun God. The next two lines create two variables: 

- `year` contains the year in which the artist performed at Sun God, and 
- `top_hit_year` contains the year in which their top hit song was released.

Now, we can fill in blank (a). Notice that the body of the `if` clause is `return 'up-and-coming'`. Therefore we need a condition that corresponds to up-and-coming, which we are told means the top hit came out after the artist appeared at Sun God. Using the variables that have been defined for us, this condition is `top_hit_year > year`. However, the `if` statement condition is already partially set up with `> 0` included. We can simply rearrange our condition `top_hit_year > year` by subtracting `year` from both sides to obtain `top_hit_year - year > 0`, which fits the desired format.

<average>89</average>


# END SOLUTION
# END SUBPROB
# BEGIN SUBPROB
What goes in blank (b)?
# BEGIN SOLUTION
**Answer: ** `year-top_hit_year > 5`

For this part, we need a condition that corresponds to an artist being outdated which happens when their top hit came out more than five years prior to their appearance at Sun God. There are several ways to state this condition: `year-top_hit_year > 5`, `year > top_hit_year + 5`, or any equivalent condition would be considered correct. 

<average>89</average>

# END SOLUTION
# END SUBPROB
# END PROB
