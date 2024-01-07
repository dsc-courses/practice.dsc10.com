import yaml
import os
import glob
import regex as re
from bs4 import BeautifulSoup
import lxml
import shutil
import stat
import sys
import warnings
import time
warnings.simplefilter('ignore')

DST_FOLDER = 'docs'

GAUGE_COUNT = 0

def get_stars_from_average(avg):
    if avg >= 90:
        stars = 1
    elif avg >= 75:
        stars = 2
    elif avg >= 50:
        stars = 3
    elif avg >= 30:
        stars = 4
    else:
        stars = 5
    return stars * '⭐️'


def delete_folder(path):
    '''Needed for Windows...
       Taken from https://stackoverflow.com/questions/21261132/shutil-rmtree-to-remove-readonly-files
    '''

    def del_rw(action, name, exc):
        os.chmod(name, stat.S_IWRITE)
        os.remove(name)

    return shutil.rmtree(path, onerror=del_rw)

def format_assignment_name(name):
    '''Takes in a string like 'fa21-final' and returns 'Fall 2021 Final Exam
       Will need to update for discussions at some point <- lol these comments are out of date
    '''
    quarter, type = name.split('-')
    season, year = quarter[:2], quarter[2:]
    season = {'fa': 'Fall', 'wi': 'Winter', 'sp': 'Spring', 'su': 'Summer'}[season]
    year = '20' + year

    return season + ' ' + year + ' ' + type.title() + ' Exam'

def format_md_path(name):
    '''Example behavior is shown below.
    >>> format_md_path('problems/sp22-midterm/q7-merge')
    'problems/sp22-midterm/q7-merge.md'

    # new use case for discussion (when there's problem-specific context)
    >>> format_md_path('problems/sp22-midterm/q7-merge, problems/sp22-midterm/data-info-for-discussion')
    'problems/sp22-midterm/q7-merge.md, problems/sp22-midterm/data-info-for-discussion.md'
    
    '''
    if ',' not in name:
        return os.path.join('problems', f'{name}.md')
    else:
        names = name.split(', ')
        if len(names) > 2:
            raise Exception(f'Provided more than 2 files in a .yml file. For debugging: {name}')
        return format_md_path(names[0]) + ', ' + format_md_path(names[1])

def format_md_paths(names):
    paths = [format_md_path(name) for name in names]
    return paths

def read_html_config(path):
    f = open(path, 'r')
    r = f.read()
    f.close()
    return r + '\n\n'

def create_top_info(params, is_exam=True):

    inst_info = f"**Instructor(s):** {params['instructors']}" if is_exam else ''

    return f'''
[&#8592; return to practice.dsc10.com](../index.html)

---

{inst_info}

{params['context']}

---

'''
# {'_Note: Solutions are currently hidden, and will be made visible at a later date._' if not params['show_solution'] else ''}


def stitch(files, show_solution, toc=False):
    '''Stitches individual .md files into a longer .md string with problems'''
    paths = format_md_paths(files)
    out = '\n\n'

    if toc:
        # Format a table of contents here
        pass

    for i, path in enumerate(paths):
        # This case only happens for discussion worksheets, when we provide a question along with a "data info" sheet just for that question
        if ', ' in path:
            question_path, info_path = path.split(', ')
            question_text = open(question_path, 'r').read()
            info_text = open(info_path, 'r').read()

            # Need to place the info text at the start of the question text
            # So will replace the # BEGIN PROB in the question text with # BEGIN PROB {context}
            r = question_text.replace("# BEGIN PROB", f"# BEGIN PROB {info_text} <br><br>")
        else:
            r = open(path, 'r', encoding='UTF-8').read()

        q_out = process_problem(problem_str=r, problem_num=i+1, show_solution=show_solution)
        q_out += '\n\n\n---\n\n\n'

        out += q_out

    return out

# ---

