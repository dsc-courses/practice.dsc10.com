# BEGIN PROB

The following code computes the breed of the cheapest toy dog.

```py
df[__(a)__].__(b)__.__(c)__
```
# BEGIN SUBPROB

Fill in part (a).

# BEGIN SOLUTION

**Answer: ** `df.get('kind') == 'toy'`

To find the cheapest toy dog, we can start by narrowing down our dataframe to only include dogs that are of kind toy. We do this by constructing the following boolean condition: `df.get('kind') == 'toy'`, which will check whether a dog is of kind toy (i.e. whether or not a given row's `'kind'` value is equal to `'toy'`). As a result, `df[df.get('kind') == 'toy']` will retrieve all rows for which the `'kind'` column is equal to `'toy'`.

<average>91</average>
# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Fill in part (b).

# BEGIN SOLUTION

**Answer: ** `.sort_values('price')`

Next, we can sort the resulting dataframe by price, which will make the minimum price (i.e. the cheapest toy dog) easily accessible to us later on. To sort the dataframe, simply use `.sort_values()`, with parameter `'price'` as follows:
`.sort_values('price')`

<average>86</average>
# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Which of the following can fill in blank (c)? **Select all that apply.**

[ ] `loc[0]`
[ ] `iloc[0]`
[ ] `index[0]`
[ ] `min()`

# BEGIN SOLUTION

**Answer: ** `index[0]`

- `loc[0]`: `loc` retrieves an element by the row label, which in this case is by `'breed'`, not by index value. Furthermore, `loc` actually returns the entire row, which is not what we are looking for. (Note that we are trying to find the singular `'breed'` of the cheapest toy dog.)  
- `iloc[0]`: While `iloc` does retrieve elements by index position, `iloc` actually returns the entire row, which is not what we are looking for.
- `index[0]`: Note that since `'breed'` is the index column of our dataframe, and since we have already filtered and sorted the dataframe, simply taking the `'breed'` at index 0, or `index[0]` will return the `'breed'` of the cheapest toy dog.
- `min()`: `min()` is a method used to find the smallest value on a series not a dataframe.

<average>81</average>
# END SOLUTION

# END SUBPROB

# END PROB
