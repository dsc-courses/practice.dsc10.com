# import yaml
# import os
# import glob
# import regex as re
# from bs4 import BeautifulSoup
# import lxml
# import shutil
# import stat
# import sys
# import warnings
# import time
# warnings.simplefilter('ignore')

# DST_FOLDER = 'docs'

# GAUGE_COUNT = 0

# def get_stars_from_average(avg):
#     if avg >= 90:
#         stars = 1
#     elif avg >= 75:
#         stars = 2
#     elif avg >= 50:
#         stars = 3
#     elif avg >= 30:
#         stars = 4
#     else:
#         stars = 5
#     return stars * '⭐️'


# def delete_folder(path):
#     '''Needed for Windows...
#        Taken from https://stackoverflow.com/questions/21261132/shutil-rmtree-to-remove-readonly-files
#     '''

#     def del_rw(action, name, exc):
#         os.chmod(name, stat.S_IWRITE)
#         os.remove(name)

#     return shutil.rmtree(path, onerror=del_rw)

# def format_assignment_name(name):
#     '''Takes in a string like 'fa21-final' and returns 'Fall 2021 Final Exam
#        Will need to update for discussions at some point <- lol these comments are out of date
#     '''
#     quarter, type = name.split('-')
#     season, year = quarter[:2], quarter[2:]
#     season = {'fa': 'Fall', 'wi': 'Winter', 'sp': 'Spring', 'su': 'Summer'}[season]
#     year = '20' + year

#     return season + ' ' + year + ' ' + type.title() + ' Exam'

# def format_md_path(name):
#     '''Example behavior is shown below.
#     >>> format_md_path('problems/sp22-midterm/q7-merge')
#     'problems/sp22-midterm/q7-merge.md'

#     # new use case for discussion (when there's problem-specific context)
#     >>> format_md_path('problems/sp22-midterm/q7-merge, problems/sp22-midterm/data-info-for-discussion')
#     'problems/sp22-midterm/q7-merge.md, problems/sp22-midterm/data-info-for-discussion.md'
    
#     '''
#     if ',' not in name:
#         return os.path.join('problems', f'{name}.md')
#     else:
#         names = name.split(', ')
#         if len(names) > 2:
#             raise Exception(f'Provided more than 2 files in a .yml file. For debugging: {name}')
#         return format_md_path(names[0]) + ', ' + format_md_path(names[1])

# def format_md_paths(names):
#     paths = [format_md_path(name) for name in names]
#     return paths

# def read_html_config(path):
#     f = open(path, 'r')
#     r = f.read()
#     f.close()
#     return r + '\n\n'

# def create_top_info(params, is_exam=True):

#     inst_info = f"**Instructor(s):** {params['instructors']}" if is_exam else ''

#     return f'''
# [&#8592; return to practice.dsc10.com](../index.html)

# ---

# {inst_info}

# {params['context']}

# ---

# '''
# # {'_Note: Solutions are currently hidden, and will be made visible at a later date._' if not params['show_solution'] else ''}


# def stitch(files, show_solution, toc=False):
#     '''Stitches individual .md files into a longer .md string with problems'''
#     paths = format_md_paths(files)
#     out = '\n\n'

#     if toc:
#         # Format a table of contents here
#         pass

#     for i, path in enumerate(paths):
#         # This case only happens for discussion worksheets, when we provide a question along with a "data info" sheet just for that question
#         if ', ' in path:
#             question_path, info_path = path.split(', ')
#             question_text = open(question_path, 'r').read()
#             info_text = open(info_path, 'r').read()

#             # Need to place the info text at the start of the question text
#             # So will replace the # BEGIN PROB in the question text with # BEGIN PROB {context}
#             r = question_text.replace("# BEGIN PROB", f"# BEGIN PROB {info_text} <br><br>")
#         else:
#             r = open(path, 'r', encoding='UTF-8').read()

#         q_out = process_problem(problem_str=r, problem_num=i+1, show_solution=show_solution)
#         q_out += '\n\n\n---\n\n\n'

#         out += q_out

#     return out

# # ---

# def pandoc(s, kind='md', flags=''):
#     '''Take in a string containing Markdown and return its HTML equivalent, via pandoc'''
#     assert kind == 'tex' or kind == 'md', 'kind must be tex or md'

#     if not os.path.exists('temp'):
#         os.mkdir('temp')

#     in_path = os.path.join('temp', f'temp.{kind}')
#     in_file = open(in_path, 'w', encoding='UTF-8')
#     in_file.write(s)
#     in_file.close()

#     src_path = os.path.join('temp', f'temp.{kind}')
#     dst_path = os.path.join('temp', 'temp.html')
#     os.system(f'pandoc -s --standalone --katex --from markdown-markdown_in_html_blocks+raw_html --metadata title=" " -s {src_path} {flags} -o {dst_path}')

#     out_path = os.path.join('temp', 'temp.html')
#     out_file = open(out_path, 'r', encoding='UTF-8') # CHANGED
#     out_s = out_file.read()
#     out_file.close()
#     delete_folder('temp')

