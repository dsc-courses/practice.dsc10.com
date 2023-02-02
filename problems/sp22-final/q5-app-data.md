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

# BEGIN SUBPROB

Complete the implementation of the `to_minutes` function below. This function takes as input a string formatted as `'x hr, y min'` where `x` and `y` represent integers, and returns the corresponding number of minutes, **as an integer** (type `int` in Python).

For example, `to_minutes('3 hr, 5 min')` should return 185.

```py
def to_minutes(time):
    first_split = time.split(' hr, ')
    second_split = first_split[1].split(' min')
    return _________
```

What goes in the blank?

# BEGIN SOLUTION

**Answer: ** `int(first_split[0])*60+int(second_split[0])`

As the last subpart demonstrated, if we want to compare times, it doesn't make sense to do so when times are represented as strings. In the `to_minutes` function, we convert a time string into an integer number of minutes. 

The first step is to understand the logic. Every hour contains 60 minutes, so for a time string formatted like  `x hr, y min'` the total number of minutes comes from multiplying the value of `x` by 60 and adding `y`.

The second step is to understand how to extract the `x` and `y` values from the time string using the string methods `.split`. The string method `.split` takes as input some separator string and breaks the string into pieces at each instance of the separator string. It then returns a list of all those pieces. The first line of code, therefore, creates a list called `first_split` containing two elements. The first element, accessed by `first_split[0]` contains the part of the time string that comes before `' hr, '`. That is, `first_split[0]` evaluates to the string `x`. 

Similarly, `first_split[1]` contains the part of the time string that comes after `' hr, '`. So it is formatted like `'y min'`. If we split this string again using the separator of `' min'`, the result will be a list whose first element is the string `'y'`. This list is saved as `second_split` so `second_split[0]` evaluates to the string `y`.

Now we have the pieces we need to compute the number of minutes, using the idea of multiplying the value of `x` by 60 and adding `y`. We have to be careful with data types here, as the bolded instructions warn us that the function must return an integer. Right now, `first_split[0]` evaluates to the string `x` and `second_split[0]` evaluates to the string `y`. We need to convert these strings to integers before we can multiply and add. Once we convert using the `int` function, then we can multiply the number of hours by 60 and add the number of minutes. Therefore, the solution is `int(first_split[0])*60+int(second_split[0])`.

Note that failure to convert strings to integers using the `int` function would lead to very different behavior. Let's take the example time string of `'3 hr, 5 min'` as input to our function. With the return statement as `int(first_split[0])*60+int(second_split[0])`, the function would return 185 on this input, as desired. With the return statement as `first_split[0]*60+second_split[0]`, the function would return a string of length 61, looking something like this `'3333...33335'`. That's because the `*` and `+` symbols do have meaning for strings, they're just different meanings than when used with integers.

<average>71</average>
# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

You want to add to `app_data` a column called `'minutes'` with integer values representing the number of minutes it took to assemble each product.

```py
app_data = app_data.assign(minutes = _________)
app_data
```

Which of the following should go in the blank?

( ) `to_minutes('assembly_time')`
( ) `to_minutes(app_data.get('assembly_time'))`
( ) `app_data.get('assembly_time').apply(to_minutes)`
( ) `app_data.get('assembly_time').apply(to_minutes(time))`

# BEGIN SOLUTION

**Answer: ** `app_data.get('assembly_time').apply(to_minutes)`

We want to create a Series of times in minutes, since it's to be added to the `app_data` DataFrame using `.assign`. The correct way to do that is to use `.apply` so that our function, which works for one input time string, can be applied separately to every time string in the `'assembly_time'` column of `app_data`. Remember that `.apply` takes as input one parameter, the name of the function to apply, with no arguments. The correct syntax is `app_data.get('assembly_time').apply(to_minutes)`.

<average>98</average>
# END SOLUTION

# END SUBPROB

# END PROB
