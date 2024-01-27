The American Kennel Club (AKC) organizes information about dog
breeds. We've loaded their dataset into a DataFrame called `df`. The index of
`df` contains the dog breed names as `str` values.

The columns are:
    
  - `'kind' (str)`: the kind of dog (herding, hound, toy, etc.). There
    are six total kinds.
  - `'size' (str)`: small, medium, or large.
  - `'longevity' (float)`: typical lifetime (years).
  - `'price' (float)`: average purchase price (dollars).
  - `'kids' (int)`: suitability for children. A value of `1` means
  high suitability, `2` means medium, and `3` means low.
  - `'weight' (float)`: typical weight (kg).
  - `'height' (float)`: typical height (cm).

The rows of `df` are arranged in **no particular
 order**. The first five rows of `df` are shown below (though
`df` has **many more rows** than pictured here).

<center><img src='../assets/images/su22-final/df.png' width=50%></center>
<br>
