from common.input import get_input_path_str
from common.output import print_output

def main():
    dots, folds = read_input()
    dots = foldit(dots, folds[0])
    result = len(dots)

    print_output(__file__, result)

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
