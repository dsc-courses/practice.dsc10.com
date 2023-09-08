# BEGIN PROB

One of your classes this quarter, PTS 1: _Principles of Taylor Swift_, has the following grading scheme:

- 20% Midterm 1
- 20% Midterm 2
- 30% Homeworks (lowest homework dropped)
- 30% Final Exam

There are 4 homework assignments, but your lowest homework score is dropped from your overall grade calculation. Each homework assignment is worth the same amount in your overall grade calculation, even though they have different numbers of available points. Your scores on all parts of the course, before the Final Exam, are as follows:

- Midterm 1: $\frac{98}{100}$
- Midterm 2: $\frac{16}{38}$
- Homework 1: $\frac{3}{4}$
- Homework 2: $\frac{18}{25}$
- Homework 3: $\frac{9}{10}$
- Homework 4: $\frac{12}{13}$

What is the minimum possible score you can earn on the Final Exam, **as a percentage**, to guarantee that you finish with at least a B grade (80% overall) in PTS 1? You may use a calculator (tip: you can type arithmetic expressions into Google and it will perform calculations for you!).

# BEGIN SOLUTION

**Answer**: 87.5%

Let $f$ be your Final Exam score in PTS 1, as a decimal between 0 and 1. (We'll treat $f$ as a decimal because all of your other scores are provided to us as decimals, or fractions, as well.) If we knew $f$, we could calculate your overall grade right now:

$$20\% \cdot \text{Midterm 1} + 20\% \cdot \text{Midterm 2} + 30\% \cdot \text{Homeworks} + 30\% \cdot f$$

We don't know $f$, but we do know the other variables in the above expression. Your Midterm Exam scores are given to us directly, but your average score on homeworks, after dropping your lowest homework, requires a bit of calculation to find. First, we need to find which of the four homeworks you did the worst on, so that we can exclude it when calculating your average homework score. That happens to be Homework 2, which you scored a 72% on; we can find this without a calculator by noticing that $25 \cdot 4 = 100$, so $\frac{18}{25} = \frac{18 \cdot 4}{25 \cdot 4} = \frac{72}{100} = 72\%$. This is lower than Homework 1, which you scored a $\frac{3}{4} = 75\%$ on; Homework 3, which you scored a $\frac{9}{10} = 90\%$ on, and Homework 4, which you scored a $\frac{12}{13} = 92.3\%$ on ($\frac{12}{13}$ is a tough fraction to simplify without a calculator, but you don't need to, since has to be greater than $\frac{9}{10}$ which you know is 90%, and thus it has to be greater than 72%).

This means that the three homework scores that we're going to include in your average homework score calculation are $\frac{3}{4}$, $\frac{9}{10}$, and $\frac{12}{13}$. Note that we're using the fractional forms rather than something like 92.3% because there's no need to round at this stage. The average of these three fractions is $\frac{1}{3} \cdot \left(\frac{3}{4} + \frac{9}{10} + \frac{12}{13}\right)$; the result is your average homework score. We'll leave it like this for now so that you only need to put one (big) expression in the calculator.

Now that we have your average homework score, we know most parts of your overall grade:

$$20\% \cdot \frac{98}{100} + 20\% \cdot \frac{16}{38} + 30\% \cdot \frac{1}{3} \cdot \left(\frac{3}{4} + \frac{9}{10} + \frac{12}{13}\right) + 30\% \cdot f$$

Simplifying everything before $30\% \cdot f$ in a calculator gives us 53.75%. 

It's worth commenting on _how_ to evaluate such an expression in a calculator. It's easier to treat percentages, like 20%, as decimals, like 0.2, when using a calculator.
<a href="https://www.google.com/search?q=0.2+*+(98%2F100)+%2B+0.2+*+(16%2F38)+%2B+0.3+*+(3%2F4+%2B+9%2F10+%2B+12%2F13)+%2F+3&sourceid=chrome&ie=UTF-8" target="_blank">Here</a> you can see the exact expression we typed into a Google search (no need to use a physical calculator!); 0.5375... is the same as 53.75..%.

Now, we have that your overall grade is

$$53.75\% + 30\% \cdot f$$

We need to find the smallest value of $f$ such that your overall grade is at least 80%, or in other words, the smallest value of $f$ that satisfies the inequality

$$53.75\% + 30\% \cdot f \geq 80\%$$

Let's solve:

$$\begin{align*} 53.75\% + 30\% \cdot f &\geq 80\% \\ 30\% \cdot f &\geq 26.25\% \\ f &\geq \frac{26.25}{30} \\ f &\geq 0.875 \end{align*}$$

So, to earn a B in PTS 1, you'll need at least an 87.5% on the Final Exam. Good luck!

# END SOLUTION

# END PROB