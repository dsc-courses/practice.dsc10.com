# BEGIN PROB

Suppose Tiffany has a random sample of dogs. Select the most
appropriate technique to answer each of the following questions using
Tiffany's dog sample.

# BEGIN SUBPROB

Do small dogs typically live longer than medium and large dogs?

( ) Standard hypothesis test
( ) Permutation test
( ) Bootstrapping

# BEGIN SOLUTION

**Answer: ** Option 2: Permutation test.

We have two parameters: dog size and life expectancy. Here if there was no significant statistical difference between the life expectancy of different dog sizes, randomly assigning our sampled life expectancy to each dog should lead us to observe similar observations to the observed statistic. Thus using a permutation test to comapre the two groups makes the most sense. We're not really trying to estimate a spcecific value so bootstrapping isn't a good idea here. Also, there's not really a good way to randomly generate life expectancies so a hypothesis test is not a good idea here. 

<average>77</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Does Tiffany's sample have an even distribution of dog kinds?

( ) Standard hypothesis test
( ) Permutation test
( ) Bootstrapping

# BEGIN SOLUTION

**Answer: ** Option 1: Standard hypothesis test.

We're not really comparing a variable between two groups, but rather looking at the overall distribution, so Permutation testing wouldn't work too well here. Again, we're not really trying to estimate anything here so bootstrapping isn't a good idea. This leaves us with the Standard Hypothesis Test, which makes sense if we use Total Variation Distance as our test statistic.

<average>51</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

What's the median weight for herding dogs?

( ) Standard hypothesis test
( ) Permutation test
( ) Bootstrapping

# BEGIN SOLUTION

**Answer: ** Option 3: Bootstrapping

Here we're trying to determine a specific value, which immediately leads us to bootstrapping. The other two tests wouldn't really make sense in this context.

<average>83</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Do dogs live longer than 12 years on average?

( ) Standard hypothesis test
( ) Permutation test
( ) Bootstrapping

# BEGIN SOLUTION

**Answer: ** Option 3: Bootstrapping

While the wording here might throw us off, we're really just trying to determine the average life expectancy of dogs, and then see how that compares to 12. This leads us to bootstrapping since we're trying to determine a specific value. The other two tests wouldn't really make sense in this context.

<average>43</average>

# END SOLUTION

# END SUBPROB

# END PROB
