from common.input import get_input_path_str
from common.output import print_output
from common.turgid import LOGGER

def main():
    '''Count the number of entries in input.txt greater than the previous entry.'''
    count = 0
    last = None

    with open(get_input_path_str(__file__), 'r') as f:
        for line in f:
            cur = int(line)

            if last and cur > last:
                count += 1

            last = cur

    print_output(__file__, count)


if __name__ == '__main__':
    main()
