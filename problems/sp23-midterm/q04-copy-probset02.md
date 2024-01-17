# BEGIN PROB

# BEGIN SUBPROB

We'd like to find the mean number of Instagram followers of all students
in DSC 10. One **correct** way to do so is given below.

```py
    mean_1 = survey.get("IG Followers").mean()
```

Another two **possible** ways to do this are given below.

```py
    # Possible method 1.
    mean_2 = survey.groupby("Section").mean().get("IG Followers").mean()

    # Possible method 2.
    X = survey.groupby("Section").sum().get("IG Followers").sum()
    Y = survey.groupby("Section").count().get("IG Followers").sum()
    mean_3 = X / Y
```
Is `mean_2` equal to `mean_1`?

( ) Yes.
( ) Yes, if both sections have the same number of students, otherwise maybe.
( ) Yes, if both sections have the same number of students, otherwise no.
( ) No.

Is `mean_3` equal to `mean_1`?

( ) Yes.
( ) Yes, if both sections have the same number of students, otherwise maybe.
( ) Yes, if both sections have the same number of students, otherwise no.
( ) No.

# BEGIN SOLUTION

**Answer**:

**Is `mean_2` is equal to `mean_1`? Yes, if both sections have the same number of students, otherwise maybe.**

`mean_2` is the "mean of means" – it finds the mean number of `"IG Followers"` for each section, then finds the mean of those two numbers. This is not in general to the overall mean, because it doesn't consider the fact that Section A may have more students than Section B (or vice versa); if this is the case, then Section A needs to be weighted more heavily in the calculation of the overall mean.

Let's look at a few examples to illustrate our point.
- Suppose Section A has 2 students who both have 10 followers, and Section B has 1 student who has 5 followers. The overall mean number of followers is $\frac{10 + 10 + 5}{3} = 8.33..$, while the mean of the means is $\frac{10 + 5}{2} = 7.5$. These are not the same number, so `mean_2` is not always equal to `mean_1`. We can rule out "Yes" as an option.
- Suppose Section A has 2 students where one has 5 followers and one has 7, and Section B has 2 students where one has 3 followers and one has 15 followers. Then, the overall mean is $\frac{5 + 7 + 3 + 13}{4} = \frac{28}{4} = 7$, while the mean of the means is $\frac{\frac{5+7}{2} + \frac{3 + 13}{2}}{2} = \frac{6 + 8}{2} = 7$. If you experiment (or even write out a full proof), you'll note that as long as Sections A and B have the same number of students, the overall mean number of followers across their two sections is equal to the mean of their section-specific mean numbers of followers. We can rule out "No" as an option.
- Suppose Section A has 2 students who both have 10 followers, and Section B has 3 students who both have 10 followers. Then, the overall mean is 10, and so is the mean of means. So, it's possible for there to be a different number of students in Sections A and B and for `mean_2` to be equal to `mean_1`. It's not always, true, though, which is why the answer is "Yes, if both sections have the same number of students, otherwise maybe" and we can rule out the "otherwise no" case.

<average>15</average>

<br><br>

**Is `mean_3` is equal to `mean_1`? Yes.**

Let's break down the calculations:

- For `X`: `survey.groupby("Section").sum().get("IG Followers")` calculates the total number of followers for each section separately. The subsequent `.sum()` then adds these totals together, providing the total number of followers in the entire class.
- For `Y`: `survey.groupby("Section").count().get("IG Followers")` counts the number of students in each section. The subsequent `.sum()` then aggregates these counts, giving the total number of students in the entire class.

Then, `mean_3 = X / Y` divides the total number of Instagram followers by the total number of students to get the overall average number of followers per student for the entire dataset. This is precisely how `mean_1` is calculated. Hence, `mean_3` and `mean_1` will always be equal, so the answer is "Yes."

<average>58</average>

# END SOLUTION

# END SUBPROB

# END PROB