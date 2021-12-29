from ast import literal_eval
from common.input import get_input_path_str
from common.output import print_output
from itertools import permutations
from day18.part01 import magnitude, plus


def main():
    result = max([magnitude(plus(*pair)) for pair in read_input()])
    print_output(__file__, result)


def read_input():
    '''Generate all possible ordered pairs from input file lines.'''
    nums = None
    with open(get_input_path_str(__file__), 'r') as f:
        nums = [literal_eval(line.strip()) for line in f]

    for pair in permutations(nums, 2):
        yield pair


if __name__ == '__main__':
    main()
