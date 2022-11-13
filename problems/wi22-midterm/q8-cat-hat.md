# BEGIN PROB

While they are not skyscrapers, New Sixth College at UCSD has four relatively tall residential buildings, which we'll call Building A, Building B, Building C, and Building D. Suppose each building has 10 floors.

Sixth College administration decides to ease the General Education requirements for a few randomly selected students. Here's their strategy:

- **Wave 1:** Select, at random, one floor from each building.
- **Wave 2:** Select, at random, one of the four floors that was selected in Wave 1.

Everyone on one of the four floors selected in Wave 1 has the CAT 1 requirement waived. Everyone on the one floor selected in Wave 2 has both the CAT 1 and CAT 2 requirements waived.

# BEGIN SUBPROB

Billy lives on the 8th floor of Building C. What's the probability that Billy has both the CAT 1 and CAT 2 requirements waived? Give your answer as a proportion between 0 and 1, rounded to 3 decimal places.

# BEGIN SOLN

**Answer:** 0.025

In order for the 8th floor of Building C to be selected, two things need to happen:

- In Wave 1, the 8th floor of Building C needs to be selected amongst all 10 floors in Building C – this happens with probability $\frac{1}{10}$, since each floor in Building C is equally likely to be selected.
- In Wave 2, the 8th floor of Building C needs to be selected amongst the 4 floors selected in Wave 1 – this happens with probability $\frac{1}{4}$, since each floor in Wave 1 is equally likely to be selected.

Since **both** events need to occur, and both events are independent (think of selecting in each wave as drawing names from a hat), the probability that both occur is the product of the probabilities that they occur individually:

$$\frac{1}{10} \cdot \frac{1}{4} = \frac{1}{40} = 0.025$$

<average>80</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

What's the probability that **at least one** of the top (10th) floors of all four buildings are selected in Wave 1?

Give your answer as a proportion between 0 and 1, rounded to 3 decimal places.

# BEGIN SOLN

**Answer:** 0.344

Whenever we are asked to compute the probability of "at least one" occurrence of some event, it is almost always easiest to compute the **complement** of (i.e. "1 minus") the probability that there are no occurrences of the event. That is the case here; as such, we need to compute the probability that none of the 10th floors are selected across all four buildings.

To compute the probability that none of the 10th floors are selected across all four buildings, we first need to find the probability that the 10th floor is not selected in just a single building. This is $1 - \frac{1}{10} = \frac{9}{10}$. Then, since the selections in each building are independent of other buildings, the probability that none of the 10th floors are selected across all four buildings is $\left( \frac{9}{10} \right)^4$.

Lastly, the probability we are asked for is the complement of the probability we just computed. So, the probability that at least one 10th floor is selected across all four buildings is

$$1 - \left( 1 - \frac{1}{10} \right)^4 = 1 - \left( \frac{9}{10} \right)^4 = 1 - 0.6561 = 0.3439$$

This rounds to 0.344.

<average>64</average>

# END SOLN

# END SUBPROB

# END PROB