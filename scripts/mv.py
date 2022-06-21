
import os
import re
import argparse

EXCLUDED = ['./_data', './_site', '.vscode', 'scripts', './README.md']

def main():
    parser = argparse.ArgumentParser('Moves files while maintaining relative links')
    parser.add_argument('old', type=str)
    parser.add_argument('new', type=str)
    
    args = parser.parse_args()

    if not os.path.isfile(args.old):
        error('Input path does not exist: %s' % args.old)
    
    if os.path.isfile(args.new):
        error('Output path already exists: %s' % args.new)
    
    #os.makedirs(os.path.dirname(args.new), exist_ok=True)
    #os.rename(args.old, args.new)

    root = os.path.abspath(os.getcwd())
    old = os.path.relpath(os.path.abspath(args.old), root)
    new = os.path.relpath(os.path.abspath(args.new), root)

    old = old.replace('.md', '')
    new = new.replace('.md', '')

    print('Root', root)
    print('Moving %s -> %s' % (old, new))

    for file in walk('.'):
        if all(not file.startswith(exc) for exc in EXCLUDED) and file.endswith('.md'):
            
            src = link(file, old)
            dest = link(file, new)

            print('Migrate: %s -> %s in %s' % (src, dest, file))
            
            with open(file, 'r', encoding='utf-8') as f:
                text = f.read()
            
            for match in re.findall(r'\[([^\(\)\[\]\n\r]+)\]\((.\/)?(%s\/?)(#?[A-Za-z0-9 _]*)\)' % src):

            
            

def link(src: str, dest: str) -> str:
    if dest.endswith('index'):
        dest = dest[:-len('/index')]
    if src.endswith('index'):
        src = src[:-len('./index')]
    target = os.path.relpath(dest, src)
    return target


def walk(path: str):
    for sub in os.listdir(path):
        sub_path = os.path.join(path, sub)
        if os.path.isfile(sub_path):
            yield sub_path
        elif os.path.isdir(sub_path):
            yield from walk(sub_path)

def error(msg: str):
    print(msg)
    exit(-1)


if __name__ == '__main__':
    main()
