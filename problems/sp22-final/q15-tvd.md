# BEGIN PROB

There are 52 IKEA locations in the United States, and there are 50 states. 

Which of the following describes how to calculate the total variation distance between the distribution of IKEA locations by state and the uniform distribution?

( ) For each IKEA location, take the absolute difference between 1/50 and the number of IKEAs in the same state divided by the total number of IKEA locations. Sum these values across all locations and divide by two.
( ) For each IKEA location, take the absolute difference between the number of IKEAs in the same state and the average number of IKEAs in each state. Sum these values across all locations and divide by two.
( ) For each state, take the absolute difference between 1/50 and the number of IKEAs in that state divided by the total number of IKEA locations. Sum these values across all states and divide by two.
( ) For each state, take the absolute difference between the number of IKEAs in that state and the average number of IKEAs in each state. Sum these values across all states and divide by two.
( ) None of the above.

# BEGIN SOLUTION

**Answer: ** For each state, take the absolute difference between 1/50 and the number of IKEAs in that state divided by the total number of IKEA locations. Sum these values across all states and divide by two.

We're looking at the distribution across states. Since there are 50 states, the uniform distribution would correspond to having a fraction of 1/50 of the IKEA locations in each state. We can picture this as a sequence with 50 entries that are all the same:
$$(1/50, 1/50, 1/50, 1/50, \dots)$$

We want to compare this to the actual distribution of IKEAs across states, which we can think of as a sequence with 50 entries, representing the 50 states, but where each entry is the proportion of IKEA locations in a given state. For example, maybe the distribution starts out like this:
$$(3/52, 1/52, 0/52, 1/52, \dots)$$
We can interpret each entry as the number of IKEAs in a state divided by the total number of IKEA locations. Note that this has nothing to do with the average number of IKEA locations in each state, which is 52/50.

The way we take the TVD of two distributions is to subtract the distributions, take the absolute value, sum up the values, and divide by 2. Since the entries represent states, this process aligns with the given answer.

<average>30</average>
# END SOLUTION

# END PROB