# BEGIN PROB

Recall that an IKEA fan created an app for people to log the amount of time it takes them to assemble an IKEA product. We have this data in `app_data`.

# BEGIN SUBPROB
Suppose that when someone downloads the app, the app requires them to choose a username, which must be different from all other registered usernames. 

**True or False**: If `app_data` had included a column with the username of the person who reported each product build, it would make sense to index `app_data` by username.

( ) True
( ) False

# BEGIN SOLUTION

**Answer: ** False

Even though people must have distinct usernames, one person can build multiple different IKEA products and log their time for each build. So we don't expect every row of `app_data` to have a distinct username associated with it, and therefore username would not be suitable as an index, since the index should have distinct values.
<average>52</average>
# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

What does the code below evaluate to?

```py
(app_data.take(np.arange(4))
         .sort_values(by='assembly_time')
         .get('assembly_time')
         .iloc[0])
```

*Hint:* The `'assembly_time'` column contains strings.

# BEGIN SOLUTION

**Answer: ** `'1 hr, 45 min'`

The code says that we should take the first four rows of `app_data` (which we can see in the preview at the start of this exam), sort the rows in ascending order of `'assembly_time'`, and extract the very first entry of the `'assembly_time'` column. In other words, we have to find the `'assembly_time'` value that would be first when sorted in ascending order. As given in the hint, the `'assembly_time'` column contains strings, and strings get sorted alphabetically, so we are looking for the assembly time, among the first four, that would come first alphabetically. This is `'1 hr, 45 min'`.

Note that first alphabetically does not correspond to the least amount of time. `'1 hr, 5 min'` represents less time than `'1 hr, 45 min'`, but in alphabetical order `'1 hr, 45 min'` comes before `'1 hr, 5 min'` because both start with the same characters `'1 hr, '` and comparing the next character, `'4'` comes before `'5'`. 
<average>46</average>
# END SOLUTION

# END SUBPROB

# END PROB
