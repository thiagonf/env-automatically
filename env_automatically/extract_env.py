import argparse
import sys
import re
import glob, os
import errno
import argparse

def main():
    parser = argparse.ArgumentParser(description='Search settings.py file')
    parser.add_argument('name_file', nargs=1, help='Name of django project to export env')

    if len(sys.argv) > 2:
        print("Error, just pass 1 project path as an argument.")
        sys.exit(1) 
    try:
        args = parser.parse_args()
        extract(args.name_file[0])
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)


def find_path(project_name):
    if project_name is '.':
        path = glob.glob('settings.py')
    else:
        format_path = '{}/**/settings.py'
        path = glob.glob(format_path.format(project_name), recursive=True)
    if len(path) == 0:
        path = glob.glob(project_name)
    if len(path) == 0:
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), 
                                project_name)
    return path[0]

def extract(project_name):
    path = find_path(project_name)
    with open(path, 'r') as settings, open('.env', 'w+') as env_file:
        REGEX = r"(config\(')([a-zA-Z0-9-_]*)"
        text_settings = settings.read()
        matches = re.findall(REGEX, text_settings, re.MULTILINE)

        for env in matches:
            env_file.write(env[1] + "\n")