def pandoc(s, kind='md', flags=''):
    '''Take in a string containing Markdown and return its HTML equivalent, via pandoc'''
    assert kind == 'tex' or kind == 'md', 'kind must be tex or md'

    if not os.path.exists('temp'):
        os.mkdir('temp')

    in_path = os.path.join('temp', f'temp.{kind}')
    in_file = open(in_path, 'w', encoding='UTF-8')
    in_file.write(s)
    in_file.close()

    src_path = os.path.join('temp', f'temp.{kind}')
    dst_path = os.path.join('temp', 'temp.html')
    os.system(f'pandoc -s --standalone --katex --from markdown-markdown_in_html_blocks+raw_html --metadata title=" " -s {src_path} {flags} -o {dst_path}')

    out_path = os.path.join('temp', 'temp.html')
    out_file = open(out_path, 'r', encoding='UTF-8') # CHANGED
    out_s = out_file.read()
    out_file.close()
    delete_folder('temp')

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

def process_MC_matches(matchobj):
    '''Helper function for process_MC'''
    global count

    match_str = matchobj.group()
    
    # Multiple choice (circular boxes)
    if match_str.count('( )') >= 2:
        exp = r'\( \) (.*)'
        input_type = 'radio'
        
    # Select all (square boxes)
    elif match_str.count('[ ]') >= 2:
        exp = r'\[ \] (.*)'
        input_type = 'checkbox'
        
    else:
        print(match_str)
        raise SyntaxError('How did this happen?')
        
    choices = re.findall(exp, match_str)
    out = '\n\n<ul class="task-list">\n'
    for choice in choices:
        processed_choice = pandoc(choice) # In case the choice includes Markdown
        processed_choice = str(BeautifulSoup(processed_choice, features='lxml').find('p')).replace('<p>', '').replace('</p>', '')
        out += f'<li><p><input type="{input_type}" disabled="" /> {processed_choice}</p></li>\n'
    
    out += '</ul>\n\n'
    
    return out

def process_MC(problem_str):
    '''Critical assumption: any problem with multiple choice or select all options has at least 2 choices'''

    extract_exp = r'\n\n([[(] [])] [\d\D]+?)\n\n'
    return re.sub(extract_exp, process_MC_matches, problem_str)


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
    problem_only = problem_only.replace('# BEGIN PROB', '').replace('# END PROB', '')

    # Process MC/SA boxes in problem_only
    problem_only = process_MC(problem_only)
    
    # Put it all together
    
    out = f'''
{heading} Problem {problem_num}

{problem_only}

{solution_processed}

    '''
    
    return out

SUBPART_REGEXP = r'# BEGIN SUBPROB([\d\D]*?)# END SUBPROB'
# subpart_count = 0

# def create_subpart_fn(problem_num, show_solution, heading):
#     def subpart_fn(matchobj):
#         global subpart_count
#         subpart_count += 1
#         match_str = re.findall(SUBPART_REGEXP, matchobj[0])[0]
#         subprob_num = str(problem_num) + f'.{subpart_count}'
#         return process_problem_no_subparts(match_str, subprob_num, show_solution, heading)
#     return subpart_fn

def process_problem_with_subparts(problem_str, problem_num, show_solution):
    # Extract any content before the first # BEGIN SUBPROB
    # preamble = problem_str[problem_str.index('# BEGIN PROB')+12:problem_str.index('# BEGIN SUBPROB')]
    
    # out = f'## Problem {problem_num}\n\n{preamble}<br>\n\n'

    problem_str = problem_str.replace('# BEGIN PROB', '').replace('# END PROB', '') \
                             .replace('# BEGIN PROBLEM', '').replace('# END PROBLEM', '')

    problem_str = f'## Problem {problem_num}\n{problem_str}'
    # other idea
    # while the number of matches is non-zero, replace the first match
    # while len(re.findall(SUBPART_REGEXP, out)) > 0L
    i = 0
    while len(re.findall(SUBPART_REGEXP, problem_str)) > 0:
        # Find the next unprocessed question
        top_match = re.findall(SUBPART_REGEXP, problem_str)[0]

        top_match_processed = process_problem_no_subparts(top_match, 
                                                          str(problem_num) + f'.{i+1}',
                                                          show_solution,
                                                          heading='###')

        top_match_processed = '<br>\n' + top_match_processed.replace(r'\ '[0], r'\\ '[:-1]) + '\n<br>'
        problem_str = re.sub(SUBPART_REGEXP, top_match_processed, problem_str, count=1)
        i += 1

    # parts = re.findall(r, problem_str)

    # here, instead of adding to the output, replace each occurrence of a match with its conversion

    # out += re.sub(SUBPART_REGEXP, create_subpart_fn(problem_num, show_solution, heading='###'), problem_str)

    # for i, part in enumerate(parts):
        # out += process_problem_no_subparts(part, str(problem_num) + f'.{i+1}', show_solution, heading='###') + '\n\n<br>\n\n'
        
    # Remove unnecessary spacing
    problem_str = problem_str.replace('<br>\n\n<br>', '<br>')
    return problem_str

