from collections import Counter
from common.input import get_input_path_str
from common.output import print_output


def main():
    temp, subs = read_input()
    result = calc(temp, subs, 10)
    print_output(__file__, result)


def calc(temp, subs, n):
    for _ in range(n):
        temp = insert(temp, subs)

    c = Counter(temp)
    mc = c.most_common()
    return mc[0][1] - mc[-1][1]


def insert(temp, subs):
    new_temp = ''
    for i in range(len(temp)-1):
        two = temp[i:i+2]

        b = ''
        if two in subs:
            b = subs[two]

        a = temp[i] if i == 0 else ''
        new_temp += a + b + temp[i+1]

    return new_temp


def read_input():
    with open(get_input_path_str(__file__), 'r') as f:
        temp = f.readline().strip()
        subs = [s.split(' -> ') for s in f.read().strip().split('\n')]

    return (temp, {k:v for k, v in subs})


if __name__ == '__main__':
    main()
