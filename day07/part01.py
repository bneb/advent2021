from common.input import get_input_path_str
from common.output import print_output
from statistics import median

def main():
    '''Compute the exponential growth given an initial condition.'''
    data = read_input()
    med = median(data)
    result = sum([abs(x-med) for x in data])

    print_output(__file__, result)


def read_input():
    with open(get_input_path_str(__file__), 'r') as f:
        return [int(x) for x in f.readline().strip().split(',')]


if __name__ == '__main__':
    main()
