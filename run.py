import yaml
import os
import glob
import re
from bs4 import BeautifulSoup
import lxml

DST_FOLDER = 'docs'

def format_assignment_name(name):
    '''Takes in a string like 'fa21-final' and returns 'Fall 2021 Final Exam
       Will need to update for discussions at some point
    '''
    quarter, type = name.split('-')
    season, year = quarter[:2], quarter[2:]
    season = {'fa': 'Fall', 'wi': 'Winter', 'sp': 'Spring', 'su': 'Summer'}[season]
    year = '20' + year

    return season + ' ' + year + ' ' + type.title() + ' Exam'

def format_md_path(name):
    path = f'problems/{name}.md'
    return path

def format_md_paths(names):
    paths = [format_md_path(name) for name in names]
    return paths

def read_html_config(path):
    r = open(path, 'r').read()
    return r + '\n\n'

def create_top_info(params):
    return f'''
[&#8592; return to practice.dsc10.com](../index.html)

---

**Instructor(s):** {params['instructors']}

{params['context']}

{'_Note: Solutions are currently hidden, and will be made visible at a later date._' if not params['show_solution'] else ''}

---

'''

def stitch(files, show_solution, toc=False):
    '''Stitches individual .md files into a longer .md string with problems'''
    paths = format_md_paths(files)
    out = '\n\n'

    if toc:
        # Format a table of contents here
        pass

    for i, path in enumerate(paths):
        r = open(path, 'r').read()
        q_out = process_problem(problem_str=r, problem_num=i+1, show_solution=show_solution)
        q_out += '\n\n\n---\n\n\n'

        out += q_out

    return out

# ---

def pandoc(s, kind='md', flags=''):
    '''Take in a string containing Markdown and return its HTML equivalent, via pandoc'''
    assert kind == 'tex' or kind == 'md', 'kind must be tex or md'

    if not os.path.exists('temp'):
        os.system('mkdir temp')

    in_file = open(f'temp/temp.{kind}', 'w')
    in_file.write(s)
    in_file.close()

    os.system(f'pandoc --standalone --from markdown-markdown_in_html_blocks+raw_html --metadata title=" " -s temp/temp.{kind} {flags} -o temp/temp.html')

    out_file = open(f'temp/temp.html', 'r')
    out_s = out_file.read()
    os.system('rm -r temp')

    soup = BeautifulSoup(out_s, features='lxml')
    return str(soup.find('body')).replace('<body>', '').replace('</body>', '')

def add_solution_box(solution_str, problem_num):
    '''solution_str must be an HTML containing the solution text.'''

    # Using . in attribute names does not work
    if isinstance(problem_num, str) and '.' in problem_num:
        problem_num = problem_num.replace('.', '_')

    out = f'''
<div class="accordion" id="accordionExample">
<div class="accordion-item">
<h2 class="accordion-header" id="heading{problem_num}">
<button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapse{problem_num}" aria-expanded="true" aria-controls="collapse{problem_num}">
Click to view the solution.
</button>
</h2>
<div id="collapse{problem_num}" class="accordion-collapse collapse collapse" aria-labelledby="heading{problem_num}" data-bs-parent="#accordionExample">
<div class="accordion-body">
{solution_str}
</div>
</div>
</div>
</div>


'''
    
    return out

def process_problem_no_subparts(problem_str, problem_num, show_solution, heading='##'):
    '''Used for problems with no subparts, and to process individual subparts'''
    
    if show_solution:
        # Extract solution    
        if '# BEGIN SOLUTION' in problem_str:
            sep = 'SOLUTION'
        elif '# BEGIN SOLN' in problem_str:
            sep = 'SOLN'
        else:
            raise AssertionError('Neither # BEGIN SOLUTION nor # BEGIN SOLN were found')
            
        exp = f'# BEGIN {sep}([\d\D]*?)# END {sep}'
            
        solution_str = re.findall(exp, problem_str)
        
        if len(solution_str) != 1:
            raise AssertionError('This should not happen')
        
        # Pass solution_str through pandoc first, then give it the solution box
        solution_str_html = pandoc(solution_str[0])
        solution_processed = add_solution_box(solution_str_html, problem_num)

        problem_only = re.sub(exp, '', problem_str)

    else:

        solution_processed = ''

        # If the solution is there, we need to remove it first
        contains_solution = False

        if '# BEGIN SOLUTION' in problem_str:
            sep = 'SOLUTION'
            contains_solution = True
        elif '# BEGIN SOLN' in problem_str:
            sep = 'SOLN'
            contains_solution = True
        else:
            # No solution was provided
            pass

        if contains_solution:
            exp = f'# BEGIN {sep}([\d\D]*?)# END {sep}'
            problem_only = re.sub(exp, '', problem_str)
        else:
            problem_only = problem_str

    # Get the problem text
    problem_only = problem_only.replace('# BEGIN PROB', '').replace('# END PROB', '').strip('\n')
    
    # Put it all together
    
    out = f'''
{heading} Problem {problem_num}

{problem_only}

{solution_processed}
    '''
    
    return out

