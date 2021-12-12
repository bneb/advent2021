from common.input import get_input_path_str
from common.output import print_output
from common.turgid import LOGGER

def main():
    '''Compute the product of binary numbers made from most frequent and infrequent digits.'''
    gamma_data = []

    with open(get_input_path_str(__file__), 'r') as f:
        bits = None
        for line in f:
            bits = bits or int('1' * len(line.strip()), 2)

            for i, b in enumerate(line.strip()):
                if len(gamma_data) <= i:
                    gamma_data.append({})

                gamma_data[i][b] = gamma_data[i].get(b, 0) + 1

    gamma = get_gamma(gamma_data)
    epsilon = gamma ^ bits

    result = gamma * epsilon

    print_output(__file__, result)


def get_gamma(gamma_data):
    '''given frequency of 0 or 1 at each bit, return a number of the most frequent bits.'''
    gamma = 0x0
    for frequency in gamma_data:
        most_frequent_bit = 0 if frequency.get('0') > frequency.get('1') else 1
        gamma <<= 1
        gamma += most_frequent_bit

    return gamma


if __name__ == '__main__':
    main()
