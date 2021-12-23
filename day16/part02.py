from common.output import print_output
from day16.part01 import read_input, read_value
from math import prod

def main():
    bin_str = read_input()
    result, _ = process_packet(bin_str, 0)
    print_output(__file__, result)


def process_packet(bin_str, i):
    '''Process a packet, return the value and the updated index.'''
    version = int(bin_str[i:i+3], 2)
    type_id = bin_str[i+3:i+6]

    if type_id == '100':
        i+=6
        value, i = read_value(bin_str, i)
        return value, i

    values = []
    if bin_str[i+6] == '0':
        sublength = int(bin_str[i+7:i+22], 2)
        i += 22
        sublength += i
        while i < sublength:
            value, i = process_packet(bin_str, i)
            values.append(value)
    elif bin_str[i+6] == '1':
        subpackets = int(bin_str[i+7:i+18], 2)
        i += 18
        for _ in range(subpackets):
            value, i = process_packet(bin_str, i)
            values.append(value)

    value = operate(type_id, values)

    return value, i


def operate(type_id, values):
    if type_id == '000': return sum(values)
    if type_id == '001': return prod(values)
    if type_id == '010': return min(values)
    if type_id == '011': return max(values)
    if type_id == '101': return 1 if values[0] > values[1] else 0
    if type_id == '110': return 1 if values[0] < values[1] else 0
    if type_id == '111': return 1 if values[0] == values[1] else 0


if __name__ == '__main__':
    main()
