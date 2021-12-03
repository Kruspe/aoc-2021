def solve_1():
    gamma, epsilon = '', ''
    for i in range(len(lines[0])):
        if mapped_bits[i]['0'] > mapped_bits[i]['1']:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
    return int(gamma, 2) * int(epsilon, 2)


def solve_2():
    oxygen_input, co2_input = lines, lines
    for i in range(len(lines[0])):
        mapped_o = parse(oxygen_input)
        mapped_c = parse(co2_input)
        filtered_o, filtered_c = [], []
        if len(oxygen_input) > 1:
            if mapped_o[i]['1'] >= mapped_o[i]['0']:
                for o in oxygen_input:
                    if o[i] == '1':
                        filtered_o.append(o)
            else:
                for o in oxygen_input:
                    if o[i] == '0':
                        filtered_o.append(o)
            oxygen_input = filtered_o
        if len(co2_input) > 1:
            if mapped_c[i]['1'] >= mapped_c[i]['0']:
                for c in co2_input:
                    if c[i] == '0':
                        filtered_c.append(c)
            else:
                for c in co2_input:
                    if c[i] == '1':
                        filtered_c.append(c)
            co2_input = filtered_c
        if len(oxygen_input) == 1 and len(co2_input) == 1:
            return int(oxygen_input[0], 2) * int(co2_input[0], 2)

    raise Exception("No value found for oxygen or co2")


def parse(l):
    mb = {}
    for i in range(len(l[0])):
        mb[i] = {'0': 0, '1': 0}
    for line in l:
        for i, bit in enumerate(line):
            mb[i][bit] = mb[i][bit] + 1
    return mb


if __name__ == '__main__':
    lines = [line.strip() for line in open('data.txt')]
    mapped_bits = parse(lines)
    print('Part 1', solve_1())
    print('Part 2', solve_2())
