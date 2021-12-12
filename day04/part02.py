from common.input import get_input_path_str
from common.output import print_output
from common.turgid import LOGGER
from day04.part01 import Board

def main():
    '''Given bingo boards and calls, get the score of the last winning board.'''
    with open(get_input_path_str(__file__), 'r') as f:
        data = f.read().split('\n\n')

    numbers = data.pop(0).strip().split(',')
    boards = [Board(b) for b in data]

    result = play_bingo(numbers, boards)

    print_output(__file__, result)


def play_bingo(numbers, boards):
    for n in numbers:
        for b in list(boards):
            b.call(n)
            row_score, col_score = b.check()

            if row_score or col_score:
                if len(boards) == 1:
                    return boards.pop().sum_uncalled() * int(n)
                boards.remove(b)


if __name__ == '__main__':
    main()
