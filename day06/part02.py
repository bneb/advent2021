from common.input import get_input_path_str
from common.output import print_output
from collections import Counter
from day06.part01 import read_input

def main():
    '''Compute the exponential growth given an initial condition.'''
    data = Counter(read_input())
    result = simulate(256, data)
    print_output(__file__, result)


def simulate(n, data):
    '''Simulate n periods.'''
    for _ in range(n):
        new_data = Counter()
        for timer, n_fish in data.items():
            if timer == 0:
                new_data[6] += n_fish
                new_data[8] += n_fish
            else:
                new_data[timer-1] += n_fish

        data = new_data

    return sum(new_data.values())


if __name__ == '__main__':
    main()
