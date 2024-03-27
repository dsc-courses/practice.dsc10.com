# BEGIN PROB

# BEGIN SUBPROB

Write a single line of code that evaluates to the name of the tallest skyscraper in the `sky` DataFrame.

# BEGIN SOLN

**Answer:** `sky.sort_values(by='height', ascending=False).index[0]`

In order to answer this question, we must first sort the values of the column we are interested in. As such, we sort the entire DataFrame by the `height` column, and because we are interested in the name of the tallest building, we should set the `ascending` parameter to `False` because we would like the heights to be ordered in descending order, thus leading to the line `sky.sort_values(by='height', ascending=False)`. After sorting in descending order, we know that the tallest building is going to be the first row of the new `sky` DataFrame, and thus we now only need to get the name of the skyscraper, which happens to be in the index. In order to access the index of the DataFrame we can use `sky.index`, and in our case because we know that we want the first index, we would need to write `sky.index[0]`. Finally, putting it all together, in order to get the name of the tallest skyscraper in the `sky` DataFrame, we would need to write `sky.sort_values(by='Height', ascending=False).index[0]`. 

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Write a single line of code that evaluates to the average number of floors across all skyscrapers in the DataFrame.

# BEGIN SOLN

**Answer:** `sky.get('floors').mean()`

In order to answer the question, we must first figure out how to get the number of floors each skyscraper has. We can do this with a line of code like `sky.get('floors')` which will get the number of floors each skyscraper has. After doing this, we now need to find out the average number of floors each skyscraper has. We can do this by using the `.mean()` method, which in our case will get the average number of floors each skyscraper has. Putting this all togther, we get a line of code that looks like `sky.get('floors').mean()`.

# END SOLN

# END SUBPROB

# END PROB