#     soup = BeautifulSoup(out_s, features='lxml')
#     return str(soup.find('body')).replace('<body>', '').replace('</body>', '')

# def add_solution_box(solution_str, problem_num):
#     '''solution_str must be an HTML containing the solution text.'''

#     # Using . in attribute names does not work
#     if isinstance(problem_num, str) and '.' in problem_num:
#         problem_num = problem_num.replace('.', '_')

#     out = f'''
# <div class="accordion" id="accordionExample">
# <div class="accordion-item">
# <h2 class="accordion-header" id="heading{problem_num}">
# <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapse{problem_num}" aria-expanded="true" aria-controls="collapse{problem_num}">
# Click to view the solution.
# </button>
# </h2>
# <div id="collapse{problem_num}" class="accordion-collapse collapse collapse" aria-labelledby="heading{problem_num}" data-bs-parent="#accordionExample">
# <div class="accordion-body">
# {solution_str}
# </div>
# </div>
# </div>
# </div>


# '''
    
#     return out

# def process_MC_matches(matchobj):
#     '''Helper function for process_MC'''
#     global count

#     match_str = matchobj.group()
    
#     # Multiple choice (circular boxes)
#     if match_str.count('( )') >= 2:
#         exp = r'\( \) (.*)'
#         input_type = 'radio'
        
#     # Select all (square boxes)
#     elif match_str.count('[ ]') >= 2:
#         exp = r'\[ \] (.*)'
#         input_type = 'checkbox'
        
#     else:
#         print(match_str)
#         raise SyntaxError('How did this happen?')
        
#     choices = re.findall(exp, match_str)
#     out = '\n\n<ul class="task-list">\n'
#     for choice in choices:
#         processed_choice = pandoc(choice) # In case the choice includes Markdown
#         processed_choice = str(BeautifulSoup(processed_choice, features='lxml').find('p')).replace('<p>', '').replace('</p>', '')
#         out += f'<li><p><input type="{input_type}" disabled="" /> {processed_choice}</p></li>\n'
    
#     out += '</ul>\n\n'
    
#     return out

# def process_MC(problem_str):
#     '''Critical assumption: any problem with multiple choice or select all options has at least 2 choices'''

#     extract_exp = r'\n\n([[(] [])] [\d\D]+?)\n\n'
#     return re.sub(extract_exp, process_MC_matches, problem_str)


# def process_problem_no_subparts(problem_str, problem_num, show_solution, heading='##'):
#     '''Used for problems with no subparts, and to process individual subparts'''
    
#     if show_solution:
#         # Extract solution    
#         if '# BEGIN SOLUTION' in problem_str:
#             sep = 'SOLUTION'
#         elif '# BEGIN SOLN' in problem_str:
#             sep = 'SOLN'
#         else:
#             raise AssertionError('Neither # BEGIN SOLUTION nor # BEGIN SOLN were found')
            
#         pattern = r"([\d\D]*?)"
#         exp = f"# BEGIN {sep}{pattern}# END {sep}"

            
#         solution_str = re.findall(exp, problem_str)
        
#         if len(solution_str) != 1:
#             raise AssertionError('This should not happen')
        
#         # Pass solution_str through pandoc first, then give it the solution box
#         solution_str_html = pandoc(solution_str[0])
#         solution_processed = add_solution_box(solution_str_html, problem_num)

#         problem_only = re.sub(exp, '', problem_str)

#     else:

#         solution_processed = ''

#         # If the solution is there, we need to remove it first
#         contains_solution = False

#         if '# BEGIN SOLUTION' in problem_str:
#             sep = 'SOLUTION'
#             contains_solution = True
#         elif '# BEGIN SOLN' in problem_str:
#             sep = 'SOLN'
#             contains_solution = True
#         else:
#             # No solution was provided
#             pass

#         if contains_solution:
#             raw_pattern = r"([\d\D]*?)"
#             exp = f"# BEGIN {sep}{raw_pattern}# END {sep}"
#             problem_only = re.sub(exp, '', problem_str)
#         else:
#             problem_only = problem_str

#     # Get the problem text
#     problem_only = problem_only.replace('# BEGIN PROB', '').replace('# END PROB', '')

#     # Process MC/SA boxes in problem_only
#     problem_only = process_MC(problem_only)
    
#     # Put it all together
    
#     out = f'''
# {heading} Problem {problem_num}

# {problem_only}

# {solution_processed}

#     '''
    
#     return out

# SUBPART_REGEXP = r'# BEGIN SUBPROB([\d\D]*?)# END SUBPROB'
# # subpart_count = 0

# # def create_subpart_fn(problem_num, show_solution, heading):
# #     def subpart_fn(matchobj):
# #         global subpart_count
# #         subpart_count += 1
# #         match_str = re.findall(SUBPART_REGEXP, matchobj[0])[0]
# #         subprob_num = str(problem_num) + f'.{subpart_count}'
# #         return process_problem_no_subparts(match_str, subprob_num, show_solution, heading)
# #     return subpart_fn