def process_problem_with_subparts(problem_str, problem_num, show_solution):

    # Extract any content before the first # BEGIN SUBPROB
    preamble = problem_str[problem_str.index('# BEGIN PROB')+12:problem_str.index('# BEGIN SUBPROB')]
    
    out = f'## Problem {problem_num}\n\n{preamble}<br>\n\n'

    parts = re.findall(r'# BEGIN SUBPROB([\d\D]*?)# END SUBPROB', problem_str)

    for i, part in enumerate(parts):
        out += process_problem_no_subparts(part, str(problem_num) + f'.{i+1}', show_solution, heading='###') + '\n\n<br>\n\n'
        
    return out

def process_problem(problem_str, problem_num, show_solution):
    assert problem_str.count('# BEGIN PROB') == problem_str.count('# END PROB') == 1, 'Need exactly one # BEGIN PROB and # END PROB pair'
    
    if '# BEGIN SUBPROB' in problem_str:
        assert problem_str.count('# BEGIN SUBPROB') == problem_str.count('# END SUBPROB'), 'Different number of # BEGIN SUBPROB and # END SUBPROB'
        return process_problem_with_subparts(problem_str, problem_num, show_solution)
    
    else:
        return process_problem_no_subparts(problem_str, problem_num, show_solution)

# ---

def process_page(path):
    '''Takes in a path to a YML file and returns a MD file with everything.'''
    r = open(path, 'r').read()
    params = yaml.safe_load(r)

    if 'show_solution' not in params.keys():
        params['show_solution'] = True
    
    out = read_html_config('include-head.html')
    out += create_top_info(params)

    out += stitch(params['problems'], params['show_solution'])

    # TODO: easily extract all files for a single final exam

    # TODO: format PDFs for printing: https://stackoverflow.com/problems/1664049/can-i-force-a-page-break-in-html-printing
    return out

def write_page(path):
    '''Takes in a path to a YML file and writes the MD file, runs pandoc, deletes the MD file'''

    assignment_name = path.split('/')[-1].replace('.yml', '')

    # Generate the Markdown
    page = process_page(path)

    # Write the Markdown
    f = open(f'{DST_FOLDER}/{assignment_name}.md', 'w')
    f.write(page)
    f.close()

    # Convert to HTML
    os.system(f'mkdir -p {DST_FOLDER}/{assignment_name}') # make folder

    title = format_assignment_name(assignment_name)
    src_path = f'{DST_FOLDER}/{assignment_name}.md'
    dst_path = f'{DST_FOLDER}/{assignment_name}/index.html'
    os.system(f'pandoc -s --standalone --from markdown-markdown_in_html_blocks+raw_html -c ../assets/theme.css --metadata title="{title}" {src_path} -o {dst_path}')

    # Delete the intermediate Markdown
    os.system(f'rm {DST_FOLDER}/{assignment_name}.md')

def write_all_pages(dir='pages'):
    '''Assumes all pages are specified in YML'''

    if os.path.exists(DST_FOLDER):
        os.system(f'rm -r {DST_FOLDER}')
    os.system(f'mkdir {DST_FOLDER}')

    all_paths = glob.glob(f'{dir}/*/*.yml')
    for path in all_paths:
        write_page(path)

    # Copy over images/scripts
    os.system(f'mkdir -p {DST_FOLDER}/assets/')
    os.system(f'cp -R assets/ {DST_FOLDER}/assets/')

def create_index():
    index_src = open('index.md', 'r').read()
    out = read_html_config('include-head.html')
    out += '\n' + index_src
    f = open(f'{DST_FOLDER}/index.md', 'w')
    f.write(out)
    f.close()
    os.system(f'pandoc -c assets/theme.css -s {DST_FOLDER}/index.md -o {DST_FOLDER}/index.html')
    os.system(f'rm -r {DST_FOLDER}/index.md')

    # Remove pre-defined title
    f = open(f'{DST_FOLDER}/index.html', 'r')
    r = f.read()
    f.close()

    r = re.sub(r'<h1 class="title">.*?</h1>', '', r)
    f = open(f'{DST_FOLDER}/index.html', 'w')
    f.write(r)
    f.close()
    
if __name__ == '__main__':
    write_all_pages()
    create_index()