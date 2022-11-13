# BEGIN PROB

You sample from a population by assigning each element of the population a number starting with 1. You include element 1 in your sample. Then you generate a random number, `n`, between 2 and 5, inclusive, and you take every `n`th element after element 1 to be in your sample. For example, if you select `n=2`, then your sample will be elements `1, 3, 5, 7`, and so on.

# BEGIN SUBPROB

**True or False**: Before the sample is drawn, you can calculate the probability of selecting each subset of the population.

# BEGIN SOLUTION

**Answer: ** True

The answer is true since someone can easily sketch each sample to view the probability of selecting
a certain subset. For example, when n = 2 we know the elements are 1, 3, 5, 7, and so on. Similarly we know
this information for n = 3, 4 and 5. Using this information we could calculate the probability of selecting a subset.

<average>97</average>
# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

**True or False**: Each subset of the population is equally likely to be selected.

# BEGIN SOLUTION

**Answer: ** False

No, each subset of the population is not equally likely to be selected since the element assigned
as element 1 will always be selected due to the way sampling is conducted as defined in the question. 
That is, the question says we always include element one in the sample which will over represent it in samples
as compared to other parts of the population. 

<average>46</average>
# END SOLUTION

# END SUBPROB

# END PROB
