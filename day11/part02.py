from common.input import get_input_path_str
from common.output import print_output
from day11.part01 import read_input, tic

def main():
    '''Given energy levels, count the number of flashes.'''
    grid = read_input()
    grid_size = len(grid)

    flashes = tic(grid)
    result = 1
    while flashes != grid_size:
        result += 1
        flashes = tic(grid)

    print_output(__file__, result)


if __name__ == '__main__':
    main()
