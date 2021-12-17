from collections import Counter
from common.input import get_input_path_str
from common.output import print_output
from operator import methodcaller

NUM_SEG_MAP = {
        0: set('abcefg'),
        1: set('cf'),
        2: set('acdeg'),
        3: set('acdfg'),
        4: set('bcdf'),
        5: set('abdfg'),
        6: set('abdefg'),
        7: set('acf'),
        8: set('abcdefg'),
        9: set('abcdfg')
    }

SEG_COUNTS = Counter([len(v) for v in NUM_SEG_MAP.values()])
UNIQUE_SEG_COUNTS = {k for k, v in SEG_COUNTS.items() if v == 1}

def main():
    '''Really complicated. prompt here: https://adventofcode.com/2021/day/8'''
    result = 0
    for (signals, outputs) in read_input():
        result += sum([1 for s in outputs if len(s) in UNIQUE_SEG_COUNTS])

    print_output(__file__, result)


def read_input():
    with open(get_input_path_str(__file__), 'r') as f:
        for line in f:
            yield tuple(map(methodcaller('split'), line.split(' | ')))


if __name__ == '__main__':
    main()