# def process_problem_with_subparts(problem_str, problem_num, show_solution):
#     # Extract any content before the first # BEGIN SUBPROB
#     # preamble = problem_str[problem_str.index('# BEGIN PROB')+12:problem_str.index('# BEGIN SUBPROB')]
    
#     # out = f'## Problem {problem_num}\n\n{preamble}<br>\n\n'

#     problem_str = problem_str.replace('# BEGIN PROB', '').replace('# END PROB', '') \
#                              .replace('# BEGIN PROBLEM', '').replace('# END PROBLEM', '')

#     problem_str = f'## Problem {problem_num}\n{problem_str}'
#     # other idea
#     # while the number of matches is non-zero, replace the first match
#     # while len(re.findall(SUBPART_REGEXP, out)) > 0L
#     i = 0
#     while len(re.findall(SUBPART_REGEXP, problem_str)) > 0:
#         # Find the next unprocessed question
#         top_match = re.findall(SUBPART_REGEXP, problem_str)[0]

#         top_match_processed = process_problem_no_subparts(top_match, 
#                                                           str(problem_num) + f'.{i+1}',
#                                                           show_solution,
#                                                           heading='###')

#         top_match_processed = '<br>\n' + top_match_processed.replace(r'\ '[0], r'\\ '[:-1]) + '\n<br>'
#         problem_str = re.sub(SUBPART_REGEXP, top_match_processed, problem_str, count=1)
#         i += 1

#     # parts = re.findall(r, problem_str)

#     # here, instead of adding to the output, replace each occurrence of a match with its conversion

#     # out += re.sub(SUBPART_REGEXP, create_subpart_fn(problem_num, show_solution, heading='###'), problem_str)

#     # for i, part in enumerate(parts):
#         # out += process_problem_no_subparts(part, str(problem_num) + f'.{i+1}', show_solution, heading='###') + '\n\n<br>\n\n'
        
#     # Remove unnecessary spacing
#     problem_str = problem_str.replace('<br>\n\n<br>', '<br>')
#     return problem_str

# # renders stars
# AVG_REGEXP = r'<average>(\d+)<\/average>'
# def stars_repl(matchobj, exam=False):
#     # global GAUGE_COUNT
#     # GAUGE_COUNT += 1
#     avg_int = int(re.findall(AVG_REGEXP, matchobj[0])[0])
#     stars = get_stars_from_average(avg_int)
#     kind = 'exam' if exam else 'problem'
#     return f'<hr><h5>Difficulty: {stars}</h5><p>The average score on this {kind} was {avg_int}%.'

# # TOPICS_REGEXP = r'<topics>([A-Za-z ,]+)<\/topics>'
# # def topics_extraction(matchobj, exam=False):

# def process_problem(problem_str, problem_num, show_solution):

#     assert problem_str.count('# BEGIN PROB') == problem_str.count('# END PROB') == 1, 'Need exactly one # BEGIN PROB and # END PROB pair'
    
#     problem_str = re.sub(AVG_REGEXP, stars_repl, problem_str)

#     if '# BEGIN SUBPROB' in problem_str:
#         assert problem_str.count('# BEGIN SUBPROB') == problem_str.count('# END SUBPROB'), f'Different number of # BEGIN SUBPROB and # END SUBPROB in Problem {problem_num}'
#         return process_problem_with_subparts(problem_str, problem_num, show_solution)
    
#     else:
#         return process_problem_no_subparts(problem_str, problem_num, show_solution)

# # ---

# def process_page(path, is_exam=True):
#     '''Takes in a path to a YML file and returns a MD file with everything, along with the title of the page (which we access through params). Defaults to processing exams.'''
#     r_file = open(path, 'r')
#     r = r_file.read()
#     r_file.close()
#     params = yaml.safe_load(r)

#     if 'show_solution' not in params.keys():
#         params['show_solution'] = True
    
#     out = read_html_config('include-head.html')
#     out += create_top_info(params, is_exam=is_exam)

#     # Add information for the entire exam
#     if 'data_info' in params.keys():
#         info_path = os.path.join('problems', f'{params["data_info"]}.md')
#         info_file = open(info_path, 'r', encoding='UTF-8')
#         info = info_file.read()
#         info_file.close()

#         out += info + '\n\n --- \n\n'

#     out += stitch(params['problems'], params['show_solution'])

#     out += '$$ $$' # to enable latex always

#     if 'footer' in params.keys():
#         out += f'\n\n {params["footer"]} \n\n'

#     # Temporary summer add-on to collect feedback
#     out += '''
# ---

# #### 👋 Feedback: Find an error? Still confused? Have a suggestion? <a href="https://forms.gle/WZ71FchnXU1K154d7">Let us know here</u></a>.

# ---
    
# '''

#     if 'title' in params.keys():
#         title = params['title']
#     else:
#         title = None

#     # TODO: easily extract all files for a single final exam
#     # TODO: format PDFs for printing: https://stackoverflow.com/problems/1664049/can-i-force-a-page-break-in-html-printing
#     return out, title

