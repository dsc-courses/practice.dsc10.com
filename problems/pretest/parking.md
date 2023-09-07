# BEGIN PROB

You plan to drive to campus for your Monday, Wednesday, Friday classes and you are interested in knowing how many parking spaces are available in each of three parking structures (Gilman, Hopkins, and Pangea).  We'll assume for this problem that these are the only three parking options available. The table below shows how many unoccupied spaces there are in each parking structure at 10am on Monday, Wednesday, and Friday of Week 1.

|           | Gilman | Hopkins | Pangea |  
|-----------|--------|---------|--------|
| Monday    | 180    | 840     | 190    |
| Wednesday | 150    | 850     | 200    |
| Friday    | 165    | 835     | 220    |

# BEGIN SUBPROB

What proportion of available spaces on Wednesday are in Gilman? Fully simplify your answer without using a calculator and without performing long division. 

# BEGIN SOLUTION

**Answer**: $\frac{1}{8}$

There are $150 + 850 + 200 = 1200$ available parking spaces on Wednesday. 150 of these are in Gilman. So the proportion we're looking for is $\frac{150}{1200}$. To simplify this, we look for common factors in the numerator and denominator. Both 150 and 1200 end in 0, which means they are both divisible by 10. If we cancel out the common factor of 10 from the numerator and denominator, we can simplify the proportion to $\frac{15}{120}$. This can be further simplified. Since 15 has factors of 3 and 5, let's look for factors of those numbers in the denominator of 120. It turns out that both are factors, but suppose we first notice that 3 is a factor of 120. This simplifies the proportion to $\frac{15}{120} = \frac{5}{40}$. Then we could notice that 40 is a multiple of 5, and simplify the proportion to $\frac{1}{8}$.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

On average, Gilman is 80% full at 10am on Monday, Wednesday, and Friday of Week 1. What is the capacity of Gilman? Solve this problem without a calculator.

# BEGIN SOLUTION

**Answer**: 825

First, we use the Gilman column of the table to compute that on average, there are 165 available spaces. We can compute this average quickly without calculation by noticing that 150 and 180 are both equally far from 165 on a number line, so the average of 180, 150, and 165 must be 165. Since 80% of Gilman is full on average, this means 20% of Gilman is not full on average. We have figured out that 20% of capacity is 165 parking spaces, which we can write as $0.2x = 165$, or equivalently, $\frac{1}{5}x = 165$, where $x$ is the capacity of Gilman. Writing 0.2 as the fraction $\frac{1}{5}$ makes it easier to solve for $x$ by hand without a calculator. We can solve for $x$ by multiplying both sides by 5, so the answer is $165 \cdot 5$, which can do using long multiplication to get 825. 

If we want to avoid using long multiplication, we can use a trick: to multiply by five, multiply by ten and divide by two, both of which are pretty easy to do. $165 \cdot 10 = 1650$ and half of that is 825. So, there are 825 parking spaces in Gilman.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

On Monday, the percentage of occupied spaces in Pangea is twice the percentage of occupied spaces in Hopkins. If Pangea has 950 parking spaces, how many parking spaces does Hopkins have? You may use a calculator for this part.

# BEGIN SOLUTION

**Answer**: 1400

Let's start with Pangea since we know more information about that facility. On Monday, 190 out of 950 parking spaces in Pangea are available, which means $950 - 190 = 760$ parking spaces are occupied. The percentage of occupied spaces in Pangea is $\frac{760}{950} \cdot 100\% = 80\%$. We're told that is twice the percentage of occupied spaces in Hopkins, so that means Hopkins must be 40% full. There are 840 available spaces in Hopkins on Monday. Since Hopkins is 40% full, these 840 unoccupied spaces correspond to the remaining 60% of spaces in Hopkins. If $x$ is the capacity of Hopkins, we have $0.6x = 840$. We can solve for $x$ by dividing both sides by 0.6 to obtain $x = 1400$. So, there are 1400 parking spaces in Hopkins.

# END SOLUTION

# END SUBPROB

# END PROB