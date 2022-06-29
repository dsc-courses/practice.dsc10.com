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

**Answer: ** `cookie_box, 2, replace=False`

solution here

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

What goes in blank (b)?

# BEGIN SOLUTION

**Answer: ** `grab[0] == grab[1]`

solution here

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

What goes in blank (c)?

( ) `prob_both_same / repetitions`
( ) `prob_both_same / 2`
( ) `np.mean(prob_both_same)`
( ) `prob_both_same.mean()`

# BEGIN SOLUTION

**Answer: ** `prob_both_same / repetitions`

solution here

# END SOLUTION

# END SUBPROB

# END PROB