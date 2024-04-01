# BEGIN PROB

*Does an ice cream shop sell more chocolate or vanilla ice cream cones?*

Choose the best data science tool to help you answer this question.

( ) hypothesis testing
( ) permutation (A/B) testing
( ) Central Limit Theorem
( ) regression

# BEGIN SOLUTION

**Answer: ** hypothesis testing

The question at hand is dealing with differences between sales of different flavors of ice cream, which is the same thing as the total of ice cream cones sold. We can use hypothesis testing to test our null hypothesis that the count of Vanilla cones sold is higher than Chocolate, and our alternative hypothesis that the count of Chocolate cones sold is more than Vanilla. A permutation test is not suitable here because we are not comparing any numerical quantity associated with each group. A permutation test could be used to answer questions like "Are chocolate ice cream cones more expensive than vanilla ice cream cones?" or "Do chocolate ice cream cones have more calories than vanilla ice cream cones?", or any other question where you are tracking a number (cost or calories) along with each ice cream cone. In our case, however, we are not tracking a number along with each individual ice cream cone, but instead tracking a total of ice cream cones sold.

An analogy to this hypothesis test can be found in the "fair or unfair coin" problem in Lectures 20 and 21, where our null hypothesis is that the coin is fair and our alternative hypothesis is that the coin is unfair. The "fairness" of the coin is not a numerical quantity that we can track with each individual coin flip, just like how the count of ice cream cones sold is not a numerical quantity that we can track with each individual ice cream cone.

<average>57</average>

# END SOLUTION

# END PROB
