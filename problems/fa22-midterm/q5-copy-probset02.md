---
lecture: 8
---

# BEGIN PROB

Consider the following incomplete assignment statement.

```py
result = evs______.mean()
```

In each part, fill in the blank above so that result evaluates to the specified quantity.

# BEGIN SUBPROB

A DataFrame, indexed by `"Brand"`, whose `"Seats"` column contains the average
number of `"Seats"` per `"Brand"`. (The DataFrame may have other columns in it as
well.)

# BEGIN SOLUTION

**Answer:** `.get(["Brand", "Seats", "TopSpeed", "Range"]).groupby("Brand")`

When we group by a column, the resulting DataFrame contains one row for every unique value in that column. The question specified that we wanted some information _per_ `"Brand"`, which implies that grouping by `"Brand"` is necessary.

`"Model"` and `"BodyStyle"` are strings. `.mean()` errors if those columns are still present, so we use `.get()` first and keep only `"Brand"` plus the numeric columns. After that selection, `.mean()` — which is already in the prompt — averages `"Seats"`, `"TopSpeed"`, and `"Range"` within each brand.

The resulting DataFrame still has columns besides `"Seats"`. For instance, it has a `"Range"` column with the average `"Range"` for each `"Brand"`. That's fine, since we were told that the resulting DataFrame may have other columns in it as well.

<average>76</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

A number, corresponding to the average `"TopSpeed"` of all EVs manufactured
by Audi in evs

# BEGIN SOLUTION

**Answer:** `[evs.get("Brand") == "Audi"].get("TopSpeed")`

There are two parts to this problem:

1. Querying, to make sure that we only keep the rows corresponding to Audis. This is accomplished by:

    - Using `evs.get("Brand") == "Audi"` to create a Boolean Series, with `True`s for the rows we want to keep and `False`s for the other rows.
    - Using Boolean indexing to keep only the rows in which the aforementioned Series is `True`. This is accomplished by `evs[evs.get("Brand") == "Audi"]` (though the `evs` part at the front was already provided).

2. Accessing the `"TopSpeed"` column. This is accomplished by using `.get("TopSpeed")`.

Then, `evs[evs.get("Brand") == "Audi"].get("TopSpeed")` is a Series contaning the `"TopSpeed"`s of all Audis, and mean of this Series is the result we're looking for. The call to `.mean()` was already provided for us.

<average>77</average>

# END SOLUTION

# END SUBPROB

# END PROB
