#### Video 🎥

<b><a href="https://podcast.ucsd.edu/watch/sp23/dsc10_a00/14">Here's a walkthrough video</a> of some of the problems on the exam.</b>

---


In September 2020, Governor Gavin Newsom announced that by 2035, all new vehicles sold in California must be zero-emissions vehicles. Electric vehicles (EVs) are among the most popular zero-emissions vehicles (though other examples include plug-in hybrids and hydrogen
fuel cell vehicles).

<center><img src='../assets/images/fa22-midterm/data22.png' width=20%></center>
<br>

The DataFrame `evs` consists of **32** rows, each of which contains information about a different EV model.

* `"Brand"` (str): The vehicle's manufacturer.
* `"Model"` (str): The vehicle's model name.
* `"BodyStyle"` (str): The vehicle's body style.
* `"Seats"` (int): The vehicle's number of seats.
* `"TopSpeed"` (int): The vehicle's top speed, in kilometers per hour.
* `"Range"` (int): The vehicle's range, or distance it can travel on a single charge, in kilometers.

The first few rows of `evs` are shown below (though remember, `evs` has 32 rows total).

<center><img src='../assets/images/fa22-midterm/form22.png' width=60%></center>
<br>

**Throughout this exam, we will refer to `evs` repeatedly.**

Assume that:

- The only four values in the `"Brand"` column are `"Tesla"`, `"BMW"`, `"Audi"`, and `"Nissan"`.
- We have already run `import babypandas as bpd` and `import numpy as np`.

**Tip:** Open this page in another tab, so that it is easy to refer to this data description as you work through the exam.


