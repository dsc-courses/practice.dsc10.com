# BEGIN PROB

King Triton has boarded a Southwest flight. For in-flight refreshments, Southwest serves four types of cookies – chocolate chip, gingerbread, oatmeal, and peanut butter.

The flight attendant comes to King Triton with a box containing 10 cookies:

- 4 chocolate chip
- 3 gingerbread
- 2 oatmeal, and
- 1 peanut butter

The flight attendant tells King Triton to grab 2 cookies out of the box without looking.

Fill in the blanks below to implement a simulation that estimates the probability that both of King Triton's selected cookies are the same.

```python
# 'cho' stands for chocolate chip, 'gin' stands for gingerbread,
# 'oat' stands for oatmeal, and 'pea' stands for peanut butter.

cookie_box = np.array(['cho', 'cho', 'cho', 'cho', 'gin', 
                       'gin', 'gin', 'oat', 'oat', 'pea'])

repetitions = 10000
prob_both_same = 0
for i in np.arange(repetitions):
    grab = np.random.choice(__(a)__)
    if __(b)__:
        prob_both_same = prob_both_same + 1
prob_both_same = __(c)__
```

# BEGIN SUBPROB

What goes in blank (a)?

( ) `cookie_box, repetitions, replace=False`
( ) `cookie_box, 2, replace=True`
( ) `cookie_box, 2, replace=False`
( ) `cookie_box, 2`

# BEGIN SOLUTION

**Answer:** `cookie_box, 2, replace=False`

We are told that King Triton grabs two cookies out of the box without looking. Since this is a random choice, we use the function `np.random.choice` to simulate this. The first input to this function is a sequence of values to choose from. We already have an array of values to choose from in the variable `cookie_box`. Calling `np.random.choice(cookie_box)` would select one cookie from the cookie box, but we want to select two, so we use an optional second parameter to specify the number of items to randomly select. Finally, we should consider whether we want to select with or without replacement. Since `cookie_box` contains individual cookies and King Triton is selecting two of them, he cannot choose the same exact cookie twice. This means we should sample without replacement, by specifying `replace=False`. Note that omitting the `replace` parameter would use the default option of sampling with replacement. 

<average>92</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

What goes in blank (b)?

# BEGIN SOLUTION

**Answer:** `grab[0] == grab[1]`

The idea of a simulation is to do some random process many times. We can use the results to approximate a probability by counting up the number of times some event occurred, and dividing that by the number of times we did the random process. Here, the random process is selecting two cookies from the cookie box, and we are doing this 10,000 times. The approximate probability will be the number of times in which both cookies are the same divided by 10,000. So we need to count up the number of times that both randomly selected cookies are the same. We do this by having an accumulator variable that starts out at 0 and gets incremented, or increased by 1, every time both cookies are the same. The code has such a variable, called `prob_both_same`, that is initialized to 0 and gets incremented when some condition is met. 

We need to fill in the condition, which is that both randomly selected cookies are the same. We've already randomly selected the cookies and stored the results in `grab`, which is an array of length 2 that comes from the output of a call to `np.random.choice`. To check if both elements of the `grab` array are the same, we access the individual elements using brackets with the position number, and compare using the `==` symbol to check equality. Note that at the end of the `for` loop, the variable `prob_both_same` will contain a count of the number of trials out of 10,000 in which both of King Triton's cookies were the same flavor.

<average>79</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

What goes in blank (c)?

( ) `prob_both_same / repetitions`
( ) `prob_both_same / 2`
( ) `np.mean(prob_both_same)`
( ) `prob_both_same.mean()`

# BEGIN SOLUTION

**Answer:** `prob_both_same / repetitions`

After the `for` loop, `prob_both_same` contains the number of trials out of 10,000 in which both of King Triton's cookies were the same flavor. We'd like it to represent the approximate probability of both cookies being the same flavor, so we need to divide the current value by the total number of trials, 10,000. Since this value is stored in the variable `repetitions`, we can divide `prob_both_same` by `repetitions`.

<average>93</average>

# END SOLUTION

# END SUBPROB

# END PROB