from common.input import get_input_path_str
from common.output import print_output
from common.turgid import LOGGER
from collections import defaultdict

def main():
    '''Given bingo boards and calls, get the score of the winning board.'''
    with open(get_input_path_str(__file__), 'r') as f:
        data = f.read().split('\n\n')

    numbers = data.pop(0).strip().split(',')
    boards = [Board(b) for b in data]

    result = play_bingo(numbers, boards)

    print_output(__file__, result)


def play_bingo(numbers, boards):
    for n in numbers:
        for b in boards:
            b.call(n)
            row_score, col_score = b.check()

            if row_score or col_score:
                return b.sum_uncalled() * int(n)


class Board:
    def __init__(self, data):
        self.not_called = Board.parse_board(data)
        self.called_rows = defaultdict(list)
        self.called_cols = defaultdict(list)

    def sum_uncalled(self):
        return sum([int(v) for v in self.not_called.keys()])

    def call(self, n):
        if n not in self.not_called:
            return False

        (row, col) = self.not_called.pop(n)
        self.called_rows[row].append(int(n))
        self.called_cols[col].append(int(n))

        return True

    def check(self):
        row_score = None
        col_score = None

        for row, called in self.called_rows.items():
            if called and len(called) >= 5:
                row_score = sum(called)

        for col, called in self.called_cols.items():
            if called and len(called) >= 5:
                col_score = sum(called)

        return (row_score, col_score)

    def parse_board(data):
        board = {}
        for y, d in enumerate(data.split('\n')):
            for x, n in enumerate(d.split()):
                board[n] = (x, y)

        return board



if __name__ == '__main__':
    main()
