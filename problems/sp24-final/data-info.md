#### Video 🎥

Some problems on this exam have walkthrough videos available:

- [Problem 2](https://podcast.ucsd.edu/watch/fa25/dsc10_a00/28/kaltura#1:42) at 01:42
- [Problem 3](https://podcast.ucsd.edu/watch/fa25/dsc10_d00/26#24:30) at 24:30
- [Problem 6](https://podcast.ucsd.edu/watch/fa25/dsc10_d00/26#33:15) at 33:15
- [Problem 7](https://podcast.ucsd.edu/watch/fa25/dsc10_d00/26#47:59) at 47:59
- [Problem 10](https://podcast.ucsd.edu/watch/fa25/dsc10_c00/29#24:30) at 24:30
- [Problem 11](https://podcast.ucsd.edu/watch/sp26/dsc10_b00/29#1:52) at 01:52
- [Problem 12](https://podcast.ucsd.edu/watch/fa25/dsc10_a00/29/kaltura#13:30) at 13:30
- [Problem 15](https://podcast.ucsd.edu/watch/fa25/dsc10_c00/29#4:45) at 04:45

---

In this final, we'll explore data on 800 different apartments available for rent in San Diego. Each row in the DataFrame `apts` corresponds to an individual apartment. The DataFrame is indexed by `"Apartment ID"` (`int`), which is a unique identifier for the apartment. 

The columns of `apts` are as follows:

-   `"Rent"` (`int`): The monthly rent for the apartment, in dollars. 
-   `"Bed"` (`str`): The number of bedrooms in the apartment. Values are `"Studio"`, `"One"`, `"Two"`, and `"Three"`. 
-   `"Bath"` (`str`): The number of bathrooms in the apartment. Values are `"One"`, `"One and a half"`, `"Two"`, `"Two and a half"`, and `"Three"`.
-   `"Laundry"` (`bool`): If the apartment comes with an in-unit washer and dryer.
-   `"Sqft"` (`int`): The area of the apartment, in square feet. 
-   `"Neighborhood"` (`str`): The neighborhood in which the apartment is located.
-   `"Complex"` (`str`): The complex the apartment is a part of.
-   `"Lease Term"` (`str`): The duration of the apartment's lease.  Values are `"1 month"`, `"6 months"`, and `"1 year"`. 

The first few rows of `apts` are shown below, though `apts` has many more rows than pictures, 800 in total. The data in `apts` is only a sample from the much larger population of **all** San Diego apartments.

<center><img src="../../assets/images/sp24-final/apts.jpg" width=600></center>

<br>

Throughout this exam, assume that we have already run `import babypandas as bpd` and `import numpy as np`.