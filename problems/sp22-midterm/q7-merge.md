# BEGIN PROB

Another DataFrame called `music` contains a row for every music artist that has ever released a song. The columns are:

- `'Name'` (`str`): the name of the music artist
- `'Genre'` (`str`): the primary genre of the artist
- `'Top_Hit'` (`str`): the most popular song by that artist, based on sales, radio play, and streaming
- `'Top_Hit_Year'` (`int`): the year in which the top hit song was released

You want to know how many musical genres have been represented at Sun God since its inception in 1983. Which of the following expressions produces a DataFrame called `merged` that could help determine the answer?


( ) `merged = sungod.merge(music, left_on='Year', right_on='Top_Hit_Year')`
( ) `merged = music.merge(sungod, left_on='Year', right_on='Top_Hit_Year')`
( ) `merged = sungod.merge(music, left_on='Artist', right_on='Name')`
( ) `merged = music.merge(sungod, left_on='Artist', right_on='Name')`

# BEGIN SOLUTION

**Answer: ** `merged = sungod.merge(music, left_on='Artist', right_on='Name')`

The question we want to answer is about Sun God music artists' genres. In order to answer, we'll need a DataFrame consisting of rows of artists that have performed at Sun God since its inception in 1983. If we merge the `sungod` DataFrame with the `music` DataFrame based on the artist's name, we'll end up with a DataFrame containing one row for each artist that has ever performed at Sun God. Since the column containing artists' names is called `'Artist'` in `sungod` and `'Name'` in `music`, the correct syntax for this merge is `merged = sungod.merge(music, left_on='Artist', right_on='Name')`. Note that we could also interchange the left DataFrame with the right DataFrame, as swapping the roles of the two DataFrames in a merge only changes the ordering of rows and columns in the output, not the data itself. This can be written in code as `merged = music.merge(sungod, left_on='Name', right_on='Artist')`, but this is not one of the answer choices.

<average>86</average>


# END SOLUTION

# END PROB
