from common.input import get_input_path_str
from common.output import print_output
from math import sqrt, ceil, floor
from re import findall


def main():
    minx, maxx, miny, maxy = read_input()
    data = check_all_trajectories(minx, maxx, miny, maxy)
    result = max(data)
    print_output(__file__, result)


def check_all_trajectories(minx, maxx, miny, maxy):
    '''Collect data for all plausible trajectories.'''
    data = []

    # limit the search space
    min_vx = get_min_vx(minx)
    max_vx = get_max_vx(maxx)
    min_vy = get_min_vy(miny)
    max_vy = get_max_vy(miny, maxy)

    for vx in range(min_vx, max_vx):
        for vy in range(min_vy, max_vy):
            outcome = check_trajectory(vx, vy, minx, maxx, miny, maxy)
            if outcome is not None:
                data.append(outcome)

    return data


def check_trajectory(vx, vy, minx, maxx, miny, maxy):
    '''If the target is hit, returns the highest point, else None.'''
    x = 0
    y = 0
    highest = 0

    while y >= miny and x <= maxx:
        highest = max(y, highest)

        if miny <= y <= maxy and minx <= x <= maxx:
            return highest

        x += vx
        if vx > 0: vx -= 1
        if vx < 0: vx += 1

        y += vy
        vy -= 1

    return None


def get_min_vx(minx):
    # leverage Gauss summation, solve using modified quadratic formula
    min_vx = int(ceil((-1 + sqrt(1+8*minx))/2))
    return min_vx


def get_max_vx(maxx):
    # We can't exceed the max x value of the target in the first bound
    return maxx+1


def get_min_vy(miny):
    # the vy should at minimum be able to hit the bottom of the range.
    return miny


def get_max_vy(miny, maxy):
    # the velocity should not be so great that it can miss the range.
    # this only works because it is known that miny < maxy < 0
    return 1-miny


def read_input():
    '''Read the one line of input. Convert from hex to binary and pad 0's.'''
    with open(get_input_path_str(__file__), 'r') as f:
        # search for positive and negative strings of digits, cast to int
        return map(int, findall('-?\d+', f.read().strip()))


if __name__ == '__main__':
    main()