# renders stars
AVG_REGEXP = r'<average>(\d+)<\/average>'
def stars_repl(matchobj, exam=False):
    # global GAUGE_COUNT
    # GAUGE_COUNT += 1
    avg_int = int(re.findall(AVG_REGEXP, matchobj[0])[0])
    stars = get_stars_from_average(avg_int)
    kind = 'exam' if exam else 'problem'
    return f'<hr><h5>Difficulty: {stars}</h5><p>The average score on this {kind} was {avg_int}%.'

# TOPICS_REGEXP = r'<topics>([A-Za-z ,]+)<\/topics>'
# def topics_extraction(matchobj, exam=False):

def process_problem(problem_str, problem_num, show_solution):

    assert problem_str.count('# BEGIN PROB') == problem_str.count('# END PROB') == 1, 'Need exactly one # BEGIN PROB and # END PROB pair'
    
    problem_str = re.sub(AVG_REGEXP, stars_repl, problem_str)

    if '# BEGIN SUBPROB' in problem_str:
        assert problem_str.count('# BEGIN SUBPROB') == problem_str.count('# END SUBPROB'), f'Different number of # BEGIN SUBPROB and # END SUBPROB in Problem {problem_num}'
        return process_problem_with_subparts(problem_str, problem_num, show_solution)
    
    else:
        return process_problem_no_subparts(problem_str, problem_num, show_solution)

# ---

def process_page(path, is_exam=True):
    '''Takes in a path to a YML file and returns a MD file with everything, along with the title of the page (which we access through params). Defaults to processing exams.'''
    r_file = open(path, 'r')
    r = r_file.read()
    r_file.close()
    params = yaml.safe_load(r)

    if 'show_solution' not in params.keys():
        params['show_solution'] = True
    
    out = read_html_config('include-head.html')
    out += create_top_info(params, is_exam=is_exam)

    # Add information for the entire exam
    if 'data_info' in params.keys():
        info_path = os.path.join('problems', f'{params["data_info"]}.md')
        info_file = open(info_path, 'r', encoding='UTF-8')
        info = info_file.read()
        info_file.close()

        out += info + '\n\n --- \n\n'

    out += stitch(params['problems'], params['show_solution'])

    out += '$$ $$' # to enable latex always

    if 'footer' in params.keys():
        out += f'\n\n {params["footer"]} \n\n'

    # Temporary summer add-on to collect feedback
    out += '''
---

#### 👋 Feedback: Find an error? Still confused? Have a suggestion? <a href="https://forms.gle/WZ71FchnXU1K154d7">Let us know here</u></a>.

---
    
'''

    if 'title' in params.keys():
        title = params['title']
    else:
        title = None

    # TODO: easily extract all files for a single final exam
    # TODO: format PDFs for printing: https://stackoverflow.com/problems/1664049/can-i-force-a-page-break-in-html-printing
    return out, title

