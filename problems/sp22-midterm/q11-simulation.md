# BEGIN PROB

The fine print of the Sun God festival website says "Ticket does not guarantee entry. Venue subject to capacity restrictions."  RIMAC field, where the 2022 festival will be held, has a capacity of 20,000 people. Let’s say that UCSD distributes 21,000 tickets to Sun God 2022 because prior data shows that 5% of tickets distributed are never actually redeemed. Let’s suppose that each person with a ticket this year has a 5% chance of not attending (independently of all others).  What is the probability that at least one student who has a ticket cannot get in due to the capacity restriction? Fill in the blanks in the code below so that `prob_angry_student` evaluates to an approximation of this probability.

```py
num_angry = 0

for rep in np.arange(10000):
    # randomly choose 21000 elements from [True, False] such that 
    # True has probability 0.95, False has probability 0.05
    attending = np.random.choice([True, False], 21000, p=[0.95, 0.05])
    if __(a)__:
        __(b)__

prob_angry_student = __(c)__
```
# BEGIN SUBPROB

What goes in the **first** blank?

( ) `np.count_nonzero(attending) == 20001`
( ) `attending[20000] == False`
( ) `attending.sum() > 20000`
( ) `np.count_nonzero(attending) > num_angry`

# BEGIN SOLUTION

**Answer: ** `attending.sum() > 20000`

Let's look at the variable `attending`. Since we're choosing 21,000 elements from the list `[True, False]` and there are 21,000 tickets distributed, this code is randomly determining whether each ticket holder will actually attend the festival. There's a 95% chance of each ticket holder attending, which is reflected in the `p=[0.95, 0.05]` argument. Remember that `np.random.choice` returns an array of random choices, which in this case means it will contain 21,000 elements, each of which is `True` or `False`. 

We want to figure out the probability of at least one ticket holder showing up and not being admitted. Another way to say this is we want to find the probability that more than 20,000 ticket holders show up to attend the festival. The way we approximate a probability through simulation is we repeat a process many times and see how often some event occured. The event we're interested in this case is that more than 20,000 ticket holders came to Sun God. Since we have an array of `True` and `False` values corresponding to whether each ticket holder actually came, we just need to determine if there are more than 20,000 `True` values in the `attending` array. 

There are several ways to count the number of `True` values in a Boolean array. One way is to sum the array since in Python `True` counts as 1 and `False` counts as 0. Therefore, `attending.sum() > 20000` is the condition we need to check here.

<average>67</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

What goes in the **second** blank?

# BEGIN SOLUTION

**Answer: ** `num_angry = num_angry + 1`

Remember our goal in simulation is to repeat a process many times to see how often some event occurs. The repetition comes from the `for` loop which runs 10,000 times. Each time, we are simulating the process of 21,000 students each randomly deciding whether to show up to Sun God or not. We want to know, out of these 10,000 trials, how frequently more than 20,000 of the students will show up. So when this happens, we want to record that it happened. The standard way to do that is to keep a counter variable that starts at 0 and gets incremented, or increased by one, each time we had more than 20,000 attendees in our simulation. 

The framework to do this is already set up because a variable called `num_angry` is initialized to 0 before the `for` loop. This variable is our counter variable, meant to count the number of trials, out of 10,000, that resulted in at least one student being angry because they showed up to Sun God with a ticket and were denied entrance. So all we need to do when there are more than 20,000 `True` values in the `attending` array is increment this counter by one via the code `num_angry = num_angry + 1`, sometimes abbreviated as `num_angry += 1`.

<average>59</average>


# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

What goes in the **third** blank?

# BEGIN SOLUTION

**Answer: ** `num_angry/10000`

To calculate the approximate probability, all we need to do is divide the number of trials in which a student was angry by the total number of trials, which is 10,000.  

<average>68</average>


# END SOLUTION

# END SUBPROB

# END PROB
