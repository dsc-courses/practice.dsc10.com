# practice.dsc10.com

Repository containing practice problems for DSC 10 (past exams and discussions). Hosted at [practice.dsc10.com](https://practice.dsc10.com).

---

## Getting Started

### 1. Install pandoc

Pandoc is required to build the site. Install it as a standalone program from [pandoc.org/installing.html](https://pandoc.org/installing.html).

### 2. Install uv

<!-- uv manages Python and all Python dependencies automatically — you do not need to install Python separately. -->

uv is a python package manager and project manager. this is designed to replace pip and poetry.

**Mac/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
Or via Homebrew: `brew install uv`

**Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 3. Clone the repo and install dependencies

```bash
git clone https://github.com/dsc-courses/practice.dsc10.com.git
cd practice.dsc10.com
uv sync
```

`uv sync` creates a virtual environment and installs all required packages. You only need to run this once (or again if `pyproject.toml` changes).

### 4. You're done!

If you ran `uv sync` for the first time, it will have created a new virtual environment with all the required packages installed.

Some important notes about uv:
- Anytime you want to run something, begin it with `uv run`. For example: `uv run python run.py pages/exams/fa25-final.yml`
- To add a package: `uv add <package-name>`
- To remove a package: `uv remove <package-name>`

Always use `uv run python` instead of `python` directly — this ensures you're using the project's dependencies, not anything on your system.

### 5. Testing your changes

To rebuild the HTML for a specific exam:

```bash
uv run python run.py pages/exams/fa25-final.yml
```

Replace `fa25-final.yml` with whichever exam or discussion you're working on.

### 6. Preview your changes

When you run the build command, it regenerates the corresponding HTML file inside `docs/`. For example, running `uv run python run.py pages/exams/fa25-final.yml` will update `docs/fa25-final/index.html`.

To preview:
1. Open `docs/<exam-name>/index.html` in your browser (e.g. `docs/fa25-final/index.html`) or open a live server of the html
2. Run the build command again after making edits
3. Refresh the browser to see your updated changes

You can keep the HTML file open in your browser and just refresh it each time you rebuild — you do not need to reopen it. **Always preview your changes locally before pushing to main.**

### 7. Push your changes

```bash
git add .
git commit -m "your message here"
git push
```

You must commit and push both the markdown files you edited **and** the generated HTML in `docs/` — the live site at practice.dsc10.com serves those HTML files directly.

---

## Directory Structure

```
practice.dsc10.com/
├── pages/        # Config files (one per exam/discussion)
├── problems/     # Markdown files (one per question)
├── docs/         # Auto-generated HTML — do not edit directly
├── assets/       # CSS and images used in the site
├── run.py        # Build script
└── index.md      # Source for the homepage
```

### `pages/`

Each page on the site corresponds to a `.yml` config file in this folder, organized into subfolders by type (`exams/`, `disc/`, `quizzes/`, etc.).

Example — `pages/exams/fa25-final.yml`:
```yaml
title: 'Fall 2025 Final Exam'
instructors: Janine Tiefenbruck, Peter Chi
context: This exam was administered in-person. Students were allowed one page of double-sided handwritten notes. No calculators were allowed. Students had **3 hours** to take this exam.
show_solution: true
data_info: fa25-final/data-info
problems:
  - fa25-final/q01
  - fa25-final/q02
  ...
```

Key fields:
- `title` / `instructors` / `context` — displayed at the top of the page
- `show_solution` — set to `true` to render solutions (used for discussions when needed)
- `data_info` — path to the dataset description file (relative to `problems/`)
- `problems` — ordered list of problem files to include (paths relative to `problems/`, no `.md` extension)

The order of problems in this list determines the order they appear on the site. This also means discussions can mix and match problems from different exams — you just list whatever problems you want.

### `problems/`

One markdown file per question, organized into subfolders by exam (e.g. `problems/fa25-final/q01.md`). The filename doesn't matter — order comes from the yml.

Each file follows this structure:

```markdown
# BEGIN PROB

Question text goes here.

# BEGIN SUBPROB

Subpart text here. Use ( ) for choose-one, [ ] for select-all.

( ) Option A
( ) Option B

# BEGIN SOLUTION

**Answer:** Option A

Explanation here.

# END SOLUTION

# END SUBPROB

# END PROB
```

To add a difficulty rating, add an `average` tag at the end of the problem with the Gradescope average score (0–100). The build script converts this to a star rating automatically:

```markdown
average: 62
```

### `docs/`

Auto-generated HTML — **never edit these files directly**. They are regenerated every time you run `run.py`. You need to commit them so the live site updates.

### `assets/images/`

Images used in problem files, organized by exam (e.g. `assets/images/fa25-final/`). To reference an image in a problem markdown file:

```markdown
![](../../assets/images/fa25-final/some-image.png)
```

---

## Style Guide

- **Answer:** should be bolded, followed by unbolded answer(s), comma-separated if it fits on one line, or each answer on a new line if it doesn't
- Use `( )` for choose one, `[ ]` for select all — add a space before the text of each option, no blank lines between options
- For subsubparts, use numbers followed by a period

### LaTeX → Markdown quick reference

| LaTeX | Markdown |
|---|---|
| `\begin{verbatim}` | ` ```py ` |
| `\end{verbatim}` | ` ``` ` |
| `"` | `'` |
| `\_` | `_` |
| `\texttt{` | `` ` `` |
| `\textbf{` | `**` |
| `\textit{` | `*` |
| `\bubble` | `( )` |
| `\correctbubble` | `( )` |
| `\squarebubble` | `[ ]` |
| `\correctsquarebubble` | `[ ]` |
| `\begin{subprob}` | `# BEGIN SUBPROB` |
| `\end{subprob}` | `# END SUBPROB` |
| `\begin{responsebox}` / `\begin{soln}` | `# BEGIN SOLUTION` |
| `\end{responsebox}` / `\end{soln}` | `# END SOLUTION` |
| `\begin{subprobset}` / `\end{subprobset}` | *(delete)* |
| `\bigskip` / `\noindent` | *(delete)* |

### Context to provide when adding a new exam

Include the following in the solutions or context blurb:
- All exams are individual (no collaboration allowed)
- `( )` = choose one, `[ ]` = select all; in their absence, students wrote code by hand
- In-person = on paper
- Select-all questions are graded as a sequence of true/false; partial credit assigned accordingly
- Students should have the DSC 10 reference sheet open when practicing

---

## Troubleshooting

- **`No module named yaml` or similar:** Make sure you're using `uv run python run.py`, not `python run.py`
- **Encoding errors:** Use `run-utf8.py` instead of `run.py`
- **Verify you're using the uv environment:** Run `uv run which python` — the path should point to `.venv/bin/python` inside the repo
