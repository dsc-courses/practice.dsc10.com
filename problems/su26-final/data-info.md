Vrinda opened an ice cream shop called The Parlor and you have been hired as the newest employee. The DataFrame `orders` lists ice cream orders from every customer since The Parlor opened. Every ice cream flavor offered at The Parlor has been sold at least once. The columns of `orders` are:

- `"flavor"` (`str`): The flavor of ice cream selected by the customer.
- `"scoops"` (`int`): The number of scoops for the ice cream order.
- `"cone"` (`bool`): `True` if the ice cream was served in a cone and `False` if it was served in a cup.
- `"price"` (`float`): The total price of the ice cream order in dollars.
- `"temp"` (`int`): The temperature high in Fahrenheit of the day on which the order was placed.
- `"days"` (`int`): The number of days since The Parlor opened (i.e. opening day is `0`, 30th day open is `29`).

The first few rows of `orders` are shown below, though `orders` has many more rows than shown.

|   | flavor | scoops | cone | price | temp | days |
|---|---|---|---|---|---|---|
| **0** | double chocolate | 2 | True | 7.50 | 74 | 0 |
| **1** | peanut butter | 1 | True | 4.50 | 74 | 0 |
| **2** | raspberry lemon | 2 | False | 6.00 | 77 | 1 |
| **3** | birthday cake | 4 | True | 13.50 | 77 | 1 |
| **4** | raspberry lemon | 1 | False | 3.00 | 90 | 2 |

<br>

Additionally, we are given another DataFrame called `flavors`. Every ice cream flavor offered at The Parlor appears in `flavors` alphabetically. Each flavor only appears once. The only column in `flavors` is `"name"` (`str`). The first few rows of `flavors` are shown below, though `flavors` has many more rows than shown.

|   | name |
|---|---|
| **0** | apple pie |
| **1** | birthday cake |
| **2** | butterscotch |

<br>

Throughout this exam, we will refer to `orders` and `flavors` repeatedly. Assume that we have already run `import babypandas as bpd` and `import numpy as np`.
