# BEGIN PROB

In a board game, whenever it is your turn, you roll a six-sided die and move that number of spaces. You get 10 turns, and you win the game if you’ve moved 50 spaces in those 10 turns. Suppose you create a simulation, based on 10,000 trials, to show the distribution of the number of spaces moved in 10 turns. Let’s call this distribution *Dist<sub>10</sub>*. You also wonder how the game would be different if you were allowed 15 turns instead of 10, so you create another simulation, based on 10,000 trials, to show the distribution of the number of spaces moved in 15 turns, which we’ll call *Dist<sub>15</sub>*
# BEGIN SUBPROB

What can we say about the shapes of *Dist<sub>10</sub>* and *Dist<sub>15</sub>*?

( ) both will be roughly normally distributed
( ) only one will be roughly normally distributed
( ) neither will be roughly normally distributed

# BEGIN SOLUTION

**Answer: ** both will be roughly normally distributed

By the central limit theorem, both simulations will appear to be roughly normally distributed. 

<average>90</average>
# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

What can we say about the centers of *Dist<sub>10</sub>* and *Dist<sub>15</sub>*?

( ) both will have approximately the same mean
( ) the mean of *Dist<sub>10</sub>* will be smaller than the mean of *Dist<sub>15</sub>*
( ) the mean of *Dist<sub>15</sub>* will be smaller than the mean of *Dist<sub>10</sub>*
# BEGIN SOLUTION

**Answer: ** the mean of *Dist<sub>10</sub>* will be smaller than the mean of *Dist<sub>15</sub>*

The distribution which moves in 10 turns will have a smaller mean as there are less turns to move spaces. Therefore,
the mean movement from turns will naturally be higher for the distribution with more turns. 

<average>83</average>
# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

What can we say about the spread of *Dist<sub>10</sub>* and *Dist<sub>15</sub>*?

( ) both will have approximately the same standard deviation
( ) the standard deviation of *Dist<sub>10</sub>* will be smaller than the standard deviation of *Dist<sub>15</sub>*
( ) the standard deviation of *Dist<sub>15</sub>* will be smaller than the standard deviation of *Dist<sub>10</sub>*
# BEGIN SOLUTION

**Answer: ** the standard deviation of *Dist<sub>10</sub>* will be smaller than the standard deviation of *Dist<sub>15</sub>*

Since taking more turns allows for more possible values, the spread of *Dist<sub>10</sub>* will be smaller than the standard deviation of *Dist<sub>15</sub>*. (ie. consider the possible range of values that are attainable for each case)
<average>65</average>
# END SOLUTION

# END SUBPROB

# END PROB
