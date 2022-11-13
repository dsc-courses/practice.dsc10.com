# BEGIN PROB

The data visualization below shows all Olympic gold medals for women’s gymnastics, broken down by the age of the gymnast. 

<center><img src='../assets/images/wi21-final/gymnastics.png' width=50%></center>

# BEGIN SUBPROB

Based on this data, rank the following three quantities in **ascending** order: the median age at which gold medals are earned, the mean age at which gold medals are earned, the standard deviation of the age at which gold medals are earned.

( ) mean, median, SD
( ) median, mean, SD
( ) SD, mean, median
( ) SD, median, mean
# BEGIN SOLUTION

**Answer: ** SD, median, mean

The standard deviation will clearly be the smallest of the three values as most of the data is encompassed
between the range of `[14-26]`. Intuitively, the standard deviation will have to be about a third of this range
which is around 4 (though this is not the exact standard deviation, but is clearly much less than the mean
and median with values closer to 19-25). Comparing the median and mean, it is important to visualize that this 
distribution is skewed right. When the data is skewed right it pulls the mean towards a higher value (as the higher values
naturally make the average higher). Therefore, we know that the mean will be greater than the median and the ranking is 
SD, median, mean. 
<average>72</average>
# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Which of the following is larger for this dataset?

( ) the difference between the 50th percentile of ages and the 25th percentile of ages
( ) the difference between the 75th percentile of ages and the 50th percentile of ages
( ) both are the same
# BEGIN SOLUTION

**Answer: ** the difference between the 75th percentile of ages and the 50th percentile of ages

Since the distribution is right skewed, the 75th percentile will have a larger difference from the 50th percentile than the
25th percentile. With right skewness, values above the 50th percentile will be more different than those smaller than the 50th 
percentile (and thus more spread out according to the graph). 
<average>78</average>
# END SOLUTION

# END SUBPROB

# END PROB
