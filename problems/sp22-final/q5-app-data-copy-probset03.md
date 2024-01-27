# BEGIN PROB

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

# END PROB
