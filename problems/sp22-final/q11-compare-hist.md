# BEGIN PROB

The histogram below shows the distribution of the number of products sold per day throughout the last 30 days, for two different IKEA products: the KURA reversible bed, and the ANTILOP highchair.

<center><img src='../assets/images/sp22-final/overlaidhist.png' width=40%></center>

# BEGIN SUBPROB

For how many days did IKEA sell between 20 (inclusive) and 30 (exclusive) KURA reversible beds per? Give an **integer** answer or write "not enough information", but **not both**.

# BEGIN SOLUTION

**Answer: ** 15

Remember that for a density histogram, the proportion of data that falls in a certain range is the area of the histogram between those bounds. So to find the proportion of days for which IKEA sold between 20 and 30 KURA reversible beds, we need to find the total area of the bins $[20, 25)$ and $[25, 30)$. Note that the left endpoint of each bin is included and the right bin is not, which works perfectly with needing to include 20 and exclude 30.

The bin $[20, 25)$ has a width of 5 and a height of about 0.047. The bin $[25, 30)$ has a width of 5 and a height of about 0.053. The heights are approximate by eye, but it appears that the $[20, 25)$ bin is below the horizontal line at 0.05 by the same amount which the $[25, 30)$ is above that line. Noticing this spares us some annoying arithmetic and we can calculate the total area as 

$$\begin{aligned} 
        \text{total area} &= 5*0.047 + 5*0.053 \\ 
        		    &= 5*(0.047 + 0.053) \\
        		    &= 5*(0.1) \\
        		    &= 0.5 
\end{aligned}$$

Therefore, the proportion of days where IKEA sold between 20 and 30 KURA reversible beds is 0.5. Since there are 30 days represented in this histogram, that corresponds to 15 days.

<average>54</average>
# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

For how many days did IKEA sell more KURA reversible beds than ANTILOP highchairs? Give an **integer** answer or write "not enough information", but **not both**.

# BEGIN SOLUTION

**Answer: ** not enough information

We cannot compare the number of KURA reversible beds sold on a certain day with the number of ANTILOP highchairs sold on the same day. These are two separate histograms shown on the same axes, but we have no way to associate data from one histogram with data from the other. For example, it's possible that on some days, IKEA sold the same number of KURA reversible beds and ANTILOP highchairs. It's also possible from this histogram that this never happened on any day.

<average>54</average>
# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Determine the relative order of the three quantities below.

1. The number of days for which IKEA sold at least 35 ANTILOP highchairs.
2. The number of days for which IKEA sold less than 25 ANTILOP highchairs.
3. The number of days for which IKEA sold between 10 (inclusive) and 20 (exclusive) KURA reversible beds.

( ) (1)<(2)<(3) 
( ) (1)<(3)<(2)
( ) (2)<(1)<(3)
( ) (2)<(3)<(1)
( ) (3)<(1)<(2)
( ) (3)<(2)<(1)

# BEGIN SOLUTION

**Answer: ** (2)<(3)<(1)

We can calculate the exact value of each of the quantities:

1. To find the number of days for which IKEA sold at least 35 ANTILOP highchairs, we need to find the total area of the rightmost three bins of the ANTILOP distribution. Doing a similar calculation to the one we did in Problem 11.1, 
$$\begin{aligned} 
        \text{total area} &= 5*0.053 + 5*0.02 + 5*0.007 \\ 
        		    &= 5*(0.08) \\
        		    &= 0.4
\end{aligned}$$
This is a proportion of 0.4 out of 30 days total, which corresponds to **12 days**.

1. To find the number of days for which IKEA sold less than 25 ANTILOP highchairs, we need to find the total area of the leftmost four bins of the ANTILOP distribution. We can do this in the same way as before, but to avoid the math, we can also use the information we've already figured out to make this easier. In Problem 11.1, we learned that the KURA distribution included 15 days total in the two bins $[20, 25)$ and $[25, 30)$. Since the $[25, 30)$ bin is just slightly taller than the $[20, 25)$ bin, these 15 days must be split as 7 in the  $[20, 25)$ bin and 8 in the $[25, 30)$ bin. Once we know the tallest bin corresponds to 8 days, we can figure out the number of days corresponding to every other bin just by eye. Anything that's half as tall as the tallest bin, for example, represents 4 days. The red lines on the histogram below each represent 1 day, so we can easily count the number of days in each bin.
<center><img src='../assets/images/sp22-final/overlaidhist-red.png' width=40%></center>
Therefore summing up the number of days from the 4 bins for which IKEA sold less than 25 ANTILOP highchairs gives $0 + 3 + 0 + 5 = 8$. Altogether, that's **8 days**.

1. To find the number of days for which IKEA sold between 10 and 20 KURA reversible beds, we simply need to add the number of days in the $[10, 15)$ and $[15, 20)$ bins of the KURA distribution. Using the histogram with the red lines makes this easy to calculate as $4+5$, or **9 days**.

Therefore since 8<9<12, the correct answer is (2)<(3)<(1).

<average>81</average>
# END SOLUTION

# END SUBPROB

# END PROB