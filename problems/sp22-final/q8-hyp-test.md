# BEGIN PROB

For this question, let's think of the data in \texttt{app\_data} as a random sample of all IKEA purchases and use it to test the following hypotheses.

\textbf{Null Hypothesis}: IKEA sells an equal amount of beds (category ``bed") and outdoor furniture (category ``outdoor"). 

\textbf{Alternative Hypothesis}: IKEA sells more beds than outdoor furniture.

The DataFrame \texttt{app\_data} contains 5000 rows, which form our sample. Of these 5000 products,
\begin{itemize}
    \item 1000 are beds,
    \item 1500 are outdoor furniture, and
    \item 2500 are in another category.
\end{itemize}

# BEGIN SUBPROB

Which of the following \textbf{could} be used as the test statistic for this hypothesis test? Select all that apply.

\squarebubble{Among $2500$ beds and outdoor furniture items, the absolute difference between the proportion of beds and the proportion of outdoor furniture.}

\correctsquarebubble{Among $2500$ beds and outdoor furniture items, the proportion of beds.}

\correctsquarebubble{Among $2500$ beds and outdoor furniture items, the number of beds.}

\squarebubble{Among $2500$ beds and outdoor furniture items, the number of beds plus the number of outdoor furniture items.}

# BEGIN SOLUTION

**Answer: ** 

solution here

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Let's do a hypothesis test with the following test statistic: among $2500$ beds and outdoor furniture items, the proportion of outdoor furniture minus the proportion of beds.

Complete the code below to calculate the observed value of the test statistic and save the result as \texttt{obs\_diff}.

\begin{verbatim}
    outdoor = (app_data.get("category")=="outdoor") 
    bed = (app_data.get("category")=="bed")
    obs_diff = ( ___(a)___ - ___(b)___ ) / ___(c)___
\end{verbatim}

The table below contains several Python expressions. Choose the correct expression to fill in each of the three blanks. Three expressions will be used, and two will be unused.

\begin{center}
\begin{tabular}{|l| l|}
\hline
Python expression & Which blank does this go in? \\
\hline
\texttt{app\_data.shape[0]}   & \bubble{(a)} \bubble{(b)} \\
& \bubble{(c)} \bubble{None} \\
\hline
\texttt{app\_data[bed].shape[0]}  & \bubble{(a)} \bubble{(b)} \\
& \bubble{(c)} \bubble{None} \\
\hline
\texttt{app\_data[outdoor].shape[0]}  & \bubble{(a)} \bubble{(b)} \\
& \bubble{(c)} \bubble{None} \\
\hline
\texttt{app\_data[outdoor | bed].shape[0]}   & \bubble{(a)} \bubble{(b)} \\
& \bubble{(c)} \bubble{None} \\
\hline
\texttt{app\_data[outdoor \& bed].shape[0]}   & \bubble{(a)} \bubble{(b)} \\
& \bubble{(c)} \bubble{None} \\
\hline
\end{tabular}
\end{center}

# BEGIN SOLUTION

**Answer: ** 

solution here

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB
Which of the following is a valid way to generate one value of the test statistic according to the null model? Select all that apply.

\correctsquarebubble{Way 1:}
\begin{verbatim}
multi = np.random.multinomial(2500, [0.5,0.5]) 
(multi[0] - multi[1])/2500
\end{verbatim}

\squarebubble{Way 2:}
\begin{verbatim}
outdoor = np.random.multinomial(2500, [0.5,0.5])[0]/2500 
bed = np.random.multinomial(2500, [0.5,0.5])[1]/2500 
outdoor - bed 
\end{verbatim}

\correctsquarebubble{Way 3:}
\begin{verbatim}
choice = np.random.choice([0, 1], 2500, replace=True) 
choice_sum = choice.sum()
(choice_sum - (2500 - choice_sum))/2500
\end{verbatim}

\correctsquarebubble{Way 4:}
\begin{verbatim}
choice = np.random.choice(["bed", "outdoor"], 2500, replace=True) 
bed = np.count_nonzero(choice=="bed")
outdoor = np.count_nonzero(choice=="outdoor")
outdoor/2500 - bed/2500
\end{verbatim}

\squarebubble{Way 5:}
\begin{verbatim}
outdoor = (app_data.get("category")=="outdoor") 
bed = (app_data.get("category")=="bed")
samp = app_data[outdoor|bed].sample(2500, replace=True) 
(samp[samp.get("category")=="outdoor"].shape[0]/2500 - 
 samp[samp.get("category")=="bed"].shape[0]/2500)
\end{verbatim}

\correctsquarebubble{Way 6:}
\begin{verbatim}
outdoor = (app_data.get("category")=="outdoor") 
bed = (app_data.get("category")=="bed")
samp = (app_data[outdoor|bed].groupby("category").count()
        .reset_index().sample(2500, replace=True))      
(samp[samp.get("category")=="outdoor"].shape[0]/2500 - 
 samp[samp.get("category")=="bed"].shape[0]/2500)
\end{verbatim}


# BEGIN SOLUTION

**Answer: ** 

solution here

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Suppose we generate $10{,}000$ simulated values of the test statistic according to the null model and store them in an array called \texttt{simulated\_diffs}. Complete the code below to calculate the p-value for the hypothesis test.

\begin{verbatim}
    np.count_nonzero(simulated_diffs _________ obs_diff)/10000
\end{verbatim}

What goes in the blank?

\bubble{\texttt{<}}

\correctbubble{\texttt{<=}}

\bubble{\texttt{>}}

\bubble{\texttt{>=}}

# BEGIN SOLUTION

**Answer: ** 

solution here

# END SOLUTION

# END SUBPROB

# END PROB