# def write_page(path, called_from_write_all_pages=False):
#     '''Takes in a path to a YML file and writes the MD file, runs pandoc, deletes the MD file'''

#     sep = '/' if '/' in path else '\\'
#     assignment_name = path.split(sep)[-1].replace('.yml', '')

#     # is_discussion = 'disc' in path
#     is_exam = 'midterm' in path or 'final' in path

#     # Generate the Markdown
#     page, title = process_page(path, is_exam=is_exam)

#     # Write the Markdown
#     open_path = os.path.join(DST_FOLDER, f'{assignment_name}.md')
#     f = open(open_path, 'w', encoding='UTF-8') # CHANGED
#     f.write(page)
#     f.close()

#     # Convert to HTML
#     dst_folder_path = os.path.join(DST_FOLDER, assignment_name)

#     if not os.path.exists(dst_folder_path):
#         os.mkdir(dst_folder_path) # make folder

#     # If an assignment title wasn't defined in params, try and create it using the file name
#     # For discussions at least, we will specify it and process_page will return it
#     if not title:
#         title = format_assignment_name(assignment_name)
#     src_path = os.path.join(DST_FOLDER, f'{assignment_name}.md')
#     dst_path = os.path.join(DST_FOLDER, assignment_name, 'index.html')
#     css_path = os.path.join('..', 'assets', 'theme.css')
#     os.system(f'pandoc -s --standalone --katex --from markdown-markdown_in_html_blocks+raw_html -c {css_path} --metadata title="{title}" {src_path} -o {dst_path}')

#     # Delete the intermediate Markdown
#     os.remove(src_path)

#     # Copy over the images for just that page, but only if called individually
#     # If called in bulk, this shouldn't be run, since this is handled by
#     # write_all_pages
#     if not called_from_write_all_pages:
#         src_path = os.path.join('assets', 'images', assignment_name)
#         dst_path = os.path.join(DST_FOLDER, src_path)
#         if os.path.exists(src_path):
#             if os.path.exists(dst_path):
#                 shutil.rmtree(dst_path)
#             shutil.copytree(src_path, dst_path)

# def update_page(path):
#     '''Doesn't work for discussion files, yet.'''
#     sep = '/' if '/' in path else '\\'
#     assignment_name = path.split(sep)[-1].replace('.yml', '')

#     # Generate the Markdown
#     page = process_page(path)

#     # Write the Markdown
#     open_path = os.path.join(DST_FOLDER, f'{assignment_name}.md')
#     f = open(open_path, 'w')
#     f.write(page)
#     f.close()

#     dst_folder_path = os.path.join(DST_FOLDER, assignment_name)
#     # Make the function much faster by not requiring the folder to be recreated
#     if not os.path.exists(dst_folder_path):
#         os.mkdir(dst_folder_path) # make folder
    
#     title = format_assignment_name(assignment_name)
#     src_path = os.path.join(DST_FOLDER, f'{assignment_name}.md')
#     # Use a temp HTML file to write over than the main one inorder to minimize delay on viewing the page
#     tmp_path = os.path.join(DST_FOLDER, assignment_name, 'temp.html')
#     dst_path = os.path.join(DST_FOLDER, assignment_name, 'index.html')
#     css_path = os.path.join('..', 'assets', 'theme.css')
#     os.system(f'pandoc -s --standalone --katex --from markdown-markdown_in_html_blocks+raw_html -c {css_path} --metadata title="{title}" {src_path} -o {tmp_path}')

#     # Delete the intermediate Markdown
#     os.remove(src_path)
#     if os.path.exists(dst_path):
#         os.remove(dst_path)
#     os.rename(tmp_path, dst_path)


# def write_all_pages(dir='pages'):
#     '''Assumes all pages are specified in YML'''

#     if os.path.exists(DST_FOLDER):
#         delete_folder(DST_FOLDER)
#     os.mkdir(DST_FOLDER)

#     # Add CNAME back – this is a massive hack, but whatever
#     cname_path = os.path.join(DST_FOLDER, 'CNAME')
#     cname = open(cname_path, 'w')
#     cname.write('practice.dsc10.com')
#     cname.close()

#     page_paths = os.path.join(dir, '*', '*.yml')
#     all_paths = glob.glob(page_paths)
#     for path in all_paths:
#         write_page(path, called_from_write_all_pages=True)

#     # Copy over images/scripts
#     # os.mkdir(f'{DST_FOLDER}/assets/')
#     # os.system(f'cp -R assets/ {DST_FOLDER}/assets/')
#     dst_path = os.path.join(DST_FOLDER, 'assets')
#     shutil.copytree('assets', dst_path)

# def create_index():
#     f_index = open('index.md', 'r')
#     index_src = f_index.read()
#     f_index.close()

#     out = read_html_config('include-head.html')
#     out += '\n' + index_src

#     src_path = os.path.join(DST_FOLDER, 'index.md')
#     f = open(src_path, 'w')
#     f.write(out)
#     f.close()

