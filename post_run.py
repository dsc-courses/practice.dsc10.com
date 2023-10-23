import os

import yaml
import pathlib

test = 'problems/sp23-midterm/q01.md'

def check_tags(filename):
    '''Check to see if the file has yaml description. If yes, return the tags of the problem.'''
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        if content.startswith('---'):
            return get_tags(filename)
    except Exception as e:
        print("No tags found")

def get_tags(filename):
    '''Return the tags in the yaml.'''
    with open(filename) as f:
        front_matter = next(yaml.load_all(f, Loader=yaml.FullLoader))
    tags = front_matter['tags']
    return tags

def get_all_paths():
    '''Get the paths of all problems in the problems folder'''
    root = pathlib.Path('problems')
    sub_dirs = list(root.glob("**/*"))
    files = [list(i.glob("**/*")) for i in sub_dirs]
    return files

# print(files)

def extract_problem_name(posixpath):
    '''Get path name of the problem. Example: 'problems/sp23-midterm/q01.md' --> sp23-midterm/q01'''
    path_str = str(posixpath)
    # prob_name = path_str.strip('problems/').strip('.md')
    prob_name = path_str.strip('.md').split('/', 1)[1]
    return prob_name

def sort_by_tag(files):
    '''Return dictionary where keys are the tag and values are the paths to problems with that tag.'''
    tag_dict = {}
    for i in files:
        for j in i:
            # print(j, check_tags(j))
            tags = check_tags(j) # this will return the tags, you will also need j...
            j = extract_problem_name(j)
            # tag should get its own folder in problems... the md files should get grouped by tag
            if (tags != None):
                for tag in tags:
                    if tag in tag_dict:
                        tag_dict[tag].append(j)
                    else:
                        tag_dict[tag] = [j]
    return tag_dict

def create_tags_folder():
    # folder_path = 'practice.dsc10.com/tags'
    parent_dir = os.getcwd()
    new_dir = 'pages/tags'
    # new_dir = 'tags'
    folder_path = os.path.join(parent_dir, new_dir)
    os.makedirs(folder_path)

def create_yaml(key, value):
    '''Create yaml page from dictionary of tags and paths.'''
    data = {}
    data['context'] = 'Collection of {} problems from DSC10 over the years.'.format(key)
    data['problems'] = value

    folder_path = 'pages/tags'
    output_file = key + '.yml'
    file_path = os.path.join(folder_path, output_file)
    with open(file_path, 'w', encoding='utf-8') as file:
        yaml.dump(data, file, default_flow_style=False)

def create_all_yaml(dict):
    '''Create different yaml pages for each tag.'''
    # folder_path = 'practice.dsc10.com/tags'
    # os.makedirs(folder_path)
    for key, value in dict.items():
        create_yaml(key, value)

if __name__ == '__main__':
    check_tags(test)
    files = get_all_paths()
    d = sort_by_tag(files)
    print(d)
    # for p in d['test1']:
    #     print(extract_problem_name(p))
    create_tags_folder()
    create_all_yaml(d)