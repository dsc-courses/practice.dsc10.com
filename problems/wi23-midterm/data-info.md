#### Video 🎥

<b><a href="https://podcast.ucsd.edu/watch/sp23/dsc10_b00/14">Here's a walkthrough video</a> of some of the problems on the exam.</b>

---

Tropical cyclones, such as hurricanes, are storms characterized by high wind speeds. These
storms can cause great devastation when they make landfall. In the US, the National Hurricane Center (NHC) is the government entity responsible for tracking and predicting these
tropical weather systems. The NHC names tropical storms of sufficient intensity, using a
list of people’s names that gets reused every six years. For example, there have been many
different storms named Cindy, all occurring in different years. We’ll assume that no tropical
storm has ever spanned more than one calendar year.

The DataFrame `storms` contains information about all named tropical storms in the Atlantic
Ocean between 1965 and 2015. Each row corresponds to a data entry describing the storm
at a particular moment in time, and one storm usually has many data entries throughout
the duration of the storm. The columns of `storms` are as follows.

- `"Name"` (`str`): The name of the storm.
- `"Date"` (`int`): The year, month, and day of the data entry, stored as an 8-digit integer. For example, `20151113` corresponds to November 13, 2015.
- `"Time"` (`str`): The time of the data entry.
- `"Status"` (`str`): A categorical variable describing the intensity of the storm at the time of the data entry. There are many possible values, for example `"TD"` stands for “tropical depression” and `"TS"` stands for “tropical storm.”
- `"Latitude"` (`str`): The latitude of the center of the storm at the time of the data entry. Describes the north-south location of the storm.
- `"Longitude"` (`str`): The longitude of the center of the storm at the time of the data entry. Describes the east-west location of the storm.

A preview of `storms` is shown below.

<center><img src='../assets/images/wi23-midterm/df.jpg' width=45%></center>
<br>

Throughout this exam, we will refer to `storms` repeatedly. Assume that we have already
run `import babypandas as bpd` and `import numpy as np`.