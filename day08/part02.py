from collections import Counter
from common.input import get_input_path_str
from common.output import print_output
from operator import methodcaller
from collections import Counter, defaultdict

def main():
    '''Really complicated. prompt here: https://adventofcode.com/2021/day/8'''
    result = 0
    for i, (signals, outputs) in enumerate(read_input()):
        new_sig_num_map = get_tangled_num_map(signals)
        output_num = 0

        for o in outputs:
            n = new_sig_num_map[frozenset(o)]
            output_num *= 10
            output_num += n

        result += output_num

    print_output(__file__, result)


def set9(num_sig_map, len_sig_map, seg_seg_map):
    four = num_sig_map[4]
    a = seg_seg_map['a']
    sixes = len_sig_map[6]

    for sig in sixes:
        diff = sig - four - set(a)
        if len(diff) == 1:
            len_sig_map[6].remove(sig)
            num_sig_map[9] = sig
            seg_seg_map['g'] = diff.pop()
            break


def set6(num_sig_map, len_sig_map, seg_seg_map):
    one   = num_sig_map[1]
    eight = num_sig_map[8]
    sixes = len_sig_map[6]

    for sig in sixes:
        if (sig | one) == eight:
            len_sig_map[6].remove(sig)
            num_sig_map[6] = sig
            break


def set0(num_sig_map, len_sig_map, seg_seg_map):
    zero = len_sig_map[6].pop()
    eight = num_sig_map[8]
    d = (eight - zero).pop()
    seg_seg_map['d'] = d
    num_sig_map[0] = zero



def setE(num_sig_map, len_sig_map, seg_seg_map):
    eight = num_sig_map[8]
    nine  = num_sig_map[9]
    e = (eight - nine).pop()
    seg_seg_map['e'] = e


def setB(num_sig_map, len_sig_map, seg_seg_map):
    four  = num_sig_map[4]
    seven = num_sig_map[7]
    d = seg_seg_map['d']
    b = four - seven - set(d)
    seg_seg_map['b'] = b


def set3(num_sig_map, len_sig_map, seg_seg_map):
    nine = num_sig_map[9]
    b = seg_seg_map['b']
    three = nine - set(b)
    num_sig_map[3] = three
    len_sig_map[5].remove(three)


def setC(num_sig_map, len_sig_map, seg_seg_map):
    three = num_sig_map[3]
    six   = num_sig_map[6]
    c = (three - six).pop()
    seg_seg_map['c'] = c


def setF(num_sig_map, len_sig_map, seg_seg_map):
    one = num_sig_map[1]
    c = seg_seg_map['c']
    f = (one - set(c)).pop()
    seg_seg_map['f'] = f


def set2(num_sig_map, len_sig_map, seg_seg_map):
    eight = num_sig_map[8]
    b = seg_seg_map['b']
    f = seg_seg_map['f']
    two = eight - set(b) - set(f)
    num_sig_map[2] = two
    len_sig_map[5].remove(two)


def set5(num_sig_map, len_sig_map, seg_seg_map):
    nine = num_sig_map[9]
    c = seg_seg_map['c']
    five = nine - set(c)
    num_sig_map[5] = five
    len_sig_map[5].remove(five)


def get_tangled_num_map(signals):
    len_sig_map = defaultdict(list)
    for s in signals:
        len_sig_map[len(s)].append(set(s))

    new_num_seg_map = {
        1: len_sig_map[2].pop(),
        4: len_sig_map[4].pop(),
        7: len_sig_map[3].pop(),
        8: len_sig_map[7].pop()
    }

    seg_seg_map = {'a': (new_num_seg_map[7] - new_num_seg_map[1]).pop()}

    set9(new_num_seg_map, len_sig_map, seg_seg_map)
    set6(new_num_seg_map, len_sig_map, seg_seg_map)
    set0(new_num_seg_map, len_sig_map, seg_seg_map)
    setE(new_num_seg_map, len_sig_map, seg_seg_map)
    setB(new_num_seg_map, len_sig_map, seg_seg_map)
    # 1, 4, 6, 7, 8, 9, 0 are set
    # a, b, d, e, g are set
    set3(new_num_seg_map, len_sig_map, seg_seg_map)
    setC(new_num_seg_map, len_sig_map, seg_seg_map)
    setF(new_num_seg_map, len_sig_map, seg_seg_map)
    # 1, 3, 4, 6, 7, 8, 9, 0 are set
    # a, b, c, d, e, f, g are set
    set2(new_num_seg_map, len_sig_map, seg_seg_map)
    set5(new_num_seg_map, len_sig_map, seg_seg_map)

    new_seg_num_map = {frozenset(v): k for k, v in new_num_seg_map.items()}
    return new_seg_num_map


def read_input():
    with open(get_input_path_str(__file__), 'r') as f:
        for line in f:
            yield tuple(map(methodcaller('split'), line.split(' | ')))


if __name__ == '__main__':
    main()
