from collections import defaultdict
from common.input import get_input_path_str
from common.output import print_output

def main():
    conns = defaultdict(set)

    for n1, n2 in read_input():
        conns[n1].add(n2)
        conns[n2].add(n1)

    paths = []
    traverse(conns, 'start', paths, [], set())

    result = len(paths)

    print_output(__file__, result)


def traverse(conns, curr, paths, path, spent):
    if curr == 'end':
        paths.append(path + [curr])
        return

    nodes = conns[curr]

    if len(nodes) == 0:
        return

    next_spent = spent | set()
    if curr.islower():
        next_spent = spent | set((curr,))

    for n in nodes - spent:
        traverse(conns, n, paths, path + [curr], next_spent)


def read_input():
    with open(get_input_path_str(__file__), 'r') as f:
        for line in f:
            yield line.strip().split('-')


if __name__ == '__main__':
    main()
