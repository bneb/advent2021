from common.input import get_input_path_str
from common.output import print_output
from common.turgid import LOGGER

def main():
    '''Count the number of entries in input.txt with rolling average greater than previous.'''
    count = 0
    last = None

    with open(get_input_path_str(__file__), 'r') as f:
        for values in rolling_values(3, f):
            cur = sum(values)

            if last and cur > last:
                count += 1

            last = cur

    print_output(__file__, count)


def rolling_values(n, input_file):
    cur = [int(next(input_file)) for _ in range(n)]
    yield cur
    i = 0

    for line in input_file:
        i %= n
        cur[i] = int(line)
        yield cur
        i += 1


if __name__ == '__main__':
    main()
