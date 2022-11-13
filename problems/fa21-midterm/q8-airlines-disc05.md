# BEGIN PROB

Suppose you are booking a flight and you have no control over which airline you fly on. Below is a table with multiple airlines and the probability of a flight being on a specific airline. 


<center>
<table class="table" style="width:20%">
  <thead>
    <tr>
      <th scope="col">Airline</th>
      <th scope="col">Chance</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Delta</th>
      <td>0.4</td>
    </tr>
    <tr>
      <th scope="row">United</th>
      <td>0.3</td>
    </tr>
    <tr>
      <th scope="row">American</th>
      <td>0.2</td>
    </tr>
    <tr>
      <th scope="row">All other airlines</th>
      <td>0.1</td>
    </tr>
  </tbody>
</table>
</center>

The airline for one flight has no impact on the airline for another flight.

For this question, suppose that you schedule 3 flights for January 2022.

# BEGIN SUBPROB

What is the probability that all 3 flights are on United? Give your answer as an **exact** decimal between 0 and 1 (not a Python expression).

# BEGIN SOLUTION

**Answer: ** 0.027

For all three flights to be on United, we need the first flight to be on United, and the second, and the third. Since these are independent events that do not impact one another, and we need all three flights to separately be on United, we need to multiply these probabilities, giving an answer of $0.3*0.3*0.3 = 0.027$.

Note that on an exam without calculator access, you could leave your answer as $(0.3)^3$.

<average>93</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

What is the probability that all 3 flights are on Delta, or all on United, or all on American? Give your answer as an **exact** decimal between 0 and 1 (not a Python expression).

# BEGIN SOLUTION

**Answer: ** 0.099

We already calculated the probability of all three flights being on United as $(0.3)^3 = 0.027$. Similarly, the probability of all three flights being on Delta is $(0.4)^3 = 0.064$, and the probability of all three flights being on American is $(0.2)^3 = 0.008$. Since we cannot satisfy more than one of these conditions at the same time, we can separately add their probabilities to find a total probability of $0.027 + 0.064 + 0.008 = 0.099$.

<average>76</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

True or False: The probability that all 3 flights are on the same airline is equal to the probability you computed in the previous subpart.

( ) True
( ) False

# BEGIN SOLUTION

**Answer: ** False

It's not quite the same because the previous subpart doesn't include the probability that all three flights are on the same airline which is not one of Delta, United, or American. For example, there is a small probability that all three flights are on Allegiant or all three flights are on Southwest. 

<average>90</average>

# END SOLUTION

# END SUBPROB

# END PROB
