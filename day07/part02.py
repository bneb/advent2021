from common.input import get_input_path_str
from common.output import print_output
from collections import Counter
from day07.part01 import read_input

def main():
    '''Compute the exponential growth given an initial condition.'''
    data = read_input()
    result = None

    for x in range(min(data), max(data)+1):
        fuel = get_fuel_used(data, x, burn_func)

        if result is None or fuel < result:
            result = fuel

    print_output(__file__, result)


def burn_func(x, i):
    d = abs(x-i)
    return (d*(d+1))/2


def get_fuel_used(data, i, burn_func):
    return sum([burn_func(d, i) for d in data])


if __name__ == '__main__':
    main()
