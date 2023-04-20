# BEGIN PROB

The expression below evaluates to `True`.

```py
(
classify_artist('Michelle Branch')=='outdated' 
and 
classify_artist('Drake')=='trending'
)
```

Consider the scatterplot created by the code below.

```py
merged.plot(kind='scatter', x='Year', y='Top_Hit_Year');
```

The point for Drake is somewhere in this scatterplot. Relative to the point for Drake, there are four quadrants of the scatterplot, as shown below.

<center><img src='../assets/images/sp22-midterm/drake-quadrants.png' width=200></center>
<br>

There is one quadrant in which the point for Michelle Branch **cannot** appear. Which is it?


( ) northeast
( ) northwest
( ) southwest
( ) southeast

# BEGIN SOLUTION

**Answer: ** northwest

The scatterplot shows an artist's year of performance at Sun God on the x-axis, and their top hit year on the y-axis.

Since Drake is considered trending, we know his top hit came out within the five years prior to his Sun God performance.  In other words, the time gap between his top hit release and his Sun God performance is at most five years.

If Michelle Branch were in the northwest quadrant, that would mean her x-coordinate was smaller than Drake's, and her y-coordinate was larger. In other words, that would mean she performed at Sun God before Drake and her top hit was released after Drake's. This means the time gap between her top hit release and her Sun God performance is less than five years, so she could not be considered outdated.

We could also answer this question through process of elimination. This would entail finding scenarios that show each of the other three quadrants is possible. 

Michelle Branch could wind up in the northeast quadrant if, say, she performed 10 years after Drake and released her top hit 1 year after Drake. She'd be considered outdated because the time gap between her top hit and her Sun God performance would exceed five years.

Similarly, Michelle Branch could be in the southwest quadrant if, say, she performed 1 year before Drake and released her top hit 10 years before Drake. Again, the time gap between her top hit and her Sun God performance would exceed five years, making her outdated.

She could also be in the southeast quadrant if, say, she performed 10 years after Drake and released her top hit 10 years before Drake. This would also make the time gap between her top hit and Sun God performance more than five years.

So since all three other quadrants are possible and we are told that one quadrant is impossible, the northwest quadrant must be impossible.

<average>65</average>


# END SOLUTION


# END PROB
