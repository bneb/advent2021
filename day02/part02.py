from common.input import get_input_path_str
from common.output import print_output
from common.turgid import LOGGER
from re import match

def main():
    '''Given a list of moves, compute your final position'''
    (x, y) = (0, 0)
    aim = 0

    with open(get_input_path_str(__file__), 'r') as f:
        for line in f:
            delta, aim = get_delta(line, aim)
            x += delta
            y += delta*aim

    result = x*y

    print_output(__file__, result)


def get_delta(line, aim):
    '''given a line return the change in position (x, y).'''
    matches = match('(forward|down|up) (\d+)', line)
    direction = matches.group(1)
    value = int(matches.group(2))

    if direction == 'forward':
        return (value, aim)
    elif direction == 'up':
        return (0, aim-value)
    elif direction == 'down':
        return (0, aim+value)
    else:
        LOGGER.error('invalid direction:', direction, 'parsed from', line)


if __name__ == '__main__':
    main()
