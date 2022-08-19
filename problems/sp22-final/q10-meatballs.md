# BEGIN PROB

IKEA is piloting a new rewards program where customers can earn free Swedish meatball plates from the in-store cafe when they purchase expensive items. Meatball plates are awarded as follows. Assume the item price is always an integer.

\begin{center}
\begin{tabular}{|l|l|}
\hline
 item price & number of meatball plates \\
\hline
less than 99 dollars & 0\\
100 to 199 dollars & 1\\
200 dollars or more & 2\\
\hline
\end{tabular}
\end{center}

We want to implement a function called \texttt{calculate\_meatball\_plates} that takes as input an array of several item prices, corresponding to the individual items purchased in one transaction, and returns the total number of meatball plates earned in that transaction.

Select all correct ways of implementing this function from the options below.

\squarebubble{Way 1:}
\begin{verbatim}
def calculate_meatball_plates(prices): 
    meatball_plates = 0
    for price in prices:
        if price >= 100 and price <= 199:
            meatball_plates = 1
        elif price >= 200:
            meatball_plates = 2
    return meatball_plates
\end{verbatim}

\correctsquarebubble{Way 2:}
\begin{verbatim}
def calculate_meatball_plates(prices): 
    meatball_plates = 0
    for price in prices:
        if price >= 200:
            meatball_plates = meatball_plates + 1
        if price >= 100:
            meatball_plates = meatball_plates + 1
    return meatball_plates
\end{verbatim}

\correctsquarebubble{Way 3:}
\begin{verbatim}
def calculate_meatball_plates(prices): 
    return (np.count_nonzero(prices >= 100) + 
            np.count_nonzero(prices >= 200))
\end{verbatim}

\correctsquarebubble{Way 4:}
\begin{verbatim}
def calculate_meatball_plates(prices): 
    return ((prices >= 200).sum()*2 + 
            ((100 <= prices) & (prices <= 199)).sum()*1)
\end{verbatim}

# BEGIN SOLUTION

**Answer: ** 

solution here

# END SOLUTION

# END PROB