Clash Royale is a mobile game where players build decks of cards and use the abilities provided by those cards to destroy their opponent's defenses.

The `cards` DataFrame describes the cards in the game. It is indexed by card `"name"` and has columns:

- `"damage"` (`int`): amount of damage dealt by the card
- `"type"` (`str`): card type, either `"spell"`, `"troop"`, or `"building"`
- `"rarity"` (`str`): card rarity, either `"common"`, `"rare"`, or `"epic"`
- `"arena_unlocked"` (`int`): a number 1 through 14 representing the stage of the game in which the card can be used

`cards` has **40 rows** and is **sorted** in ascending order of `"arena_unlocked"`. The first figure below shows the first six rows of `cards`, and the second figure shows the distribution of `"arena_unlocked"` over all 40 rows.

<center><img src="https://raw.githubusercontent.com/dsc-courses/practice.dsc10.com/refs/heads/master/assets/images/sp26-quizzes/cr.jpg" width="400"></center>

<center><img src="https://raw.githubusercontent.com/dsc-courses/practice.dsc10.com/refs/heads/master/assets/images/sp26-quizzes/hist.jpg" width="400"></center>

Assume that we have already run `import babypandas as bpd` and `import numpy as np`.