#     css_path = os.path.join('assets', 'theme.css')
#     src_path = os.path.join(DST_FOLDER, 'index.md')
#     dst_path = os.path.join(DST_FOLDER, 'index.html')
#     os.system(f'pandoc -c {css_path} -s {src_path} -o {dst_path}')
#     os.remove(src_path)

#     # Remove pre-defined title
#     src_path = os.path.join(DST_FOLDER, 'index.html')
#     f = open(src_path, 'r')
#     r = f.read()
#     f.close()

#     r = re.sub(r'<h1 class="title">.*?</h1>', '', r)
#     f = open(src_path, 'w')
#     f.write(r)
#     f.close()

# if __name__ == '__main__':
#     # No arguments: run all
#     if len(sys.argv) == 1:
#         write_all_pages()
#         create_index()

#     elif sys.argv[1] == 'index':
#         create_index()

#     elif sys.argv[1] == "listen":
#             # Obtain the file paths for all markdown files.
#             # We will be looking to see if the modification time changes to signal an update
#             page_paths = os.path.join('pages', '*', '*.yml')
#             all_paths = glob.glob(page_paths)
            
#             # This creates an array that contains an entry for each yml file containing all the yml and md paths related to it.
#             # These are all the files we would want to check for edits.
#             listen_files = []
#             for path in all_paths:
#                 r_file = open(path, 'r')
#                 r = r_file.read()
#                 r_file.close()
#                 params = yaml.safe_load(r)
#                 listen_files += [[path] + list(map(lambda x: os.path.join("problems",x + ".md"),params.get("problems",[])))]

#             # This uses the same format as the listen_files variable to store the timestamp info for each file.
#             # Timestamps are used to check for file changes to signal updates.
#             cached_stamp = []
#             for i,section in enumerate(listen_files):
#                 cached_stamp += [[]]
#                 for file in section:
#                     cached_stamp[i] += [os.stat(file).st_mtime]


#             # Beginning of listening loop.
#             # This is based on the second response to this post: https://stackoverflow.com/questions/182197/how-do-i-watch-a-file-for-changes            
#             while True:
#                 try:
#                     # Every second
#                     time.sleep(1)
#                     # For each markdown file
#                     for i, section in enumerate(listen_files):
#                         for j, path in enumerate(section):
#                             # Get the last modified time stamp
#                             stamp = os.stat(path).st_mtime
#                             # Compare to currently cached timestamp
#                             # If its different then the file in questions has been modified and needs to be reflected on the html file
#                             if stamp != cached_stamp[i][j]:
#                                 # When a yml file is updated, we also need to update the files listened to reflect changes
#                                 # to the problem section
#                                 if ".yml" in path:
#                                     print(f"Updating tracked problems for {section[0]}")
#                                     r_file = open(path, 'r')
#                                     r = r_file.read()
#                                     r_file.close()
#                                     new_problems = yaml.safe_load(r).get("problems",[])
#                                     # Replace old listened files with new listened files to reflects changes to the .yml file
#                                     listen_files[i] = [path] + list(map(lambda x: os.path.join("problems",x + ".md"),new_problems))
#                                     cached_stamp[i] = [os.stat(file).st_mtime for file in listen_files[i]]
#                                 # Update cached timestamp to reflect the update
#                                 cached_stamp[i][j] = stamp
#                                 print(f"Updating: {section[0]}")
#                                 # Update the new HTML folder
#                                 update_page(section[0])
#                                 print("Finished Updating! Refresh the .html file on your browser to see changes!")
#                                 break
#                 except KeyboardInterrupt:
#                     break
#     else:
#         for page in sys.argv[1:]:
#             write_page(page)


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
from collections import defaultdict
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

        # parse front matter once and extract a visible lecture pill
        front, body = parse_frontmatter(r)

        lec = front.get("lecture")
        lec_txt = None
        if isinstance(lec, list) and lec:
            lec_txt = ", ".join(str(int(x)) for x in sorted({int(x) for x in lec}))
        elif isinstance(lec, int):
            lec_txt = str(lec)
        elif isinstance(lec, str) and lec.strip():
            parts = re.split(r"[,\s]+", lec.strip())
            nums = [int(p) for p in parts if p]
            if nums:
                lec_txt = ", ".join(str(x) for x in sorted(set(nums)))

        lecture_html = (
            f"<div class='meta'><span class='pill pill-lecture' title='Lecture number(s)'>Lecture {lec_txt}</span></div>\n"
            if lec_txt else ""
        )

        # Pass body (content without front matter) so it renders cleanly
        q_out = process_problem(problem_str=body, problem_num=i+1, show_solution=show_solution, lecture_html=lecture_html)
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


def process_problem_no_subparts(problem_str, problem_num, show_solution, heading='##', lecture_html=""):
    '''Used for problems with no subparts, and to process individual subparts'''
    
    if show_solution:
        # Extract solution    
        if '# BEGIN SOLUTION' in problem_str:
            sep = 'SOLUTION'
        elif '# BEGIN SOLN' in problem_str:
            sep = 'SOLN'
        else:
            raise AssertionError('Neither # BEGIN SOLUTION nor # BEGIN SOLN were found')
            
        pattern = r"([\d\D]*?)"
        exp = f"# BEGIN {sep}{pattern}# END {sep}"

            
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
            raw_pattern = r"([\d\D]*?)"
            exp = f"# BEGIN {sep}{raw_pattern}# END {sep}"
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
{lecture_html}

