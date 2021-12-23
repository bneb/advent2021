from common.input import get_input_path_str
from common.output import print_output

def main():
    bin_str = read_input()
    result, _ = process_packet(bin_str, 0)
    print_output(__file__, result)


def process_packet(bin_str, i):
    '''Process a packet, return the version and the updated index.'''
    version = int(bin_str[i:i+3], 2)
    ptype = bin_str[i+3:i+6]

    if ptype == '100':
        i+=6
        value, i = read_value(bin_str, i)
        return version, i
    elif bin_str[i+6] == '0':
        sublength = int(bin_str[i+7:i+22], 2)
        i += 22
        sublength += i
        while i < sublength:
            next_version, i = process_packet(bin_str, i)
            version += next_version
    elif bin_str[i+6] == '1':
        subpackets = int(bin_str[i+7:i+18], 2)
        i += 18
        for _ in range(subpackets):
            next_version, i = process_packet(bin_str, i)
            version += next_version

    return version, i


def read_value(bin_str, i):
    '''Given 5 bits, read the last 4. If the first is 1, read the next five.
    Returns the binary number from the read bits, and the updated index.'''
    n = ''

    while bin_str[i] == '1':
        n += bin_str[i+1:i+5]
        i += 5

    n += bin_str[i+1:i+5]

    return int(n, 2), i+5


def read_input():
    '''Read the one line of input. Convert from hex to binary and pad 0's.'''
    with open(get_input_path_str(__file__), 'r') as f:
        hex_str = f.read().strip()
        hex_num = int(hex_str, 16)
        fill_width = len(hex_str) * 4 # 4 bits for each hex char
        bin_str = bin(hex_num)[2:].zfill(fill_width) # remove '0b' and pad with 0

        return bin_str


if __name__ == '__main__':
    main()
