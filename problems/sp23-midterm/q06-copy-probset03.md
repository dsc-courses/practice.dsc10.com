# BEGIN PROB

Suppose there are 200 students enrolled in DSC 10, and that the histogram below displays the distribution of the number of Instagram
followers each student has, measured in 100s. That is, if a student is
represented in the first bin, they have between 0 and 200 Instagram
followers.

<center><img src='../assets/images/sp23-midterm/histogram.png' width=60%></center>
<br>

# BEGIN SUBPROB

How many students in DSC 10 have between 200 and 800 Instagram
followers? Give your answer as an integer.

# BEGIN SOLUTION

**Answer**: 90

Remember, the key property of histograms is that the proportion of values in a bin is equal to the area of the corresponding bar. To find the number of values in the range 2-8 (the $x$-axis is measured in hundreds), we'll need to find the proportion of values in the range 2-8 and multiply that by 200, which is the total number of students in DSC 10. To find the proportion of values in the range 2-8, we'll need to find the areas of the 2-4, 4-6, and 6-8 bars.

Area of the 2-4 bar: $\text{width} \cdot \text{height} = 2 \cdot 0.1 = 0.2$

Area of the 4-6 bar: $\text{width} \cdot \text{height} = 2 \cdot 0.0625 = 0.125$.

Area of the 6-8 bar: $\text{width} \cdot \text{height} = 2 \cdot 0.0625 = 0.125$.

Then, the total proportion of values in the range 2-8 is $0.2 + 0.125 + 0.125 = 0.45$, so the total number of students with between 200 and 800 Instagram followers is $0.45 \cdot 200 = 90$.

<average>49</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Suppose the height of a bar in the above histogram is $h$. How many
students are represented in the corresponding bin, in terms of $h$?

*Hint: Just as in the first subpart, you'll need to use the assumption
from the start of the problem.*

( ) $20 \cdot h$
( ) $100 \cdot h$
( ) $200 \cdot h$
( ) $400 \cdot h$
( ) $800 \cdot h$

# BEGIN SOLUTION

**Answer**: $400 \cdot h$

As we said at the start of the last solution, the key property of histograms is that the proportion of values in a bin is equal to the area of the corresponding bar. Then, the number of students represented bar a bar is the total number of students in DSC 10 (200) multiplied by the area of the bar.

Since all bars in this histogram have a width of 2, the area of a bar in this histogram is $\text{width} \cdot \text{height} = 2 \cdot h$. If there are 200 students in total, then the number of students represented in a bar with height $h$ is $200 \cdot 2 \cdot h = 400 \cdot h$.

To verify our answer, we can check to see if it makes sense in the context of the previous subpart. The 2-4 bin has a height of $0.1$, and $400 \cdot 0.1 = 40$. The total number of students in the range 2-8 was 90, so it makes sense that 40 of them came from the 2-4 bar, since the 2-4 bar takes up about half of the area of the 2-8 range.

<average>36</average>

# END SOLUTION

# END SUBPROB

# END PROB