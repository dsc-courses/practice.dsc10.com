# BEGIN PROB

You are browsing the IKEA showroom, deciding whether to purchase the BILLY bookcase or the LOMMARP bookcase. You are concerned about the amount of time it will take to assemble your new bookcase, so you look up the assembly times reported in \texttt{app\_data}. Thinking of the data in \texttt{app\_data} as a random sample of all IKEA purchases, you want to perform a permutation test to test the following hypotheses.

\textbf{Null Hypothesis}: The assembly time for the BILLY bookcase and the assembly time for the LOMMARP bookcase come from the same distribution.

\textbf{Alternative Hypothesis}: The assembly time for the BILLY bookcase and the assembly time for the LOMMARP bookcase come from different distributions. 

# BEGIN SUBPROB

Suppose we query \texttt{app\_data} to keep only the BILLY bookcases, then average the \texttt{"minutes"} column. In addition, we separately query \texttt{app\_data} to keep only the LOMMARP bookcases, then average the \texttt{"minutes"} column. If the null hypothesis is true, which of the following statements about these two averages is correct?

\bubble{These two averages are the same.}

\correctbubble{Any difference between these two averages is due to random chance.}

\bubble{Any difference between these two averages cannot be ascribed to random chance alone.}

\bubble{The difference between these averages is statistically significant.}

# BEGIN SOLUTION

**Answer: ** 

solution here

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

For the permutation test, we'll use as our test statistic the average assembly time for BILLY bookcases minus the average assembly time for LOMMARP bookcases, in minutes.

Complete the code below to generate one simulated value of the test statistic in a new way, without using \texttt{np.random.permutation}.

\begin{verbatim}
billy = (app_data.get("product") == 
        "BILLY Bookcase, white, 31 1/2x11x79 1/2")
lommarp = (app_data.get("product") == 
          "LOMMARP Bookcase, dark blue-green, 25 5/8x78 3/8")
billy_lommarp = app_data[billy|lommarp]
billy_mean = np.random.choice(billy_lommarp.get("minutes"), 
                              billy.sum()).mean()
lommarp_mean = _________
billy_mean - lommarp_mean
\end{verbatim}

What goes in the blank?

\bubble{\texttt{billy\_lommarp[lommarp].get("minutes").mean()}}

\bubble{\texttt{np.random.choice(billy\_lommarp.get("minutes"), lommarp.sum()).mean()}} 

\bubble{\texttt{billy\_lommarp.get("minutes").mean() - billy\_mean}}

\correctbubble{\texttt{(billy\_lommarp.get("minutes").sum() - billy\_mean*billy.sum())/lommarp.sum()}}

# BEGIN SOLUTION

**Answer: ** 

solution here

# END SOLUTION

# END SUBPROB

# END PROB