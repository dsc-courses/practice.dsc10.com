# BEGIN PROB

Below, we've defined four functions, named `converter_1`, `converter_2`,
`converter_3`, and `converter_4`. All four functions return `"12PM"`
when `"A"` is the argument passed in and return `"1PM"` when `"B"` is
the argument passed in. Where they potentially differ is in how they
behave when called on arguments other than `"A"` and `"B"`.

Note: In the answer choices below, by `None` we mean that the function
call doesn't return anything, but doesn't error either.

# BEGIN SUBPROB

Consider the function `converter_1`, defined below.

```py
    def converter_1(section):
        if section == "A":
            return "12PM"
        else:
            return "1PM"
```

When `convert_1` is called on an argument other than `"A"` or `"B"`, what
does it return?

( ) `"12PM"`
( ) `"1PM"`
( ) `None`
( ) It errors

<br>

Consider the function `converter_2`, defined below.

```py
    def converter_2(section):
        time_dict = {
            "A": "12PM",
            "B": "1PM"
        }
        return times_dict[section]
```

When `convert_2` is called on an argument other than `"A"` or `"B"`, what does it return?

( ) `"12PM"`
( ) `"1PM"`
( ) `None`
( ) It errors

<br>

Consider the function `converter_3`, defined below.

```py
    def converter_3(section):
        if section == "A":
            return "12PM"
        elif section == "B":
            return "1PM"
        else:
            return 1 / 0
```

When converter_3 is called on an argument other than `"A"` or `"B"`, what does it return?

( ) `"12PM"`
( ) `"1PM"`
( ) `None`
( ) It errors

<br>

Consider the function `converter_4`, defined below.

```py
    def converter_4(section):
        sections = ["A", "B"]
        times = ["12PM", "1PM"]
        for i in np.arange(len(sections)):
            if section == sections[i]:
                return times[i]
```
When `converter_4` is called on an argument other than `"A"` or `"B"`, what does it return?

( ) `"12PM"`
( ) `"1PM"`
( ) `None`
( ) It errors

# BEGIN SOLUTION

**Answer**: `converter_1`: `"1PM"`, `converter_2`: It errors, `converter_3`: It errors, `converter_4`: `None`.

`converter_1`: `"1PM"`. The function `converter_1` checks if the input `section` is equal to `"A"`. If it is, the function returns `"12PM"`. However, if the input is anything other than `"A"` (including values other than `"B"`), the function defaults to the `else` condition and returns `"1PM"`. So, even for arguments other than `"A"` or `"B"`, `converter_1` will return `"1PM"`.

<average>90</average>

<br><br>

`converter_2`: It errors. The function `converter_2` utilizes a dictionary (`time_dict`) to map section values to their corresponding times. When a key that doesn't exist in the dictionary is accessed (anything other than `"A"` or `"B"`), a KeyError is raised, causing the function to error.
<average>62</average>

<br><br>

`converter_3`: It errors. The function `converter_3` specifically checks if the input section is `"A"` or `"B"`. If the input is neither `"A"` nor `"B"`, the function defaults to the else condition where it tries to divide `1` by `0`. This operation will cause a ZeroDivisionError, leading the function to error.
<average>90</average>

<br><br>

`converter_4`: `None`. The function `converter_4` uses two lists, `sections` and `times`, to map the section letters `"A"` and `"B"` to their corresponding times `"12PM"` and `"1PM"`. The function then employs a `for`-loop to traverse through the sections list. The expression `range(len(sections))` is used to generate a sequence of indices for this list; since `len(sections)` is 2, `np.arange(len(sections))` is the array `np.array([0, 1])`. Then,
- Inside the loop, the condition if `section == sections[i]` checks if the input section matches the section at the current index `i` of the `sections` list. If a match is found, the function returns the corresponding time from the `times` list using `return times[i]`.
- However, if the function traverses the entire `sections` list without finding a match (i.e., the input is neither `"A"` nor `"B"`), no `return` statement is executed. In Python, if a function completes its execution without encountering a `return` statement, it implicitly returns the value `None`. Hence, for inputs other than `"A"` or `"B"`, `converter_4` will return `None`.

<average>77</average>

# END SOLUTION

# END SUBPROB

# END PROB