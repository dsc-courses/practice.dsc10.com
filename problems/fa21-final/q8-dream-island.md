# BEGIN PROB

Each individual penguin in our dataset is of a certain species (Adelie, Chinstrap, or Gentoo) and comes from a particular island in Antarctica (Biscoe, Dream, or Torgerson). There are 330 penguins in our dataset, grouped by species and island as shown below.

<center><img src='../assets/images/fa21-final/dream_form.png' width=20%></center>
<br>

Suppose we pick one of these 330 penguins, uniformly at random, and name it Chester.

# BEGIN SUBPROB

What is the probability that Chester comes from Dream island? Give your answer as a number between 0 and 1, rounded to three decimal places. 

# BEGIN SOLUTION

**Answer:** 0.373

P(Chester comes from Dream island) = # of penguins in dream island $/$ # of all penguins in the data = $\frac{55+68}{330} \approx 0.373$

<average>94</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

If we know that Chester comes from Dream island, what is the probability that Chester is an Adelie penguin? Give your answer as a number between 0 and 1, rounded to three decimal places. 

# BEGIN SOLUTION

**Answer:** 0.447

P(Chester is an Adelie penguin given that Chester comes from Dream island) = # of Adelie penguins from Dream island $/$ # of penguins from Dream island = $\frac{55}{55+68} \approx 0.447$

<average>91</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

If we know that Chester is not from Dream island, what is the probability that Chester is not an Adelie penguin? Give your answer as a number between 0 and 1, rounded to three decimal places. 

# BEGIN SOLUTION

**Answer:** 0.575

Method 1

P(Chester is not an Adelie penguin given that Chester is not from Dream island) = # of penguins that are not Adelie penguins from islands other than Dream island $/$ # of penguins in island other than Dream island = $\frac{119\ \text{(eliminate all penguins that are Adelie or from Dream island, only Gentoo penguins from Biscoe are left)}}{44+44+119} \approx 0.575$

Method 2

P(Chester is not an Adelie penguin given that Chester is not from Dream island) = 1- (# of penguins that are Adelie penguins from islands other than Dream island $/$ # of penguins in island other than Dream island) = $1-\frac{44+44}{44+44+119} \approx 0.575$

<average>85</average>

# END SOLUTION

# END SUBPROB

# END PROB