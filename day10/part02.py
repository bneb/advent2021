from common.input import get_input_path_str
from common.output import print_output
from statistics import median

POINTS_MAP = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

CLOSE_LOOKUP = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}

OPEN_LOOKUP = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

def main():
    '''Given open-close pairs, find and score syntax errors.'''
    data = [process_line(line) for line in read_input()]
    result = int(median(sorted([x for x in data if x is not None])))
    print_output(__file__, result)


def process_line(line):
    openings = []
    for c in line:
        if c in CLOSE_LOOKUP:
            if openings.pop() != CLOSE_LOOKUP[c]:
                return None
        else:
            openings.append(c)

    score = 0
    while len(openings) > 0:
        o = openings.pop()
        c = OPEN_LOOKUP[o]
        score *= 5
        score += POINTS_MAP[c]

    return score

def read_input():
    with open(get_input_path_str(__file__), 'r') as f:
        for line in f:
            yield line.strip()


if __name__ == '__main__':
    main()
