
import os
import re
import argparse

from typing import NamedTuple, Tuple, Mapping


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

    def follow(self) -> str:
        """ Follows the link, returning a path for the new destination """
        return '%s/' % abs_path(os.path.join(self.src.path, self.path))
    
    def format(self) -> str:
        """ Formats the link in a standardized format """
        link = '[%s](' % self.name
        if self.path == './/':
            link += '#%s)' % self.section
        elif self.section == '':
            link += '%s)' % self.path[2:]
        else:
            link += '%s#%s)' % (self.path[2:], self.section)
        return link


def main():
    parser = argparse.ArgumentParser('Tools for manipulating links in markdown')
    subparser = parser.add_subparsers(dest='command')

    _ = subparser.add_parser('validate', help='Validates all existing links, reporting broken ones')
    _ = subparser.add_parser('sanitize', help='Sanitizes and reformats all existing links')
    parser_mv = subparser.add_parser('mv', help='Moves a file, renaming all existing links to that file')

    parser_mv.add_argument('old', type=str)
    parser_mv.add_argument('new', type=str)
    
    args = parser.parse_args()

    if args.command == 'validate':
        do_validate()
    elif args.command == 'sanitize':
        do_sanitize()
    elif args.command == 'mv':
        print('linky.py mv is not functional yet!')
        do_mv(args.old, args.new)


def do_validate():
    tree = build_tree()
    index = {p.path for p in tree}

    for path in tree:
        header = False
        for link in build_links(path):
            target = link.follow()
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
            clean = link.format()
            if link.raw != clean:
                if not header:
                    header = True
                    print('Found incorrectly formatted links in %s' % path.file)
                print('  L%-5d: \'%s\' -> \'%s\'' % (link.line, link.raw, clean))
                replacements[link.raw] = clean
        
        if replacements:
            replace_all_in(path.file, replacements)


def do_mv(old: str, new: str):
    tree = build_tree()
    index = {p.path : p for p in tree}

    if old not in tree:
        return print('No path: %s' % old)
    if new not in tree:
        return print('No path: %s' % new)
    
    old_path = index[old]
    new_path = index[new]

    # Update all links to the old path
    for path in tree:
        if path != old_path:
            replacements = {}
            for link in path:
                if link.follow() == old_path.path:  # Link that links to the old file
                    pass  # Need to update the old link to point at the new file


def replace_all_in(file: str, replacements: Mapping[str, str]):
    """ Applies all replacements to the content of a given file """
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    for key, val in replacements.items():
        text = text.replace(key, val)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(text)


def build_links(path: Path) -> Tuple[Link, ...]:
    """ Builds the set of all Links for a given web Path """
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
    """ Builds the set of all Path objects in the web view """
    tree = []
    for path in walk('.'):
        if all(not path.startswith(exc) for exc in EXCLUDED) and path.endswith('.md'):
            path = abs_path(path)
            tree.append(Path(path, sanitize_path(path)))
    return tuple(tree)

def walk(path: str):
    """ Walks a directory, yielding each path found """
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
    """ Returns the absolute path relative to the root of the web directory """
    return os.path.relpath(os.path.abspath(path), ROOT)


if __name__ == '__main__':
    main()
