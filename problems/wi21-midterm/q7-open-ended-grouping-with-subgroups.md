# BEGIN PROB

Give an example of a dataset and a question you would want to answer about that dataset which you would answer by grouping with subgroups (using multiple columns in the `groupby` command). Explain how you would use the `groupby` command to answer your question.

Creative responses that are different than ones we've already seen in this class will earn the most credit.

# BEGIN SOLUTION

**Answer: ** There are many possible correct answers. Below are some student responses that earned full credit, lightly edited for clarity.

---

<i> Consider the dataset of Olympic medals (Bronze, Silver, Gold) that a country won for a specific sport, with columns `'sport'`, `'country'`, `'medals'`.</i>

<i> Question: In which sport did the US win the most medals?</i>

<i>We can group by country and then subgroup by sport. We can then use a combination of `reset_index()` and `sort_values(by = 'medals')`  and then use `.get` and `.iloc[-1]` to get the our answer to the question.</i>

---

<i> Given a data set of cell phone purchase volume at every electronics store, we might want to find the difference in popularity of Samsung phones and iPhones in every state. I would use the `groupby` command to first group by state, followed by phone brand, and then aggregate with the `sum()` method. The resulting table would show the total iPhone and Samsung phone sales separately for each state which I could then use to calculate the difference in proportion of each brand's sales volumes.</i>

---

<i> You are given a table called `cars` with columns: `'brands'` (Toyota, Honda, etc.), `'model'` (Prius, Accord, etc.), `'price'` of the car, and `'fuel_type'`  (gas, hybrid, electric). Since you are environmentally friendly you only want cars that are electric, but you want to find the cheapest one. Find the brand that has the cheapest average price for an electric car.</i>

<i>You want to `groupby` on both `'brands'` and `'fuel_type'` and use the aggregate command `mean()` to find the average price per fuel type for each brand. Then you would find only the electric fuel types and sort values to find the cheapest. </i>

<average>81</average>
# END SOLUTION

# END PROB