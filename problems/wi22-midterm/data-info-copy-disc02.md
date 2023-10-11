For the problems that follow, we will work with a dataset consisting of various skyscrapers in the US, which we've loaded into a DataFrame called `sky`. The first few rows of `sky` are shown below (though the full DataFrame has more rows):

<center><img src='../assets/images/wi22-midterm/sky.png' width=60%></center>

<p>&nbsp;</p>

Each row of `sky` corresponds to a single skyscraper. For each skyscraper, we have:

* its name, which is stored in the index of `sky` (string)

* the `'material'` it is made up of (string)

* the `'city'` in the US where it is located (string)

* the number of `'floors'` (levels) it contains (int)

* its `'height'` in meters (float), and 

* the `'year'` in which it was opened (int)
