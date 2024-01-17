Recall, at the start of the quarter, you were asked to complete a Welcome Survey to tell us about your background coming into the course. You were also asked to share seemingly irrelevant details, like the number of followers you have on Instagram and the number of unread emails in your primary email account. Well, those details are no longer irrelevant – in this exam, we will work with the data from this quarter's Welcome Survey!

Each row in the DataFrame `survey` represents one student in DSC 10. The information stored in the columns of `survey` are as follows:

- `"Section"` (`str`): The lecture section the student is enrolled in (either `"A"` or `"B"`).
- `"IG Followers"` (`int`): The number of followers the student has on Instagram. If the student does not have an Instagram account, this number is 0.
- `"Unread Emails"` (`int`): The number of unread emails in the student's primary email account.
- `"College"` (`str`): The college the student is a member of (either `"ERC"`, `"Marshall"`, `"Muir"`, `"Revelle"`, `"Seventh"`, `"Sixth"` or `"Warren"`).
- `"Major"` (`str`): The student's primary major, in major code form. For instance, the major code for the Data Science major is `"DS25"`.
- `"Class Standing"` (`str`): The student's class standing (either `"Freshman"`, `"Sophomore"`, `"Junior"`, or `"Senior"`).


The first few rows of `survey` are shown below, though `survey` has many more rows than are pictured below (since there are more than 5 students in DSC 10 this quarter).


<center><img src='../assets/images/sp23-midterm/df-preview.png' width=60%></center>
<br>

Assume that we have already run `import babypandas as bpd` and `import numpy as np`.
