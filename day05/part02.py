from common.output import print_output
from day05.part01 import make_grid

def main():
    '''Given line segments, count the grid points where line segments cross at least twice.'''
    grid = make_grid(filter_coords)

    result = sum([1 for v in grid.values() if v >= 2])

    print_output(__file__, result)


def filter_coords(x1, y1, x2, y2):
    return x1 != x2 and y1 != y2 and abs(x1-x2) != abs(y1-y2)


if __name__ == '__main__':
    main()
