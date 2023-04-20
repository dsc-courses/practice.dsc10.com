Credit cards allow consumers to make purchases by borrowing money and paying it back later. Credit card companies are wary of granting this borrowing ability to consumers who may not be able to pay back their debt. Therefore, potential credit card carriers must submit an application that contains information about themselves and their history of paying back debt. 

The DataFrame `apps` contains application data for a random sample of 1,000 applicants for a particular credit card from the 1990s. The columns are:

-   `"status" (str)`: Whether the credit card application was approved:
    `"approved"` or `"denied"` values only.

-   `"age" (float)`: The applicant's age, in years, to the nearest
    twelfth of a year.

-   `"income" (float)`: The applicant's annual income, in tens of
    thousands of dollars.

-   `"homeowner" (str)`: Whether the credit card applicant owns their
    own home: `"yes"` or `"no"` values only.

-   `"dependents" (int)`: The number of dependents, or individuals that
    rely on the applicant as a primary source of income, such as
    children.

The first few rows of `apps` are shown below, though remember that
`apps` has 1,000 rows.

<center><img src='../assets/images/fa22-final/apps.jpg' width=45%></center>
<br>

**Throughout this exam, we will refer to `apps` repeatedly.**

Assume that:

-   Each applicant only submitted a single application.

-   We have already run `import babypandas as bpd` and
    `import numpy as np`.

**Tip:** Open this page in another tab, so that it is easy to refer to this data description as you work through the exam.