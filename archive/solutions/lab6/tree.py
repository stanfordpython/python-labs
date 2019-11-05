import pathlib

NORMAL_CONTINUATION = '├── '
FINAL_CONTINUATION = '└── '

VERTICAL = '│   '
SPACER = '    '

def tree(directory):
    print(directory.name)
    tree_helper(directory, indent='')

def tree_helper(file, indent):
    if not file.is_dir():
        return
    children = list(file.iterdir())
    if children:
        for subfile in children[:-1]:
            print(indent, NORMAL_CONTINUATION, subfile.name, sep='')
            tree_helper(subfile, indent + VERTICAL)
        print(indent, FINAL_CONTINUATION, children[-1].name, sep='')
        tree_helper(children[-1], indent + SPACER)

def help():
    return """Usage: python3 tree.py <directory>

    Pretty-print a directory hierarchy."""

if __name__ == '__main__':
    # Note: In a production system, you'd probably use argparse.
    import sys
    arguments = sys.argv[1:]
    if len(arguments) >= 2:
        print(help())
        sys.exit(1)

    directory = pathlib.Path.cwd()  # Default
    if arguments:
        directory = pathlib.Path(arguments[0])

    if not directory.is_dir():
        print('Invalid directory: {}'.format(directory))

    tree(directory)

