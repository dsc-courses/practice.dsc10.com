Unidentified flying objects (or UFOs) are objects seen in the sky that cannot be explained by the observer. These objects seem to be something other than planes, birds, etc. Some people believe that UFOs are actually extraterrestrial spacecrafts that suggest the possibility of alien life.

UFO sightings are reports describing where and when an individual observed a UFO. The DataFrame `ufo` has one row for every reported UFO sighting in the state of Nevada. The columns are:

- `"zipcode"` (`str`): The zip code of the town where the sighting was reported.
- `"shape"` (`str`): The reported shape of the UFO, either `"cylinder"`, `"sphere"`, or `"disk"`.
- `"time"` (`str`): The time at which the sighting began, formatted as 24-hour time as `"HH:MM"`.
- `"duration"` (`str`): How long the sighting lasted, formatted using a combination of hours (`h`), minutes (`m`), and seconds (`s`), e.g. `"2m"` or `"1h 45m 3s"`.

The first few rows of `ufo` are shown below, though `ufo` has many more rows than pictured.

<center><img src='../assets/images/su26-midterm/ufo.png' width=600></center>
<br>

Throughout this exam, we will refer to `ufo` repeatedly.
Assume that we have already run `import babypandas as bpd` and `import numpy as np`.
