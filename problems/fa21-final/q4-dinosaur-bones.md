# BEGIN PROB

# BEGIN SUBPROB

The Museum of Natural History has a large collection of dinosaur bones, and they know the approximate year each bone is from. They want to use this sample of dinosaur bones to estimate **the total number of years that dinosaurs lived on Earth**. We'll make the assumption that the sample is a uniform random sample from the population of all dinosaur bones. Which statistic below will give the best estimate of the population parameter?

( ) sample sum
( ) sample max - sample min
( ) 2 $\cdot$ (sample mean - sample min)
( ) 2 $\cdot$ (sample max - sample mean)
( ) 2 $\cdot$ sample mean
( ) 2 $\cdot$ sample median

# BEGIN SOLUTION

**Answer:** sample max - sample min

Our goal is to estimate **the total number of years that dinosaurs lived on Earth**. In other words, we want to know the range of time that dinosaurs lived on Earth, and by definition range = biggest value - smallest value. By using "sample max - sample min", we calculate the difference between the earliest and the latest dinosaur bones in this uniform random sample, which helps us to estimate the population range.

<average>52</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

The curator at the Museum of Natural History, who happens to have taken a data science course in college, points out that the estimate of the parameter obtained from this sample could certainly have come out differently, if the museum had started with a different sample of bones. The curator suggests trying to understand the distribution of the sample statistic. Which of the following would be an appropriate way to create that distribution?

( ) bootstrapping the original sample
( ) using the Centrual Limit Theorem
( ) both bootstrapping and the Central Limit Theorem
( ) neither bootstrapping nor the Central Limit Theorem

# BEGIN SOLUTION

**Answer:** neither bootstrapping nor the Central Limit Theorem

Recall, the Central Limit Theorem (CLT) says that the probability distribution of **the sum or average** of a large random sample drawn with replacement will be roughly normal, regardless of the distribution of the population from which the sample is drawn. Thus, the theorem only applies when our sample statistics is sum or average, while in this question, our statistics is range, so CLT does not apply.

Bootstrapping is a valid technique for estimating measures of central tendency, e.g. the population mean, median, standard deviation, etc. It doesn't work well in estimating extreme or sensitive values, like the population maximum or minimum. Since the statistic we're trying to estimate is the difference between the population maximum and population minimum, bootstrapping is not appropriate.

<average>20</average>

# END SOLUTION

# END SUBPROB

# END PROB