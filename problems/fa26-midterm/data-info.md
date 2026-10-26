Campuswire is an online discussion forum used by many college courses, including DSC 10. Students and instructional staff use it to ask questions, share announcements, and discuss course material.

The DataFrame `posts` has one row for every post made on a course's Campuswire forum. The columns are:

- `"post_id"` (`int`): A unique ID number for the post.
- `"title"` (`str`): The title of the post.
- `"date"` (`str`): The date the post was made, formatted as `"YYYY-MM-DD"`, for example `"2026-02-03"`.
- `"author_role"` (`str`): The role of the author, either `"student"` or `"staff"`.
- `"category"` (`str`): The category the post was filed under, such as `"General"`, `"Quiz 1"`, `"Projects"`, or `"Homework 3"`.
- `"is_private"` (`bool`): `True` if the post is visible only to the author and course staff, and `False` if it is visible to the whole class.
- `"is_question"` (`bool`): `True` if the post is a question, and `False` if it is a note (such as an announcement or reminder).
- `"is_resolved"` (`bool`): `True` if the post has been marked as resolved, and `False` otherwise.
- `"num_views"` (`int`): The number of times the post has been viewed.
- `"num_likes"` (`int`): The number of likes the post has received.
- `"num_comments"` (`int`): The number of comments on the post.

The first few rows of `posts` are shown below, though `posts` has many more rows than pictured.

<center><img src="../assets/images/fa26-midterm/cw.png" width="100%"></center> \

Throughout this exam, we will refer to `posts` repeatedly. Assume that we have already run `import babypandas as bpd` and `import numpy as np`.
