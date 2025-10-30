The English language is considered a challenging language to learn, largely because there are exceptions to just about every "rule"!

In this exam, we'll work with a data set of English words that appeared in texts used by Indian undergraduate students learning English. The students were asked to read the texts and mark the words they found difficult.

The DataFrame `words` is indexed by `"word"` and contains the following columns:

- `"freq"` (`int`): The frequency of the word, or the number of times it appeared in the texts.
- `"length"` (`int`): The length of the word, or the number of letters it contains.
- `"ps"` (`str`): The part of speech of the word (e.g. noun, verb, adjective). This is formatted as an ordered pair, where the first component is the word, and the second component is a tag indicating the part of speech (e.g. VBD for past tense verb). The tags and their meanings are determined by a system known as the Penn Treebank part of speech tagging system.
- `"diff"` (`int`): The number of students who marked the word difficult.

The first few rows of `words` are shown below, though there are many more rows than pictured.

<center><img src="https://raw.githubusercontent.com/dsc-courses/practice.dsc10.com/refs/heads/master/assets/images/fa25-midterm/preview.jpg" width=400></center> \


Assume that we have already run `import babypandas as bpd` and `import numpy as np`.
