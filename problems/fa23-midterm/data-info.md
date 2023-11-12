An area's cost of living describes how expensive it is to live in that
area. In this exam, we'll work with the DataFrame `living_cost`, which
describes the typical cost of living for different types of families
across all 3143 counties in the 50 United States. The first few rows
of `living_cost` are shown below, but `living_cost` has **many more
rows** than shown.

<center><img src='../assets/images/fa23-midterm/living_cost_preview.jpg' width=800></center>

<br>

Two counties in the same state will never have the same name, but as
the last two rows above illustrate, there are some counties in different
states with the same name, like Lee County.

The `"family_type"` column uses a code to describe the number of adults
and children in a family. For example, a value of `"2a1c"` represents
families with two adults and one child. There are ten unique values, as
follows: `"1a0c"`, `"1a1c"`, `"1a2c"`, `"1a3c"`, `"1a4c"`, `"2a0c"`,
`"2a1c"`, `"2a2c"`, `"2a3c"`, `"2a4c"`. We will assume that **all
families fall into one of these ten categories**, and **all ten family
structures are present in each US county**.

Each of the 31430 rows of the DataFrame represents a unique
combination of `"state"`, `"county"`, and `"family_type"`. As a result,
there will be more than one row with a `"state"` of `"CA"` and a
`"county"` of `"San Diego"`, corresponding to different values of
`"family_type"`. Similarly, there will be many rows such that
`"family_type"` is `"2a1c"`, all corresponding to different counties.
There is **only one row**, however, where `"state"` is `"CA"`,
`"county"` is `"San Diego"`, and `"family_type"` is `"1a2c"`

In addition to the `"state"`, `"county"`, and `"family_type"` columns,
`living_cost` includes the following columns.

-   `"is_metro"` (`bool`): `True` if the county is part of a metropolitan
    (urban) area, `False` otherwise. This value is the same for all rows
    of the DataFrame corresponding to the same county and state.
-   `"avg_housing_cost"` (`int`): The average yearly cost of housing, in
    dollars, for families of the given size in the given county and
    state.
-   `"avg_childcare_cost"` (`int`): The average yearly cost of childcare,
    in dollars, for families of the given size in the given county and
    state.
-   `"median_income"` (`int`): The median annual income, in dollars, for
    families of the given size in the given county and state.

**Throughout the exam**, assume we have already run
`import babypandas as bpd` and `import numpy as np`.