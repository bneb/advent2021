from common.input import get_input_path_str
from common.output import print_output

def main():
    '''Given a grid, count cells lower than NSEW neighbors.'''
    result = 0
    grid = read_input()

    for (i, j), val in grid.items():
        n = grid.get((i-1, j), 10)
        s = grid.get((i+1, j), 10)
        e = grid.get((i, j+1), 10)
        w = grid.get((i, j-1), 10)

        if val < min(n, s, e, w):
            result += 1+val

    print_output(__file__, result)


def read_input():
    with open(get_input_path_str(__file__), 'r') as f:
        grid = dict()
        for row_num, row in enumerate(f.read().split('\n')):
            for col_num, val in enumerate(row):
                grid[(row_num, col_num)] = int(val)

        return grid


if __name__ == '__main__':
    main()
