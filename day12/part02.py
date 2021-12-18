from collections import defaultdict
from common.input import get_input_path_str
from common.output import print_output
from day12.part01 import read_input

def main():
    conns = defaultdict(set)

    for n1, n2 in read_input():
        conns[n1].add(n2)
        conns[n2].add(n1)

    paths = []
    traverse(conns, 'start', paths, [], set(), False)

    result = len(paths)

    print_output(__file__, result)


def traverse(conns, curr, paths, path, spent, twice):
    if curr == 'end':
        paths.append(path + [curr])
        return

    nodes = conns[curr] - set(('start',))

    if len(nodes) == 0:
        return

    next_spent = spent | set()
    if curr.islower():
        next_spent = spent | set((curr,))

    for n in nodes:
        nt = False
        if n in spent:
            if not twice:
                traverse(conns, n, paths, path + [curr], next_spent, True)
        else:
            traverse(conns, n, paths, path + [curr], next_spent, twice)


if __name__ == '__main__':
    main()
