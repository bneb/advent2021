from ast import literal_eval
from common.input import get_input_path_str
from common.output import print_output


def main():
    num = read_input()
    result = magnitude(num)
    print_output(__file__, result)


def magnitude(num):
    '''Custom way to score any node in the tree.'''
    if isinstance(num, int):
        return num

    left, right = num
    return 3*magnitude(left) + 2*magnitude(right)


def explode(num, level=0):
    '''Returns a tuple of node, add_left, add_right, was_reduced.
    This logic is confusing. Only explode one side at a time.
    '''
    if isinstance(num, int):
        return num, 0, 0, False

    left, right = num

    if level >= 4 and isinstance(left, int) and isinstance(right, int):
        return 0, left, right, True

    left, left_add, right_add, reduced = explode(left, level+1)
    if reduced:
        right = add_left(right, right_add)
        right_add = 0
    else:
        right, left_add, right_add, reduced = explode(right, level+1)
        if reduced:
            left = add_right(left, left_add)
            left_add = 0
    return (left, right), left_add, right_add, reduced


def add_left(num, val):
    '''Add add to the left most node of num.'''
    if isinstance(num, int):
        return num+val

    return add_left(num[0], val), num[1]


def add_right(num, val):
    '''Add add to the right most node of num.'''
    if isinstance(num, int):
        return num+val

    return num[0], add_right(num[1], val)


def split(num):
    '''Returns ((left, right), was_reduced).'''
    if isinstance(num, int):
        return (num, False) if num < 10 else ((num//2, num-num//2), True)

    left, right = num
    left, reduced = split(left)
    right, reduced = (right, True) if reduced else split(right)

    return (left, right), reduced


def reduce(num):
    '''Iteratively explode or split until no further reduction is possible.'''
    was_reduced = True
    while was_reduced:
        num, _, _, was_reduced = explode(num)
        num, was_reduced = (num, True) if was_reduced else split(num)

    return num


def plus(num, right):
    '''Returns the reduced tuple of (num, right).'''
    return reduce((num, right))


def read_input():
    '''Iteratively read and combine each line of the file into the number.'''
    with open(get_input_path_str(__file__), 'r') as f:
        num = literal_eval(f.readline().strip())
        num = reduce(num)

        for line in f:
            num = (num, literal_eval(line.strip()))
            num = reduce(num)

        return num


if __name__ == '__main__':
    main()
