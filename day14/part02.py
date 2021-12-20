from collections import Counter
from common.input import get_input_path_str
from common.output import print_output
from day14.part01 import read_input


def main():
    start_string, subs = read_input()
    result = calc(start_string, subs, 40)
    print_output(__file__, result)


def calc(start_string, subs, n):
    pair_counts = Counter(zip(start_string[:-1], start_string[1:]))
    letter_counts = Counter(start_string)

    for _ in range(n):
        pair_counts = insert(pair_counts, subs, letter_counts)

    ranked_letter_counts = letter_counts.most_common()
    hi_freq = ranked_letter_counts[0][1]
    lo_freq = ranked_letter_counts[-1][1]

    return hi_freq - lo_freq


def insert(pair_counts, subs, letter_counts):
    new_pair_counts = Counter()

    for (a, c), count in pair_counts.items():
        b = subs.get((a, c), None)
        if b:
            new_pair_counts[(a, b)] += count
            new_pair_counts[(b, c)] += count
        else:
            new_pair_counts[(a, c)] += count
        letter_counts[b] += count

    return new_pair_counts


if __name__ == '__main__':
    main()
