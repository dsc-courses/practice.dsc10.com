#### Video 🎥

<b><a href="https://podcast.ucsd.edu/watch/wi24/dsc10_a00/29">Here's a walkthrough video</a> of some of the problems on the exam.</b>

---

*Clue* is a murder mystery game where players use the process of elimination to figure out
the details of a crime. The premise is that a murder was committed inside a large home, by
one of **6 suspects**, with one of **7 weapons**, and in one of **9 rooms**.

The game comes with **22 cards**, one for each of the 6 suspects, 7 weapons, and 9 rooms. To
set up the game, one suspect card, one weapon card, and one room card are chosen randomly,
without being looked at, and placed aside in an envelope. The cards in the envelope represent
the details of the murder: who did it, with what weapon, and in what room.

The remaining 19 cards are randomly shuffled and dealt out to the players (as equally as
possible). Players then look at the cards they were dealt and can conclude that any cards
they see were **not** involved in the murder. In the gameplay, players take turns moving around
to different rooms of the house on the gameboard, which gives them opportunities to see
cards in other players’ hands and further eliminate suspects, weapons, and rooms. The first
player to narrow it down to one suspect, with one weapon, and in one room can make an
accusation and win the game!

Suppose Janine, Henry, and Paige are playing a
game of Clue. Janine and Paige are each dealt
6 cards, and Henry is dealt 7. The DataFrame
clue has 22 rows, one for each card in the game.
clue represents **Janine’s knowledge** of who is
holding each card. clue is indexed by "`Card`",
which contains the name of each suspect, weapon,
and room in the game. The "`Category`" column contains "`suspect`", "`weapon`", or "`room`".
The "`Cardholder`" column contains "`Janine`",
"`Henry`", "`Paige`", or "`Unknown`".

Since Janine’s knowledge is changing throughout
the game, the "`Cardholder`" column needs to be
updated frequently. At the beginning of the game,
the "`Cardholder`" column contains only "`Janine`"
and "`Unknown`" values. We’ll assume throughout this exam that clue contains Janine’s current
knowledge at an arbitrary point in time, not necessarily at the beginning of the game. For example,
clue **may look like** the DataFrame below.


<center><img src='../assets/images/wi24-midterm/clue.jpg' width=20%></center>
<br>

**Note**: Throughout the exam, assume we have already run `import babypandas as bpd` and
`import numpy as np`.
