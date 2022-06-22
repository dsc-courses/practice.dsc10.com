######## ignore: # ! /usr/bin/env python3

import yaml
import os
import glob
import re

DST_FOLDER = 'docs'

# Utility functions for creating discussion/exam pages

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
    path = f'questions/{name}.md'
    return path

def format_md_paths(names):
    paths = [format_md_path(name) for name in names]
    return paths

def read_html_config(path):
    r = open(path, 'r').read()
    return r + '\n\n'

def create_top_info(params):
    return f'''
### DSC 10 Practice

---

**Instructor(s):** {params['instructors']}

{params['context']}

---

'''

def reformat_solution(question_str, question_number):
    '''Correctly adds the HTML formatting for solutions.'''

    if '# BEGIN SOLUTION' not in question_str:
        print('Warning: No solution was found.')
        return question_str

    splitted = question_str.split('# BEGIN SOLUTION')
    question_text = splitted[0]
    solution_text = splitted[1].strip('# END SOLUTION\n')

    

    solution_formatted = f'''
<div class="accordion" id="accordionExample">
  <div class="accordion-item">
    <h2 class="accordion-header" id="heading{question_number}">
      <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapse{question_number}" aria-expanded="true" aria-controls="collapse{question_number}">
        Click to view the solution.
      </button>
    </h2>
    <div id="collapse{question_number}" class="accordion-collapse collapse collapse" aria-labelledby="heading{question_number}" data-bs-parent="#accordionExample">
      <div class="accordion-body">
        {solution_text}
      </div>
    </div>
  </div>
</div>
    '''

    return question_text + '\n\n' + solution_formatted


def stitch(files, heading_weight='##', toc=False):
    '''Stitches individual .md files into a longer .md string with questions'''
    paths = format_md_paths(files)
    out = '\n\n'

    if toc:
        # Format a table of contents here
        pass

    for i, path in enumerate(paths):
        q_out = f'{heading_weight} Question {i + 1}\n'

        r = open(path, 'r').read()
        q_out += reformat_solution(question_str=r, question_number=i+1)
        q_out += '\n\n\n---\n\n\n'

        out += q_out

    return out

def process_page(path):
    '''Takes in a path to a YML file and returns a MD file with everything.'''
    r = open(path, 'r').read()
    params = yaml.safe_load(r)
    
    out = read_html_config('include-head.html')
    out += create_top_info(params)
    out += stitch(params['questions'])
    
    # String containing a Markdown document, can be written to file then use pandoc on it
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
    os.system(f'cp assets/theme.css {DST_FOLDER}/assets/theme.css')

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

# if __name__ == '__main__':
#     while True:
#         f = open('build/fa21-final.md', 'w')
#         f.write(process_page('pages/exams/fa21-final.yml'))
#         f.close()
#         os.system('pandoc -s --standalone --from markdown-markdown_in_html_blocks+raw_html -c ../scripts/theme.css build/fa21-final.md -o build/fa21-final.html')
#         os.
#         time.sleep(3)
    

    # pandoc -s --toc -c pandoc.css -A footer.html MANUAL.txt -o example3.html