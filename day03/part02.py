from common.input import get_input_path_str
from common.output import print_output
from common.turgid import LOGGER

def main():
    '''Compute the product of binary numbers made from most frequent and infrequent digits.'''
    o2_data = None

    with open(get_input_path_str(__file__), 'r') as f:
        o2_data = f.read().splitlines()

    co2_data = o2_data.copy()

    for i in range(len(o2_data[0])):
        zeros, ones = get_frequency_at(o2_data, i)
        o2_data = get_list_for_bit(o2_data, '0' if zeros > ones else '1', i)

        zeros, ones = get_frequency_at(co2_data, i)
        co2_data = get_list_for_bit(co2_data, '0' if zeros <= ones else '1', i)

    o2 = int(o2_data.pop(), 2)
    co2 = int(co2_data.pop(), 2)

    result = o2 * co2

    print_output(__file__, result)


def get_list_for_bit(binary_strs, bit, n):
    '''Yield binary strings having the matching bit at position n.'''
    if len(binary_strs) == 1:
        return binary_strs

    return [s for s in binary_strs if s[n] == bit]


def get_frequency_at(binary_strs, n):
    '''Calculate the bit frequency at position n from the left.'''
    zeros = 0
    ones = 0

    for s in binary_strs:
        if s[n] == '1':
            ones += 1
        else:
            zeros += 1

    return (zeros, ones)


if __name__ == '__main__':
    main()
