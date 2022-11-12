# BEGIN PROB
You are given a DataFrame called `sports`, indexed by `'Sport'` containing one column, `'PlayersPerTeam'`. The first few rows of the DataFrame are shown below:

| Sport    | PlayersPerTeam |
| ----------- | ----------- |
| baseball      | 9       |
| basketball   | 5        |
| field hockey   | 11        |
<br />
Which of the following evaluates to `'basketball'`?

( ) `sports.loc[1]`
( ) `sports.iloc[1]`
( ) `sports.index[1]`
( ) `sports.get('Sport').iloc[1]`

# BEGIN SOLUTION

**Answer: ** `sports.index[1]`

We are told that the DataFrame is indexed by `'Sport'` and `'basketball'` is one of the elements of the index. To access an element of the index, we use `.index` to extract the index and square brackets to extract an element at a certain position. Therefore, `sports.index[1]` will evaluate to `'basketball'`.

The first two answer choices attempt to use `.loc` or `.iloc` directly on a DataFrame. We typically use `.loc` or `.iloc` on a Series that results from using `.get` on some column. Although we don't typically do it this way, it is possible to use `.loc` or `.iloc` directly on a DataFrame, but doing so would produce an entire row of the DataFrame. Since we want just one word, `'basketball'`, the first two answer choices must be incorrect. 

The last answer choice is incorrect because we can't use `.get` with the index, only with a column. The index is never considered a column.

<average>88</average>
# END SOLUTION

# END PROB