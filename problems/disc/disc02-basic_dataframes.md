# BEGIN PROB

You will be using the same `sky` DataFrame provided in the first question to answer the following questions.

# BEGIN SUBPROB

Using the `sky` DataFrame, write a single line of code that evaluates to the height of the tallest skyscraper.

# BEGIN SOLN

**Answer:** `sky.get('height').max()`

In order to answer this question, we must first get the column of data that we are interested in. Because the question asks us for the tallest skyscraper it would be reasonable for us to get the `height` column of the dataset, which is why we wrote the piece of code `sky.get('height')`. Now that we have gotten all the heights of the skyscrapers, we now need some way to find the tallest skyscraper. In order to this, we can using the `.max()` method, which in this case, will return the tallest skyscraper. Putting these two parts together is how we ended up with `sky.get('height').max()`. 

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Again using the `sky` DataFrame, write a single line of code that evaluates to the average number of floors across all skyscrapers in the DataFrame.

# BEGIN SOLN

**Answer:** `sky.get('floors').mean()`

In order to answer the question, we must first figure out how to get the number of floors each skyscraper has. We can do this with a line of code like `sky.get('floors')` which will get the number of floors each skyscraper has. After doing this, we now need to find out the average number of floors each skyscraper has. We can do this by using the `.mean()` method, which in our case will get the average number of floors each skyscraper has. Putting this all togther, we get a line of code that looks like `sky.get('floors').mean()`.

# END SOLN

# END SUBPROB

# END PROB