# latex-to-md.py
# Converts an exam .tex file to a set of .md files, one for each problem
# Usage: python latex-to-md.py exam.tex out_folder
# After running, out_folder will contain one .md file per problem in exam.tex
# NOTE: This script normalizes MC options to avoid wrapped/spaced options that break run.py parsing.

import os
import sys
import re

def replace_tags(prob_str):
    tags = {'probset': '', 
            'prob': 'PROB', 
            'soln': 'SOLUTION', 
            'subprob': 'SUBPROB', 
            'subprobset': ''}

    for tag in tags.keys():
        latex_brace = '{' + tag + '}'
        prob_str = prob_str.replace(f'\\begin{latex_brace}', f'# BEGIN {tags[tag]}\n\n' if tags[tag] else tags[tag]) \
                           .replace(f'\\end{latex_brace}', f'\n\n# END {tags[tag]}' if tags[tag] else tags[tag])

    # Remove point values
    prob_str = re.sub(r'(\[)?\(\d pts?\)(\])?', '', prob_str)

    # Convert correct bubbles
    regex_map = {r'\\correctbubble{(.*)}': '( )',
                 r'\\bubble{(.*)}': '( )',
                 r'\\correctsquarebubble{(.*)}': '[ ]',
                 r'\\squarebubble{(.*)}': '[ ]'}

    def make_repl(mc_bubble):
        def repl(matchobj):
            bubble_text = matchobj.group(1)
            # Flatten explicit LaTeX line breaks/indentation to avoid broken MC option lines in Markdown.
            bubble_text = re.sub(r'\\\\\s*\\hspace\*?\{[^}]*\}\s*', ' ', bubble_text)
            bubble_text = re.sub(r'\\\\\s*', ' ', bubble_text)
            bubble_text = re.sub(r'\s+', ' ', bubble_text).strip()
            return regex_map[mc_bubble] + ' ' + bubble_text
        return repl

    for mc_bubble in regex_map:
        prob_str = re.sub(mc_bubble, make_repl(mc_bubble), prob_str)

    return prob_str

def pandoc_tex_to_md(prob_str_tex):
    with open('temp.tex', 'w') as f:
        f.write(prob_str_tex)
    os.system('pandoc -s --wrap=none temp.tex -o temp.md')
    with open('temp.md', 'r') as f:
        text = f.read()
    os.remove('temp.tex')
    os.remove('temp.md')
    return text

def remove_leading_slash(prob_str_md):
    prob_str_md = prob_str_md.replace('\\#', '#') \
                             .replace('\\[X\\]', '[X]') \
                             .replace('\\(X\\)', '(X)') \
                             .replace('\\[ \\]', '[ ]') \
                             .replace('\\( \\)', '( )')

    return prob_str_md

def remove_blank_lines_between_mc_options(prob_str_md):
    def is_mc_option_line(line):
        return re.match(r'^\s*[\(\[][\sX][\)\]]\s+', line) is not None

    lines = prob_str_md.splitlines()
    cleaned_lines = []
    for i, line in enumerate(lines):
        if line.strip():
            cleaned_lines.append(line)
            continue

        prev_line = cleaned_lines[-1] if cleaned_lines else ''
        next_line = lines[i + 1] if i + 1 < len(lines) else ''

        if is_mc_option_line(prev_line) and is_mc_option_line(next_line):
            continue
        cleaned_lines.append(line)

    return '\n'.join(cleaned_lines)

def split_probs_to_files(prob_str_md):
    probs = re.findall(r'# BEGIN PROB[\W\w]*?# END PROB', prob_str_md)

    # Add # BEGIN SOLUTION, # END SOLUTION each time it's necessary
    new_probs = []
    for prob in probs:
        if '# END SUBPROB' in prob:
            new_prob = prob.replace('# END SUBPROB', '# BEGIN SOLUTION\n\n# END SOLUTION\n\n# END SUBPROB')
        else:
            new_prob = prob.replace('# END PROB', '# BEGIN SOLUTION\n\n# END SOLUTION\n\n# END PROB')
        new_probs.append(new_prob)
    return new_probs

def write_prob_files(probs, out_dir):
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)

    for i, prob in enumerate(probs):
        save_file_name = os.path.join(out_dir, 'q' + str(i+1).zfill(2) + '.md')
        with open(save_file_name, 'w') as f:
            f.write(prob)

def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()

if __name__ == '__main__':
    if len(sys.argv[1:]) != 2:
        raise ValueError(f'2 arguments required but {len(sys.argv[1:])} provided.')
    file_path = sys.argv[1]
    out_dir = sys.argv[2]

    # Step 1: Read as .tex
    file_as_tex = read_file(file_path)

    # Step 2: Make replacements
    prob_str_tex = replace_tags(file_as_tex)

    # Step 3: Call pandoc and remove leading slashes (e.g. \# -> #, \[X\] -> [X])
    prob_str_md = pandoc_tex_to_md(prob_str_tex)

    # print(prob_str_md[:10000])

    prob_str_md = remove_leading_slash(prob_str_md)
    prob_str_md = remove_blank_lines_between_mc_options(prob_str_md)

    # Step 4: Split by # BEGIN PROB
    probs = split_probs_to_files(prob_str_md)

    # Step 5: Write each prob to a separate file
    write_prob_files(probs, out_dir)
