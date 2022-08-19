# BEGIN PROB

An IKEA chair designer is experimenting with some new ideas for armchair designs. She has the idea of making the arm rests shaped like bell curves, or normal distributions. A cross-section of the armchair design is shown below. 

\begin{center}
    \includegraphics[width=\textwidth]{armchair.png}
\end{center}
This was created by taking the portion of the standard normal distribution from $z=-4$ to $z=4$ and adjoining two copies of it, one centered at $z=0$ and the other centered at $z=8$. Let's call this shape the armchair curve.

Since the area under the standard normal curve from $z=-4$ to $z=4$ is approximately 1, the total area under the armchair curve is approximately 2.

Complete the implementation of the two functions below:
\begin{enumerate}
\item \texttt{area\_left\_of(z)} should return the area under the armchair curve to the left of \texttt{z}, assuming \texttt{-4 <= z <= 12}, and 
\item \texttt{area\_between(x, y)} should return the area under the armchair curve between \texttt{x} and \texttt{y}, assuming \texttt{-4 <= x <= y <= 12}. 
\end{enumerate}

\begin{verbatim}
import scipy

def area_left_of(z):
    '''Returns the area under the armchair curve to the left of z.
       Assume -4 <= z <= 12'''
    if ___(a)___: 
        return ___(b)___ 
    return scipy.stats.norm.cdf(z)

def area_between(x, y):
    '''Returns the area under the armchair curve between x and y. 
    Assume -4 <= x <= y <= 12.'''
    return ___(c)___
\end{verbatim}


# BEGIN SUBPROB

What goes in blank (a)?

# BEGIN SOLUTION

**Answer: ** \texttt{z>4}

solution here

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

What goes in blank (b)?

# BEGIN SOLUTION

**Answer: ** \texttt{scipy.stats.norm.cdf(z-8)+1}

solution here

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

What goes in blank (c)?

# BEGIN SOLUTION

**Answer: ** \texttt{area\_left\_of(y) - area\_left\_of(x)}

solution here

# END SOLUTION

# END SUBPROB

# END PROB