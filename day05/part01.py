from common.input import get_input_path_str
from common.output import print_output
from collections import Counter
from re import findall

def main():
    '''Given line segments, count the grid points where line segments cross at least twice.'''
    grid = make_grid(filter_coords)

    result = sum([1 for v in grid.values() if v >= 2])

    print_output(__file__, result)


def filter_coords(x1, y1, x2, y2):
    return x1 != x2 and y1 != y2


def make_grid(filter_coords):
    grid = Counter()

    with open(get_input_path_str(__file__), 'r') as f:
        for l in f:
            x1, y1, x2, y2 = [int(x) for x in findall('\d+', l)]
            populate_grid(x1, y1, x2, y2, grid, filter_coords)

    return grid


def populate_grid(x1, y1, x2, y2, grid, filter_coords):
    if filter_coords(x1, y1, x2, y2):
        return

    grid[(x1, y1)] += 1
    while x1 != x2 or y1 != y2:
        if x1 < x2:
            x1 += 1
        elif x1 > x2:
            x1 -= 1
        if y1 < y2:
            y1 += 1
        elif y1 > y2:
            y1 -= 1

        grid[(x1, y1)] += 1


if __name__ == '__main__':
    main()
