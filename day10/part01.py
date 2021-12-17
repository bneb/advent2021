from common.input import get_input_path_str
from common.output import print_output

POINT_MAP = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

CLOSE_LOOKUP = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}

def main():
    '''Given open-close pairs, find and score syntax errors.'''
    result = sum([process_line(line) for line in read_input()])

    print_output(__file__, result)


def process_line(line):
    openings = []
    for c in line:
        if c in CLOSE_LOOKUP:
            if openings.pop() != CLOSE_LOOKUP[c]:
                return POINT_MAP[c]
        else:
            openings.append(c)

    return 0


def read_input():
    with open(get_input_path_str(__file__), 'r') as f:
        for line in f:
            yield line.strip()


if __name__ == '__main__':
    main()
