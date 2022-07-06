
import os
import re
import argparse

from typing import NamedTuple, Tuple


EXCLUDED = ['./_data', './_site', '.vscode', 'scripts', './README.md']
ROOT = os.getcwd()


class Path(NamedTuple):
    file: str
    path: str

class Link(NamedTuple):
    src: Path
    line: int
    raw: str
    name: str
    path: str
    section: str


def main():
    parser = argparse.ArgumentParser('Tools for manipulating links in markdown')
    subparser = parser.add_subparsers(dest='command')

    _ = subparser.add_parser('validate', help='Validates all existing links, reporting broken ones')
    _ = subparser.add_parser('sanitize', help='Sanitizes and reformats all existing links')
    parser_mv = subparser.add_parser('mv', help='Moves a file, renaming all existing links to that file')
    
    args = parser.parse_args()

    if args.command == 'validate':
        do_validate()
    elif args.command == 'sanitize':
        do_sanitize()



def do_validate():
    tree = build_tree()
    index = {p.path for p in tree}

    for path in tree:
        header = False
        for link in build_links(path):
            target = follow_link(link)
            if target not in index:
                if not header:
                    header = True
                    print('Found broken links in %s' % path.file)
                print('  L%-5d: \'%s\' -> \'%s\'' % (link.line, link.raw, target))


def do_sanitize():
    tree = build_tree()

    for path in tree:
        header = False
        replacements = {}
        for link in build_links(path):
            cleaned = '[%s](' % link.name
            if link.path == './/':
                cleaned += '#%s)' % link.section
            elif link.section == '':
                cleaned += '%s)' % link.path[2:]
            else:
                cleaned += '%s#%s)' % (link.path[2:], link.section)
            if link.raw != cleaned:
                if not header:
                    header = True
                    print('Found incorrectly formatted links in %s' % path.file)
                print('  L%-5d: \'%s\' -> \'%s\'' % (link.line, link.raw, cleaned))
                replacements[link.raw] = cleaned
        
        if replacements:
            # Fix links in file
            with open(path.file, 'r', encoding='utf-8') as f:
                text = f.read()
            
            for key, val in replacements.items():
                text = text.replace(key, val)
            
            with open(path.file, 'w', encoding='utf-8') as f:
                f.write(text)
        


def do_mv():
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
                pass
            
            

def link(src: str, dest: str) -> str:
    if dest.endswith('index'):
        dest = dest[:-len('/index')]
    if src.endswith('index'):
        src = src[:-len('./index')]
    target = os.path.relpath(dest, src)
    return target


def follow_link(link: Link) -> str:
    return '%s/' % abs_path(os.path.join(link.src.path, link.path))


def build_links(path: Path) -> Tuple[Link, ...]:
    with open(path.file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    links = []
    for i, line in enumerate(text.split('\n')):
        for match in re.finditer(r'\[([^\(\)\[\]\n\r]+)\]\(\.?\/?([A-Za-z0-9_-]*)\/?\#?([A-Za-z0-9_-]*)\)', line):
            name, root, section = match.groups()
            start, end = match.span()
            links.append(Link(path, 1 + i, line[start:end], name, './%s/' % root, section))
    return tuple(links)


def build_tree() -> Tuple[Path, ...]:
    tree = []
    for path in walk('.'):
        if all(not path.startswith(exc) for exc in EXCLUDED) and path.endswith('.md'):
            path = abs_path(path)
            tree.append(Path(path, sanitize_path(path)))
    return tuple(tree)

def walk(path: str):
    for sub in os.listdir(path):
        sub_path = os.path.join(path, sub)
        if os.path.isfile(sub_path):
            yield sub_path
        elif os.path.isdir(sub_path):
            yield from walk(sub_path)

def sanitize_path(path: str) -> str:
    if '\\' in path:
        path = path.replace('\\', '/')
    if '.md' in path:
        path = path.replace('.md', '')
    if path.endswith('index'):
        path = path[:-len('/index')]
    if not path.endswith('/'):
        path = path + '/'
    return path

def abs_path(path: str) -> str:
    return os.path.relpath(os.path.abspath(path), ROOT)

def error(msg: str):
    print(msg)
    exit(-1)


if __name__ == '__main__':
    main()
