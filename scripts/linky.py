
import os
import re
import argparse

from typing import NamedTuple, Tuple, List


EXCLUDED = ['./_data', './_site', '.vscode', 'scripts', './README.md', './index.md']
ROOT = os.getcwd()

BEGIN_SORT_ALPHABETICAL = '<!--linky_begin_sort_alphabetical-->'
END_SORT_ALPHABETICAL = '<!--linky_end_sort_alphabetical-->'


class Path(NamedTuple):
    file: str
    path: str
    lines: Tuple[str]
    headers: List['Header']
    links: List['Link']

    def has_header(self, path: str) -> bool:
        return any(h.path == path for h in self.headers)
    
    def save(self):
        with open(self.file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(self.lines))

class Header(NamedTuple):
    src: Path
    line: int
    raw: str
    path: str

class Link(NamedTuple):
    """ A [name](path#section) link embedded in a markdown file. """
    src: Path
    line: int
    raw: str
    name: str
    path: str
    section: str

    def follow(self) -> str:
        """ Follows the link, returning a path for the new destination """
        return '%s' % abs_path(os.path.join(self.src.path, self.path))
    
    def format(self) -> str:
        """ Formats the link in a standardized format """
        path = os.path.normpath(self.path)
        link = '[%s](' % self.name
        if path == '.':
            link += '#%s)' % self.section
        elif self.has_section():
            link += '%s/#%s)' % (path, self.section)
        else:
            link += '%s/)' % path
        return link
    
    def has_section(self) -> bool:
        return self.section != ''


class BatchedPrint:
    def __init__(self, header: str):
        self.header = header
    
    def print(self, *args):
        if self.header is not None:
            print(self.header)
            self.header = None
        print(*args)


def main():
    parser = argparse.ArgumentParser('Tools for manipulating links in markdown')
    subparser = parser.add_subparsers(dest='command')

    _ = subparser.add_parser('validate', help='Validates all existing links, reporting broken ones')
    _ = subparser.add_parser('sanitize', help='Sanitizes and reformats all existing links')
    #parser_mv = subparser.add_parser('mv', help='Moves a file, renaming all existing links to that file')

    #parser_mv.add_argument('old', type=str)
    #parser_mv.add_argument('new', type=str)
    
    args = parser.parse_args()

    if args.command == 'validate':
        do_validate()
    elif args.command == 'sanitize':
        do_sanitize()


def do_validate():
    tree = build_tree()
    index = {p.path: p for p in tree}
    #print(index)

    for path in tree:
        batch = BatchedPrint('Found broken links in %s' % path.file)
        for link in path.links:
            target = link.follow()
            #print(path.path, link.raw, link.path, target)
            if target not in index:
                batch.print('  L%-5d: \'%s\' -> \'%s\'' % (link.line, link.raw, target))
            elif link.has_section():
                target_path = index[target]
                if not target_path.has_header(link.section):
                    target = '#' + link.section
                    batch.print('  L%-5d: \'%s\' -> \'%s\'' % (link.line, link.raw, target))


def do_sanitize():
    tree = build_tree()

    for path in tree:
        modified = False
        
        replacements = {}
        batch = BatchedPrint('Found incorrectly formatted links in %s' % path.file)
        for link in path.links:
            clean = link.format()
            if link.raw != clean:
                batch.print('  L%-3d: \'%s\' -> \'%s\'' % (link.line, link.raw, clean))
                replacements[link.raw] = clean
        
        if replacements:
            for i, line in enumerate(path.lines):
                for key, val in replacements.items():
                    if key in line:
                        path.lines[i] = line.replace(key, val)
                        modified = True
        
        # Alphabetical Sorting
        sort_ranges = []
        sort_range = None
        for i, line in enumerate(path.lines):
            if sort_range is not None:
                if line == END_SORT_ALPHABETICAL:
                    sort_ranges.append(sort_range)
                    sort_range = None
                elif line != '':  # Don't include empty lines in sort
                    sort_range.append((i, line))
            elif line == BEGIN_SORT_ALPHABETICAL:
                sort_range = []
        if sort_range is not None:
            print('ERROR: Finished iterating for sort ranges but did not find a end tag?')
            continue
        
        batch = BatchedPrint('Sorting ranges in %s' % path.file)
        for sort_range in sort_ranges:
            sorted_lines = sorted([line for _, line in sort_range])
            sorted_indexes = sorted([i for i, _ in sort_range])
            sorting_done = False
            for i, line in zip(sorted_indexes, sorted_lines):
                if path.lines[i] != line:
                    modified = True
                    sorting_done = True
                path.lines[i] = line
            if sorting_done:
                batch.print('  L%d-%d (%d lines)' % (sorted_indexes[0], sorted_indexes[-1], len(sorted_indexes)))
        
        if modified:  # Modified
            path.save()



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


def build_tree() -> Tuple[Path, ...]:
    """ Builds the set of all Path objects in the web view """
    tree = []
    for path in walk('.'):
        if all(not path.startswith(exc) for exc in EXCLUDED) and path.endswith('.md'):
            path = abs_path(path)

            with open(path, 'r', encoding='utf-8') as f:
                text = f.read()
            
            lines = text.split('\n')
            path_obj = Path(path, sanitize_path(path), lines, [], [])

            for i, line in enumerate(lines):
                for match in re.finditer(r'\[([^\(\)\[\]\n\r]+)\]\(([./A-Za-z0-9_-]*)\/?\#?([A-Za-z0-9_-]*)\)', line):
                    name, root, section = match.groups()
                    start, end = match.span()
                    path_obj.links.append(Link(path_obj, 1 + i, line[start:end], name, './%s/' % root, section))
                
                match = re.match(r'#+ (.+)', line)
                if match:
                    raw, *_ = match.groups()
                    link = re.sub(r'[^A-Za-z0-9]', '-', raw.lower())
                    path_obj.headers.append(Header(path_obj, line, raw, link))

            tree.append(path_obj)
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
    return os.path.normpath(path)

def abs_path(path: str) -> str:
    """ Returns the absolute path relative to the root of the web directory """
    return os.path.relpath(os.path.abspath(path), ROOT)


if __name__ == '__main__':
    main()