def write_page(path, called_from_write_all_pages=False):
    '''Takes in a path to a YML file and writes the MD file, runs pandoc, deletes the MD file'''

    sep = '/' if '/' in path else '\\'
    assignment_name = path.split(sep)[-1].replace('.yml', '')

    # is_discussion = 'disc' in path
    is_exam = 'midterm' in path or 'final' in path

    # Generate the Markdown
    page, title = process_page(path, is_exam=is_exam)

    # Write the Markdown
    open_path = os.path.join(DST_FOLDER, f'{assignment_name}.md')
    f = open(open_path, 'w', encoding='UTF-8') # CHANGED
    f.write(page)
    f.close()

    # Convert to HTML
    dst_folder_path = os.path.join(DST_FOLDER, assignment_name)

    if not os.path.exists(dst_folder_path):
        os.mkdir(dst_folder_path) # make folder

    # If an assignment title wasn't defined in params, try and create it using the file name
    # For discussions at least, we will specify it and process_page will return it
    if not title:
        title = format_assignment_name(assignment_name)
    src_path = os.path.join(DST_FOLDER, f'{assignment_name}.md')
    dst_path = os.path.join(DST_FOLDER, assignment_name, 'index.html')
    css_path = os.path.join('..', 'assets', 'theme.css')
    os.system(f'pandoc -s --standalone --katex --from markdown-markdown_in_html_blocks+raw_html -c {css_path} --metadata title="{title}" {src_path} -o {dst_path}')

    # Delete the intermediate Markdown
    os.remove(src_path)

    # Copy over the images for just that page, but only if called individually
    # If called in bulk, this shouldn't be run, since this is handled by
    # write_all_pages
    if not called_from_write_all_pages:
        src_path = os.path.join('assets', 'images', assignment_name)
        dst_path = os.path.join(DST_FOLDER, src_path)
        if os.path.exists(src_path):
            if os.path.exists(dst_path):
                shutil.rmtree(dst_path)
            shutil.copytree(src_path, dst_path)

def update_page(path):
    '''Doesn't work for discussion files, yet.'''
    sep = '/' if '/' in path else '\\'
    assignment_name = path.split(sep)[-1].replace('.yml', '')

    # Generate the Markdown
    page = process_page(path)

    # Write the Markdown
    open_path = os.path.join(DST_FOLDER, f'{assignment_name}.md')
    f = open(open_path, 'w')
    f.write(page)
    f.close()

    dst_folder_path = os.path.join(DST_FOLDER, assignment_name)
    # Make the function much faster by not requiring the folder to be recreated
    if not os.path.exists(dst_folder_path):
        os.mkdir(dst_folder_path) # make folder
    
    title = format_assignment_name(assignment_name)
    src_path = os.path.join(DST_FOLDER, f'{assignment_name}.md')
    # Use a temp HTML file to write over than the main one inorder to minimize delay on viewing the page
    tmp_path = os.path.join(DST_FOLDER, assignment_name, 'temp.html')
    dst_path = os.path.join(DST_FOLDER, assignment_name, 'index.html')
    css_path = os.path.join('..', 'assets', 'theme.css')
    os.system(f'pandoc -s --standalone --katex --from markdown-markdown_in_html_blocks+raw_html -c {css_path} --metadata title="{title}" {src_path} -o {tmp_path}')

    # Delete the intermediate Markdown
    os.remove(src_path)
    if os.path.exists(dst_path):
        os.remove(dst_path)
    os.rename(tmp_path, dst_path)


def write_all_pages(dir='pages'):
    '''Assumes all pages are specified in YML'''

    if os.path.exists(DST_FOLDER):
        delete_folder(DST_FOLDER)
    os.mkdir(DST_FOLDER)

    # Add CNAME back – this is a massive hack, but whatever
    cname_path = os.path.join(DST_FOLDER, 'CNAME')
    cname = open(cname_path, 'w')
    cname.write('practice.dsc10.com')
    cname.close()

    page_paths = os.path.join(dir, '*', '*.yml')
    all_paths = glob.glob(page_paths)
    for path in all_paths:
        write_page(path, called_from_write_all_pages=True)

    # Copy over images/scripts
    # os.mkdir(f'{DST_FOLDER}/assets/')
    # os.system(f'cp -R assets/ {DST_FOLDER}/assets/')
    dst_path = os.path.join(DST_FOLDER, 'assets')
    shutil.copytree('assets', dst_path)

