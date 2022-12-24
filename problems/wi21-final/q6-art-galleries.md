# BEGIN PROB

Suppose you have a dataset of 29 art galleries that includes the number of pieces of art in each gallery. 

A histogram of the number of art pieces in each gallery, as well as the code that generated it, is shown below.

<center><img src='../assets/images/wi21-final/art-galleries.png' width=70%></center>

# BEGIN SUBPROB

How many galleries have at least 80 but less than 100 art pieces? Input your answer below. Make sure your answer is an integer and does not include any text or symbols.

# BEGIN SOLUTION

**Answer: ** 7

Through looking at the graph we can find the total number of art galleries by taking 0.012 (height of bin) * 20 (the size of the bin) * 29 (total number of art galleries).
This will yield an anwser of 6.96 which should be rounded to the nearest integer (7).

<average>94</average>
# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

If we added to our dataset two more art galleries, each containing 24 pieces of art, and plotted the histogram again for the larger dataset, what would be the height of the bin `[20,45)`? Input your answer as a number rounded to **six decimal places**.

# BEGIN SOLUTION

**Answer: ** 0.007742

Taking the area of the bin `[20,45]` we can find the number of art galleries already within this bin 0.0055 * 25  = 0.1375 (estimation based on the visualization).
To find the number take this proportion x the total number of art galleries. 0.1375 * 29 = about 4 art galleries. If we add
two art galleries to this total we get 4 art galleries in the `[20,45]` bin to get 6 art galleries. To find the frequency of 6 art
galleries to the entire data set we can take 6/31. Note that the question asks for the *height* of the bin. Therefore, we can 
take (6/31) / 25 due to the size of the bin which will give an answer of 0.007742 upon rounding to six decimal places. 

<average>66</average>
# END SOLUTION

# END SUBPROB

# END PROB
