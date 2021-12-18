from collections import Counter
from common.input import get_input_path_str
from common.output import print_output

def main():
    '''Given energy levels, count the number of flashes.'''
    grid = read_input()
    steps = 100
    result = 0

    for i in range(steps):
        flashes = tic(grid)
        result += flashes

    print_output(__file__, result)


def neighbors(grid, r, c):
    for rowD in range(-1, 2):
        for colD in range(-1, 2):
            if rowD == 0 and colD == 0:
                continue

            coords = (r+rowD, c+colD)
            if coords in grid:
                yield coords

def print_grid(grid):
    temp_x = max([cord[0] for cord in grid.keys()])
    temp_y = max([cord[1] for cord in grid.keys()])
    res = [[0] * (temp_y + 1) for ele in range(temp_x + 1)]

    for (i, j), val in grid.items():
        res[i][j] = val

    for r in res:
        print(r)


def tic(grid):
    q = list(grid.keys())
    flashes = 0
    n = len(q)

    while q:
        i = q.pop(0)

        if n > 0 or grid[i] > 0:
            n -= 1
            grid[i] += 1

        if grid[i] > 9:
            flashes += 1
            grid[i] = 0
            ns = list(neighbors(grid, *i))
            q += ns
    return flashes


def read_input():
    with open(get_input_path_str(__file__), 'r') as f:
        grid = Counter()
        for row_num, row in enumerate(f.read().split('\n')):
            for col_num, val in enumerate(row):
                grid[(row_num, col_num)] = int(val)

        return grid


if __name__ == '__main__':
    main()
