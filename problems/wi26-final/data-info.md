We will work with a DataFrame called `zoo` containing information about animals at the San Diego Zoo. Each row corresponds to one animal. The DataFrame includes columns such as:

- `"species"` (`str`): The species name (e.g. `"Giant Panda"`).
- `"exhibit"` (`str`): The exhibit where the animal is housed.
- `"kind"` (`str`): The animal’s class (e.g. `"Reptile"`, `"Mammal"`, `"Bird"`).
- `"weight_lb"` (`float`): The animal’s weight in pounds.
- `"age"` (`float`): The animal’s age.
- `"status"` (`str`): Conservation status (e.g. `"Endangered"`, `"Vulnerable"`).
- `"daily_food_lb"` (`float`): Estimated pounds of food consumed per day.
- Location or area of the zoo where the animal’s habitat is (e.g. Asian Passage), as used in the exam.

A preview of `zoo` is shown below.

<center><img src="../assets/images/wi26-final/zoo_reference.png" width=800></center>

Assume we have already run `import babypandas as bpd` and `import numpy as np`.
