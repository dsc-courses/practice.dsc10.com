# BEGIN PROB

# BEGIN SUBPROB

Which of the following blocks of code correctly assigns `random_art_museums` to an array of the names of 10 art museums, randomly selected without replacement from those in `art_museums`? Select all that apply.

Option 1:
```py
def get_10(df):
    return np.array(df.sample(10).get('Name'))

random_art_museums = get_10(art_museums)
```

Option 2:
```py
def get_10(art_museums):
    return np.array(art_museums.sample(10).get('Name'))

random_art_museums = get_10(art_museums)
```

Option 3:
```py
def get_10(art_museums):
    random_art_museums = np.array(art_museums.sample(10).get('Name'))

random_art_museums = get_10(art_museums)
```

Option 4:
```py
def get_10():
    return np.array(art_museums.sample(10).get('Name'))

random_art_museums = get_10()
```

Option 5:
```py
random_art_museums = np.array([])

def get_10():
    random_art_museums = np.array(art_museums.sample(10).get('Name'))
    return random_art_museums

get_10()
```

[ ] Option 1
[ ] Option 2
[ ] Option 3
[ ] Option 4
[ ] Option 5
[ ] None of the above

# BEGIN SOLN

**Answers:** Option 1, Option 2, and Option 4

Note that if `df` is a DataFrame, then `df.sample(10)` is a DataFrame containing 10 randomly selected rows in `df`. With that in mind, let's look at all of our options.

- **Option 1:** This implementation of `get_10` takes in a DataFrame `df` and returns an array containing 10 randomly selected values in `df`'s `'Name'` column. After defining `get_10`, we assign `random_art_museums` to the result of calling `get_10(art_museums)`. This assigns `random_art_museums` as intended, so Option 1 is correct.
- **Option 2:** This option is functionally the same as Option 1, so it is also correct. The only difference between Option 2 and Option 1 is that Option 2 uses the parameter name `art_museums` and Option 1 uses the parameter name `df` (both in the `def` line and in the function body); this does not change the behavior of `get_10` or the lines afterward.
- **Option 3:** `get_10` here does not return anything! So, `get_10(art_museums)` evaluates to `None` (which means "nothing" in Python), and `random_art_museums` is also `None`, meaning Option 3 is incorrect.
- **Option 4:** At first, it may appear that this option is wrong, as `get_10` does not take in any inputs. However, the body of `get_10` contains a reference to the DataFrame `art_museums`, which is ultimately where we want to sample from. As a result, `get_10` does indeed return an array containing 10 randomly selected museum names, and `random_art_museums = get_10()` correctly assigns `random_art_museums` to this array, so Option 4 is correct.
- **Option 5:** Here, `get_10` returns the correct array. However, outside of the function, `random_art_museums` is never assigned to the output of `get_10`. (The variable name `random_art_museums` inside the function has nothing to do with the array defined before and outside the function.) As a result, after running the line `get_10()` at the bottom of the code block, `random_art_museums` is still an empty array, and as such, Option 5 is incorrect.

<average>85</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

London has the most art museums in the top 100 of any city in the world. The most visited art museum in London is `'Tate Modern'`. 

Which of the following blocks of code correctly assigns `best_in_london` to `'Tate Modern'`? Select all that apply.

Option 1:
```py
def most_common(df, col):
    return df.groupby(col).count().sort_values(by='Rank', ascending=False).index[0]

def most_visited(df, col, value):
    return df[df.get(col)==value].sort_values(by='Visitors', ascending=False).get('Name').iloc[0]

best_in_london = most_visited(art_museums, 'City', most_common(art_museums, 'City'))
```

Option 2:
```py
def most_common(df, col):
    print(df.groupby(col).count().sort_values(by='Rank', ascending=False).index[0])

def most_visited(df, col, value):
    print(df[df.get(col)==value].sort_values(by='Visitors', ascending=False).get('Name').iloc[0])

best_in_london = most_visited(art_museums, 'City', most_common(art_museums, 'City'))
```

Option 3:
```py
def most_common(df, col):
    return df.groupby(col).count().sort_values(by='Rank', ascending=False).index[0]

def most_visited(df, col, value):
    print(df[df.get(col)==value].sort_values(by='Visitors', ascending=False).get('Name').iloc[0])

best_in_london = most_visited(art_museums, 'City', most_common(art_museums, 'City'))
```

[ ] Option 1
[ ] Option 2
[ ] Option 3
[ ] None of the above

# BEGIN SOLN

**Answer:** Option 1 only

At a glance, it may seem like there's a lot of reading to do to answer the question. However, it turns out that all 3 options follow similar logic; the difference is in their use of `print` and `return` statements. Whenever we want to "save" the output of a function to a variable name or use it in another function, we need to `return` somewhere within our function. Only Option 1 contains a `return` statement in both `most_common` and `most_visited`, so it is the only correct option.

Let's walk through the logic of Option 1 (which we don't necessarily need to do to answer the problem, but we should in order to enhance our understanding):

- First, we use `most_common` to find the city with the most art museums. `most_common` does this by grouping the input DataFrame `df` (`art_museums`, in this case) by `'City'` and using the `.count()` method to find the number of rows per `'City'`. Note that when using `.count()`, all columns in the aggregated DataFrame will contain the same information, so it doesn't matter which column you use to extract the counts per group. After sorting by one of these columns (`'Rank'`, in this case) in decreasing order, `most_common` takes the first value in the `index`, which will be the name of the `'City'` with the most art museums. **This is London**, i.e. `most_common(art_museums, 'City')` evaluates to `'London'` in Option 1 (in Option 2, it evaluates to `None`, since `most_common` there doesn't `return` anything).
- Then, we use `most_visited` to find the museum with the most visitors in the city with the most museums. This is achieved by keeping only the rows of the input DataFrame `df` (again, `art_museums` in this case) where the value in the `col` (`'City'`) column is `value` (`most_common(art_museums, 'City')`, or `'London'`). Now that we only have information for museums in London, we can sort by `'Visitors'` to find the most visited such museum, and take the first value from the resulting `'Name'` column. While all 3 options follow this logic, only Option 1 **returns** the desired value, and so only Option 1 assigns `best_in_london` correctly. (Even if Option 2's `most_visited` used `return` instead of `print`, it still wouldn't work, since Option 2's `most_common` also uses `print` instead of `return`).

<average>86</average>

# END SOLN

# END SUBPROB

# END PROB