# BEGIN PROB

The HAUGA bedroom furniture set includes two items, a bed frame and a bedside table. Suppose the amount of time it takes someone to assemble the bed frame is a random quantity drawn from the probability distribution below.

<center>
<table class="table" style="width:30%">
  <thead>
    <tr>
      <th scope="col">Time to assemble bed frame</th>
      <th scope="col">Probability</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">10 minutes</th>
      <td>0.1</td>
    </tr>
    <tr>
      <th scope="row">20 minutes</th>
      <td>0.4</td>
    </tr>
    <tr>
      <th scope="row">30 minutes</th>
      <td>0.5</td>
    </tr>
  </tbody>
</table>
</center>

Similarly, the time it takes someone to assemble the bedside table is a random quantity, independent of the time it takes them to assemble the bed frame, drawn from the probability distribution below.

<center>
<table class="table" style="width:30%">
  <thead>
    <tr>
      <th scope="col">Time to assemble bedside table</th>
      <th scope="col">Probability</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">30 minutes</th>
      <td>0.3</td>
    </tr>
    <tr>
      <th scope="row">40 minutes</th>
      <td>0.4</td>
    </tr>
    <tr>
      <th scope="row">50 minutes</th>
      <td>0.3</td>
    </tr>
  </tbody>
</table>
</center>

# BEGIN SUBPROB

What is the probability that Stella assembles the bed frame in 10 minutes if we know it took her less than 30 minutes to assemble? Give your answer as a decimal between 0 and 1.

# BEGIN SOLUTION

**Answer: ** 0.2

We want to find the probability that Stella assembles the bed frame in 10 minutes, given that she assembles it in less than 30 minutes. The multiplication rule can be rearranged to find the conditional probability of one event given another.

$$\begin{aligned} 
        P(A \text{ and } B) &= P(A \text{ given } B)*P(B)\\
        P(A \text{ given } B) &= \frac{P(A \text{ and } B)}{P(B)}
\end{aligned}$$

Let's, therefore, define events $A$ and $B$ as follows:

- $A$ is the event that Stella assembles the bed frame in 10 minutes.
- $B$ is the event that Stella assembles the bed frame in less than 30 minutes.

Since 10 minutes is less than 30 minutes, $A \text{ and } B$ is the same as $A$ in this case. Therefore, $P(A \text{ and } B) = P(A) = 0.1$. 

Since there are only two ways to complete the bed frame in less than 30 minutes (10 minutes or 20 minutes), it is straightforward to find $P(B)$ using the addition rule $P(B) = 0.1 + 0.4$. The addition rule can be used here because assembling the bed frame in 10 minutes and assembling the bed frame in 20 minutes are mutually exclusive. We could alternatively find $P(B)$ using the complement rule, since the only way not to complete the bed frame in less than 30 minutes is to complete it in exactly 30 minutes, which happens with a probability of 0.5. We'd get the same answer, $P(B) = 1 - 0.5 = 0.5$.

Plugging these numbers in gives our answer.

$$\begin{aligned} 
        P(A \text{ given } B) &= \frac{P(A \text{ and } B)}{P(B)}\\
                              &= \frac{0.1}{0.5}\\
                              &= 0.2
\end{aligned}$$

<average>72</average>
# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

What is the probability that Ryland assembles the bedside table in 40 minutes if we know that it took him 30 minutes to assemble the bed frame? Give your answer as a decimal between 0 and 1

# BEGIN SOLUTION

**Answer: ** 0.4

We are told that the time it takes someone to assemble the bedside table is a random quantity, *independent* of the time it takes them to assemble the bed frame. Therefore we can disregard the information about the time it took him to assemble the bed frame and read directly from the probability distribution that his probability of assembling the bedside table in 40 minutes is 0.4.
<average>82</average>
# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

What is the probability that Jin assembles the complete HAUGA set in at most 60 minutes? Give your answer as a decimal between 0 and 1.

# BEGIN SOLUTION

**Answer: ** 0.53

There are several different ways for the total assembly time to take at most 60 minutes:

1. The bed frame takes 10 minutes and the bedside table takes any amount of time.
2. The bed frame takes 20 minutes and the bedside table takes 30 or 40 minutes.
3. The bed frame takes 30 minutes and the bedside table takes 30 minutes.

Using the multiplication rule, these probabilities are:

1. $0.1*1 = 0.1$
2. $0.4*0.7 = 0.28$
3. $0.5*0.3 = 0.15$

Finally, adding them up because they represent mutually exclusive cases, we get $0.1+0.28+0.15 = 0.53$.
<average>58</average>
# END SOLUTION

# END SUBPROB

# END PROB