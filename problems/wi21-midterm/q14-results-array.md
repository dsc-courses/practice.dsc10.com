# BEGIN PROB

```py
results = np.array([])
for i in np.arange(10):
    result = np.random.choice(np.arange(1000), replace=False)
    results = np.append(results, result)
```

After this code executes, `results` contains:

( ) a simple random sample of size 9, chosen from a set of size 999 with replacement
( ) a simple random sample of size 9, chosen from a set of size 999 without replacement
( ) a simple random sample of size 10, chosen from a set of size 1000 with replacement
( ) a simple random sample of size 10, chosen from a set of size 1000 without replacement

# BEGIN SOLUTION

**Answer: ** a simple random sample of size 10, chosen from a set of size 1000 with replacement

Let's see what the code is doing. The first line initializes an empty array called `results`. The for loop runs 10 times. Each time, it creates a value called `result` by some process we'll inspect shortly and appends this value to the end of the `results` array. At the end of the code snippet, `results` will be an array containing 10 elements.

Now, let's look at the process by which each element `result` is generated. Each `result` is a random element chosen from `np.arange(1000)` which is the numbers from 0 to 999, inclusive. That's 1000 possible numbers. Each time `np.random.choice` is called, just one value is chosen from this set of 1000 possible numbers. 

When we sample just one element from a set of values, sampling with replacement is the same as sampling without replacement, because sampling with or without replacement concerns whether subsequent draws can be the same as previous ones. When we're just sampling one element, it really doesn't matter whether our process involves putting that element back, as we're not going to draw again!

Therefore, `result` is just one random number chosen from the 1000 possible numbers. Each time the `for` loop executes, `result` gets set to a random number chosen from the 1000 possible numbers. It is possible (though unlikely) that the random `result` of the first execution of the loop matches the `result` of the second execution of the loop. More generally, there can be repeated values in the `results` array since each entry of this array is independently drawn from the same set of possibilities. Since repetitions are possible, this means the sample is drawn with replacement.

Therefore, the `results` array contains a sample of size 10 chosen from a set of size 1000 with replacement. This is called a "simple random sample" because each possible sample of 10 values is equally likely, which comes from the fact that `np.random.choice` chooses each possible value with equal probability by default.

<average>11</average>
# END SOLUTION

# END PROB