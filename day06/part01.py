from common.input import get_input_path_str
from common.output import print_output

def main():
    '''Compute the exponential growth given an initial condition.'''
    data = read_input()
    data = simulate(80, data)
    result = len(data)

    print_output(__file__, result)


def simulate(n, data):
    '''Run n tics of the clock.'''
    for _ in range(n):
        data = tic(data)

    return data


def read_input():
    with open(get_input_path_str(__file__), 'r') as f:
        return [int(x) for x in f.readline().strip().split(',')]


def tic(old_data):
    new_data = []
    for d in old_data:
        if d == 0:
            new_data.append(6)
            new_data.append(8)
        else:
            new_data.append(d-1)

    return new_data


if __name__ == '__main__':
    main()