{problem_only}

{solution_processed}

    '''
    
    return out

SUBPART_REGEXP = r'# BEGIN SUBPROB([\d\D]*?)# END SUBPROB'

def process_problem_with_subparts(problem_str, problem_num, show_solution, lecture_html=""):
    problem_str = problem_str.replace('# BEGIN PROB', '').replace('# END PROB', '') \
                             .replace('# BEGIN PROBLEM', '').replace('# END PROBLEM', '')

    # Add the lecture pill once at the top of the problem
    problem_str = f'## Problem {problem_num}\n{lecture_html}{problem_str}'
    i = 0
    while len(re.findall(SUBPART_REGEXP, problem_str)) > 0:
        top_match = re.findall(SUBPART_REGEXP, problem_str)[0]

        top_match_processed = process_problem_no_subparts(top_match, 
                                                          str(problem_num) + f'.{i+1}',
                                                          show_solution,
                                                          heading='###',
                                                          lecture_html="")  # no pill per subpart

        top_match_processed = '<br>\n' + top_match_processed.replace(r'\ '[0], r'\\ '[:-1]) + '\n<br>'
        problem_str = re.sub(SUBPART_REGEXP, top_match_processed, problem_str, count=1)
        i += 1

    problem_str = problem_str.replace('<br>\n\n<br>', '<br>')
    return problem_str

# ===== Lecture-page helpers (Step 2) =====

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*(.*)\Z", re.DOTALL)

def _parse_frontmatter(text: str):
    """Return (frontmatter_dict, body_without_frontmatter)."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    fm_raw, body = m.group(1), m.group(2)
    try:
        data = yaml.safe_load(fm_raw) or {}
        if not isinstance(data, dict):
            data = {}
    except Exception:
        data = {}
    return data, body

def _normalize_lecture_tag(value):
    """Normalize 'lecture' tag into a list of ints."""
    if value is None:
        return []
    if isinstance(value, int):
        return [value]
    if isinstance(value, list):
        out = []
        for v in value:
            try:
                out.append(int(v))
            except Exception:
                pass
        return sorted(set(out))
    # strings like "14, 18" or "[14, 18]"
    s = str(value).strip()
    if not s:
        return []
    if s.startswith('[') and s.endswith(']'):
        try:
            arr = yaml.safe_load(s)
            return _normalize_lecture_tag(arr)
        except Exception:
            pass
    parts = re.split(r"[,\s]+", s)
    out = []
    for p in parts:
        if p:
            try:
                out.append(int(p))
            except Exception:
                pass
    return sorted(set(out))

def _slug_and_qnum_from_path(md_path: str):
    """
    problems/<slug>/qNN*.md -> (slug, NN)
    """
    parts = md_path.replace("\\", "/").split("/")
    if len(parts) < 3:
        return None, None
    slug = parts[1]  # 'sp24-final' etc.
    fname = parts[-1]
    m = re.match(r"q0*([0-9]+)\.md\Z", fname)
    return slug, (int(m.group(1)) if m else None)

def collect_problems_by_lecture():
    """
    Scan problems/, group by lecture number.
    Returns: dict[int, list[dict]] with keys like 1..25 and items:
      {'path', 'slug', 'q', 'body'}
    """
    out = defaultdict(list)
    for md in glob.glob(os.path.join('problems', '*', 'q*.md')):
        with open(md, 'r', encoding='UTF-8') as f:
            raw = f.read()
        fm, body = _parse_frontmatter(raw)
        lecs = _normalize_lecture_tag(fm.get('lecture'))
        if not lecs:
            continue
        slug, q = _slug_and_qnum_from_path(md)
        for L in lecs:
            out[L].append({'path': md, 'slug': slug, 'q': q, 'body': body})
    # sort each list nicely
    for L in out:
        out[L].sort(key=lambda d: (d['slug'] or '', d['q'] or 0))
    return out

# --- Fix asset paths for lecture pages (depth: docs/lectures/lecN/) ---
_ASSET_ROOTS = ("assets/", "pdfs/", "static/")

def _normalize_from_lecture(url: str) -> str:
    """Make asset/link URLs correct from docs/lectures/lecN/index.html."""
    # ignore absolute, anchors, data URIs
    if "://" in url or url.startswith(("data:", "#")):
        return url

    for root in _ASSET_ROOTS:
        # already correct for lecN page depth
        if url.startswith(f"../../{root}"):
            return url
        # common cases we need to bump up one level
        if url.startswith(f"../{root}"):
            return f"../{url}"                # -> ../../root...
        if url.startswith(f"./{root}"):
            return f"../../{url[2:]}"         # ./assets/... -> ../../assets/...
        if url.startswith(root):
            return f"../../{url}"             # assets/... -> ../../assets/...
    return url

def rewrite_paths_for_lecture(md_or_html: str) -> str:
    """
    Rewrites:
      - Markdown:  ![](assets/...) / [pdf](pdfs/...) etc.
      - HTML:      <img src="...">, <a href="...">, <source src>, <link href>
    so they resolve from docs/lectures/lecN/index.html.
    """
    s = md_or_html

    # Markdown images/links
    md_img  = re.compile(r'(!\[[^\]]*\]\()([^)\s]+)')
    md_link = re.compile(r'(\[[^\]]*\]\()([^)\s]+)')
    s = md_img.sub (lambda m: m.group(1) + _normalize_from_lecture(m.group(2)) + ")", s)
    s = md_link.sub(lambda m: m.group(1) + _normalize_from_lecture(m.group(2)) + ")", s)

    # HTML attributes
    html_attr = re.compile(r'(\b(?:src|href)=["\'])([^"\']+)(["\'])', re.I)
    s = html_attr.sub(lambda m: m.group(1) + _normalize_from_lecture(m.group(2)) + m.group(3), s)

    return s



def write_lecture_pages():
    """
    Create docs/lectures/lec{N}/index.html for each lecture N.
    - Matches the exam pages layout (no extra wrapper).
    - Root link works from nested path.
    - Assets/images/pdf links rewritten to ../../...
    - Strip Pandoc's H1 .title for visual consistency.
    """
    problems_by_lec = collect_problems_by_lecture()
    if not problems_by_lec:
        return []

    base = os.path.join(DST_FOLDER, 'lectures')
    os.makedirs(base, exist_ok=True)

    written = []
    for L in sorted(problems_by_lec.keys()):
        items = problems_by_lec[L]

        # Use the same include-head the exams use,
        # but fix the CSS path depth for /docs/lectures/lecN/
        head_html = read_html_config('include-head.html').replace(
            'href="assets/theme.css"', 'href="../../assets/theme.css"'
        )

        page_md  = head_html
        page_md += """
[&#8592; return to practice.dsc10.com](../../index.html)

---

"""
        page_md += f"# Lecture {L} — Collected Practice Questions\n\n"
        page_md += (
            f"Below are practice problems tagged for Lecture **{L}** "
            f"(rendered directly from the original exam/quiz sources).\n\n---\n\n"
        )

        # Append problems (rewrite asset paths so images/pdfs work from /lectures/lecN/)
        for i, item in enumerate(items, start=1):
            body_fixed = rewrite_paths_for_lecture(item['body'])
            q_html = process_problem(problem_str=body_fixed, problem_num=i, show_solution=True)

            src_line = ""
            if item['slug'] and item['q'] is not None:
                src_line = f'<p class="meta"><em>Source:</em> {item["slug"]} — Q{item["q"]}</p>\n'

            page_md += src_line + q_html + "\n\n---\n\n"

        # Write temp MD -> HTML (mirror exams: keep pandoc simple and strip auto title)
        lec_dir = os.path.join(base, f'lec{L}')
        os.makedirs(lec_dir, exist_ok=True)
        md_tmp = os.path.join(DST_FOLDER, f'lec{L}.md')
        with open(md_tmp, 'w', encoding='UTF-8') as f:
            f.write(page_md)

        dst_html = os.path.join(lec_dir, 'index.html')
        css_path = os.path.join('..','..','assets','theme.css')
        os.system(
            f'pandoc -s --standalone --katex '
            f'--from markdown-markdown_in_html_blocks+raw_html '
            f'-c {css_path} '
            f'--metadata title="Lecture {L} — Practice" '
            f'{md_tmp} -o {dst_html}'
        )
        os.remove(md_tmp)

    with open(dst_html, 'r', encoding='utf-8') as f:
        html = f.read()

    # strip Pandoc title (existing line)
    html = re.sub(r'<h1 class="title">.*?</h1>', '', html, flags=re.S)

    # NEW: normalize any remaining relative asset links in the final HTML
    html = rewrite_paths_for_lecture(html)

    with open(dst_html, 'w', encoding='utf-8') as f:
        f.write(html)


        written.append(L)

    return written

def build_lecture_links_block(lec_numbers):
    """Return a centered, no-scroll grid of lecture links with tidy spacing."""
    if not lec_numbers:
        return ""

    html = []
    # NOTE: no leading '---' (which pandoc turns into an <hr />)
    html.append("\n### 🔎 Find Problems by Lecture\n")
    html.append("<p>Jump to a page that collects all questions tagged for a given lecture.</p>\n")

    # A single centered grid: no flex shrink, fills up to 1100px, wraps nicely.
    html.append(
        '<div style="max-width:1100px;width:100%;margin:0 auto 24px;'
        'display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));'
        'gap:14px;">'
    )
    for L in sorted(lec_numbers):
        html.append(
            f'<a class="btn btn-light" '
            f'style="display:block;width:100%;text-align:center;white-space:nowrap;padding:.55rem .8rem;" '
            f'href="lectures/lec{L}/index.html">Lecture {L}</a>'
        )
    html.append('</div>\n')

    return "".join(html)

# renders stars
AVG_REGEXP = r'<average>(\d+)<\/average>'
def stars_repl(matchobj, exam=False):
    avg_int = int(re.findall(AVG_REGEXP, matchobj[0])[0])
    stars = get_stars_from_average(avg_int)
    kind = 'exam' if exam else 'problem'
    return f'<hr><h5>Difficulty: {stars}</h5><p>The average score on this {kind} was {avg_int}%.'

# --- Front matter helpers (YAML at top of problem files) ---
FM_RE = re.compile(r'^---\s*\n(.*?)\n---\s*(.*)\Z', re.S)

def parse_frontmatter(s: str):
    """
    Returns (front: dict, body: str). If no front matter, returns ({}, s).
    """
    m = FM_RE.match(s)
    if not m:
        return {}, s
    data = yaml.safe_load(m.group(1)) or {}
    if not isinstance(data, dict):
        data = {}
    return data, m.group(2)

def process_problem(problem_str, problem_num, show_solution, lecture_html=""):

    assert problem_str.count('# BEGIN PROB') == problem_str.count('# END PROB') == 1, 'Need exactly one # BEGIN PROB and # END PROB pair'
    
    problem_str = re.sub(AVG_REGEXP, stars_repl, problem_str)

    if '# BEGIN SUBPROB' in problem_str:
        assert problem_str.count('# BEGIN SUBPROB') == problem_str.count('# END SUBPROB'), f'Different number of # BEGIN SUBPROB and # END SUBPROB in Problem {problem_num}'
        return process_problem_with_subparts(problem_str, problem_num, show_solution, lecture_html)
    
    else:
        return process_problem_no_subparts(problem_str, problem_num, show_solution, lecture_html=lecture_html)

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
    if not os.path.exists(dst_folder_path):
        os.mkdir(dst_folder_path) # make folder
    
    title = format_assignment_name(assignment_name)
    src_path = os.path.join(DST_FOLDER, f'{assignment_name}.md')
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

    # Copy over assets (scripts, css, images)
    dst_path = os.path.join(DST_FOLDER, 'assets')
    shutil.copytree('assets', dst_path)

    # Build lecture pages based on 'lecture' tags
    write_lecture_pages()


def create_index():
    # Read the authored homepage markdown
    with open('index.md', 'r', encoding='utf-8') as f_index:
        index_src = f_index.read()

    # Build <head> (bootstrap, theme, etc.)
    out = read_html_config('include-head.html')

    # Build the lecture links HTML
    lec_map = collect_problems_by_lecture()
    lec_numbers = sorted(lec_map.keys())
    lecture_block = build_lecture_links_block(lec_numbers)

    # Insert the lecture block *before* the feedback section if present.
    # This matches the "move feedback below the lecture grid" requirement.
    feedback_re = re.compile(
        r'(?s)\n+---\s*\n\s*####\s*.*?Let us know here.*?\n\s*---\s*\n'
    )
    m = feedback_re.search(index_src)
    if m:
        index_src_reordered = index_src[:m.start()] + lecture_block + index_src[m.start():]
    else:
        # Fallback: append at end if feedback block isn't found
        index_src_reordered = index_src + lecture_block

    out += '\n' + index_src_reordered

    # Write intermediate MD then render to HTML (unchanged)
    src_path = os.path.join(DST_FOLDER, 'index.md')
    with open(src_path, 'w', encoding='utf-8') as f:
        f.write(out)

    css_path = os.path.join('assets', 'theme.css')
    dst_path = os.path.join(DST_FOLDER, 'index.html')
    os.system(f'pandoc -c {css_path} -s {src_path} -o {dst_path}')
    os.remove(src_path)

    # Strip Pandoc's auto H1 title (unchanged)
    with open(dst_path, 'r', encoding='utf-8') as f:
        html = f.read()
    html = re.sub(r'<h1 class="title">.*?</h1>', '', html, flags=re.S)
    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(html)



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
                            if stamp != cached_stamp[i][j]:
                                # When a yml file is updated, update tracked problems
                                if ".yml" in path:
                                    print(f"Updating tracked problems for {section[0]}")
                                    r_file = open(path, 'r')
                                    r = r_file.read()
                                    r_file.close()
                                    new_problems = yaml.safe_load(r).get("problems",[])
                                    listen_files[i] = [path] + list(map(lambda x: os.path.join("problems",x + ".md"),new_problems))
                                    cached_stamp[i] = [os.stat(file).st_mtime for file in listen_files[i]]
                                # Update cached timestamp
                                cached_stamp[i][j] = stamp
                                print(f"Updating: {section[0]}")
                                # Update the HTML
                                update_page(section[0])
                                print("Finished Updating! Refresh the .html file on your browser to see changes!")
                                break
                except KeyboardInterrupt:
                    break
    else:
        for page in sys.argv[1:]:
            write_page(page)
