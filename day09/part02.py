from common.input import get_input_path_str
from common.output import print_output

def main():
    '''Given a grid, count cells lower than NSEW neighbors.'''
    basins = []
    grid = read_input()

    for (i, j), val in grid.items():
        n = grid.get((i-1, j), 10)
        s = grid.get((i+1, j), 10)
        e = grid.get((i, j+1), 10)
        w = grid.get((i, j-1), 10)

        # Start searching in a new basin if at a local minima.
        if val < min(n, s, e, w):
            basin = {(i, j)}
            search(grid, basin, i, j, val)
            basins.append(basin)

    a, b, c = sorted([len(b) for b in basins])[-3:]
    result = a*b*c

    print_output(__file__, result)


def search(grid, basin, r, c, val):
    '''Recursively search NSEW neighbors and add into basin.'''
    for coords in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
        new_val = grid.get(coords, 10)

        if val < new_val < 9:
            basin.add(coords)
            search(grid, basin, *coords, new_val)


def read_input():
    with open(get_input_path_str(__file__), 'r') as f:
        grid = dict()
        for row_num, row in enumerate(f.read().split('\n')):
            for col_num, val in enumerate(row):
                grid[(row_num, col_num)] = int(val)

        return grid


if __name__ == '__main__':
    main()
