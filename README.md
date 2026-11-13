# practice.dsc10.com

Repository containing practice problems for DSC 10 (past exams and discussion). Hosted at practice.dsc10.com.

## Publishing a change

Pushing to `master` publishes the site. You don't need to build anything or install anything:

1. Run `git pull`, then edit the files you need (usually in `problems/` or `pages/`).
2. Commit and push to `master`, but don't commit `docs/`.
3. GitHub tests, builds and publishes the whole site. It's live about 8 minutes later.

If the build fails, the live site stays as it was and your commit gets a red X on GitHub. Open it to read the error, which names the file to fix, then push the fix. Nothing else publishes until the build passes, so please fix it soon.

### Keeping work hidden

Everything on `master` goes live, so:

- **Solutions that aren't ready:** set `show_solution: false` in the page's `.yml`. This hides them on that page and keeps its problems off the lecture pages.
- **Problems that aren't ready:** they aren't built until a page's `.yml` lists them.
- **Pages that aren't ready:** leave them out of `index.md`. They can still be reached by URL.

The repo itself is public, so don't push anything students must not see yet, like upcoming exams.

## Previewing locally (optional)

Install [uv](https://docs.astral.sh/uv/getting-started/installation/). uv sets up the right versions of Python, the Python packages and pandoc the first time you run a command. Then run these from the root of the repo. The output goes in `docs/`.

```
uv run run.py pages/exams/fa24-final.yml   # one page (faster)
uv run run.py                              # the whole site
uv run run.py index                        # just the homepage
```

When you're done, discard the preview with `git restore docs`.

## Changing the setup

- Run the tests with `uv run pytest`.
- Package versions are locked in `uv.lock`, so use `uv add` and `uv remove` instead of editing it, and commit it along with `pyproject.toml`.
- The pandoc version comes from `pypandoc_binary`. To change it, update that package and `PINNED_PANDOC_VERSION` in `utils/pandoc_tool.py` together, then rebuild and compare the output.

## Writing problems

Style guide for writing up problems:

- **Answer:** should be bolded followed by unbolded answer(s), comma separated if it fits on one line, or each answer on a new line if it doesn't fit on one line
- Use () for choose one, [] for select all. Add a space before the text of each answer choice.
- For subsubparts, use numbers followed by period to introduce each question

In translating from Latex to Markdown, there are a few easy find/replace things that help with a lot of things:

\begin{verbatim} --> ```py
\end{verbatim} --> ```
" --> '
\_ --> _
\texttt{ --> `
\textbf{ --> **
\textit{ --> *
\bubble --> ( )
\correctbubble --> ( )
\squarebubble --> [ ]
\correctsquarebubble --> [ ]
\begin{subprobset} -->
\end{subprobset} -->
\begin{subprob} --> # BEGIN SUBPROB
\end{subprob} --> # END SUBPROB
\begin{responsebox} --> # BEGIN SOLUTION
\end{responsebox} --> # END SOLUTION
\begin{soln} --> # BEGIN SOLUTION
\end{soln} --> # END SOLUTION
\bigskip -->
\noindent --> 

Note: ( ) and [ ] need a space between the brackets. There should not be blank lines between options.

To explain up-front:
- All exams are individual (collaboration on exams is never allowed).
- What ( ) and [ ] mean. In their absence, students needed to write out code by hand.
- In-person means on-paper.
- Think of select-all questions as a sequence of true-false questions. Partial credit for these questions was assigned accordingly.
- When taking an exam for practice, we recommend having a copy of the DSC 10 reference sheet open in another tab, as well as a second copy of the exam, so you can access the data descriptions.
