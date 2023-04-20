King Triton, UCSD's mascot, is quite the traveler! For this question, we will be working with the `flights` DataFrame, which details several facts about each of the flights that King Triton has been on over the past few years. The first few rows of `flights` are shown below.

<center><img src='../assets/images/fa21-midterm/flights.png' width=40%></center>
<br>

Here's a description of the columns in `flights`:

- `'DATE'`: the date on which the flight occurred. Assume that there were no "redeye" flights that spanned multiple days.
- `'FLIGHT'`: the flight number. Note that this is not unique; airlines reuse flight numbers on a daily basis.
- `'FROM'` and `'TO'`: the 3-letter airport code for the departure and arrival airports, respectively. Note that it's not possible to have a flight from and to the same airport.
- `'DIST'`: the distance of the flight, in miles.
- `'HOURS'`: the length of the flight, in hours.
- `'SEAT'`: the kind of seat King Triton sat in on the flight; the only possible values are `'WINDOW'`, `'MIDDLE'`, and `'AISLE'`.