def create_index():
    f_index = open('index.md', 'r')
    index_src = f_index.read()
    f_index.close()

    out = read_html_config('include-head.html')
    out += '\n' + index_src

    src_path = os.path.join(DST_FOLDER, 'index.md')
    f = open(src_path, 'w')
    f.write(out)
    f.close()

    css_path = os.path.join('assets', 'theme.css')
    src_path = os.path.join(DST_FOLDER, 'index.md')
    dst_path = os.path.join(DST_FOLDER, 'index.html')
    os.system(f'pandoc -c {css_path} -s {src_path} -o {dst_path}')
    os.remove(src_path)

    # Remove pre-defined title
    src_path = os.path.join(DST_FOLDER, 'index.html')
    f = open(src_path, 'r')
    r = f.read()
    f.close()

    r = re.sub(r'<h1 class="title">.*?</h1>', '', r)
    f = open(src_path, 'w')
    f.write(r)
    f.close()

if __name__ == '__main__':
    # No arguments: run all
    if len(sys.argv) == 1:
        write_all_pages()
        create_index()

    elif sys.argv[1] == 'index':
        create_index()

    elif sys.argv[1] == "listen":
            # Obtain the file paths for all markdown files.
            # We will be looking to see if the modification time changes to signal an update
            page_paths = os.path.join('pages', '*', '*.yml')
            all_paths = glob.glob(page_paths)
            
            # This creates an array that contains an entry for each yml file containing all the yml and md paths related to it.
            # These are all the files we would want to check for edits.
            listen_files = []
            for path in all_paths:
                r_file = open(path, 'r')
                r = r_file.read()
                r_file.close()
                params = yaml.safe_load(r)
                listen_files += [[path] + list(map(lambda x: os.path.join("problems",x + ".md"),params.get("problems",[])))]

            # This uses the same format as the listen_files variable to store the timestamp info for each file.
            # Timestamps are used to check for file changes to signal updates.
            cached_stamp = []
            for i,section in enumerate(listen_files):
                cached_stamp += [[]]
                for file in section:
                    cached_stamp[i] += [os.stat(file).st_mtime]


            # Beginning of listening loop.
            # This is based on the second response to this post: https://stackoverflow.com/questions/182197/how-do-i-watch-a-file-for-changes            
            while True:
                try:
                    # Every second
                    time.sleep(1)
                    # For each markdown file
                    for i, section in enumerate(listen_files):
                        for j, path in enumerate(section):
                            # Get the last modified time stamp
                            stamp = os.stat(path).st_mtime
                            # Compare to currently cached timestamp
                            # If its different then the file in questions has been modified and needs to be reflected on the html file
                            if stamp != cached_stamp[i][j]:
                                # When a yml file is updated, we also need to update the files listened to reflect changes
                                # to the problem section
                                if ".yml" in path:
                                    print(f"Updating tracked problems for {section[0]}")
                                    r_file = open(path, 'r')
                                    r = r_file.read()
                                    r_file.close()
                                    new_problems = yaml.safe_load(r).get("problems",[])
                                    # Replace old listened files with new listened files to reflects changes to the .yml file
                                    listen_files[i] = [path] + list(map(lambda x: os.path.join("problems",x + ".md"),new_problems))
                                    cached_stamp[i] = [os.stat(file).st_mtime for file in listen_files[i]]
                                # Update cached timestamp to reflect the update
                                cached_stamp[i][j] = stamp
                                print(f"Updating: {section[0]}")
                                # Update the new HTML folder
                                update_page(section[0])
                                print("Finished Updating! Refresh the .html file on your browser to see changes!")
                                break
                except KeyboardInterrupt:
                    break
    else:
        for page in sys.argv[1:]:
            write_page(page)
