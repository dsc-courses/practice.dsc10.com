We are using (fictional) grading data from Quiz 3. Jeffrey and Kate each graded a random sample of DSC 10 submissions. The `grading` DataFrame has one row per graded submission with 50 rows total (25 per grader). The columns are: `"grader"` (str, either `"Jeffrey"` or `"Kate"`), `"score"` (int, score between 0 and 100), and `"submission_id"` (int, unique ID). The first few rows of `grading` are shown below.

<center><img src="../assets/images/wi26-quizzes/quiz4_data-info.png" width=600></center>

After examining the difficulty of the last DSC 10 quiz, expert detective and professor Peter has deduced that one of the two graders has been grading significantly harsher than the other.
