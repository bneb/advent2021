from common.input import get_input_path_str
from common.output import print_output

def main():
    dots, folds = read_input()
    for fold in folds:
        dots = foldit(dots, fold)

    print_grid(dots)


def foldit(dots, fold):
    new_dots = set()
    axis, value = fold

    for dot in dots:
        x, y = dot
        if axis == 'x':
            if x > value:
                x = 2*value - x
        else:
            if y > value:
                y = 2*value - y

        new_dots.add((x, y))

    return new_dots


def print_grid(grid):
    minx = min([x for x, _ in grid])
    maxx = max([x for x, _ in grid])+1
    miny = min([y for _, y in grid])
    maxy = max([y for _, y in grid])+1

    for y in range(0, maxy):
        print(''.join(['#' if (x, y) in grid else '.' for x in range(0, maxx)]))


def read_input():
    with open(get_input_path_str(__file__), 'r') as f:
        lines = f.read().strip().split('\n')
        boundary = lines.index('')

        dots = set()
        for d in lines[:boundary]:
            x, y = d.split(',')
            dots.add((int(x), int(y)))

        folds = []
        for i in lines[boundary+1:]:
            text, val = i.split('=')
            y = text[-1]
            folds.append((y, int(val)))

    return (dots, folds)


if __name__ == '__main__':
    main()
