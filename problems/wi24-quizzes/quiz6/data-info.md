It can be hard to find a parking spot on UCSD's campus! The `parking` DataFrame contains UCSD parking occupancy data for two on-campus parking structures. The `"Structure"` column contains either `"Gilman"` or `"Hopkins"`. Each row of `parking` represents one day. The `"Occupancy"` column contains a float representing the proportion of occupied spaces at noon on that day. We'll use this data to test the following hypotheses:

- **Null Hypothesis**: At noon, Gilman and Hopkins are equally occupied. The observed differences in our samples are simply due to random chance.

- **Alternative Hypothesis**: At noon, Hopkins is less occupied than Gilman. The observed differences in our samples cannot be explained by random chance alone.

As our test statistic, we will use the mean noontime `"Occupancy"` of Hopkins minus the mean noontime `"Occupancy"` of Gilman.