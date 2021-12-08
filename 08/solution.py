def solve_1():
    counter = 0
    for output in outputs:
        for item in output:
            if len(item) == 2 or len(item) == 3 or len(item) == 4 or len(item) == 7:
                counter += 1
    return counter


def solve_2():
    result = []
    for index in range(len(patterns)):
        all_patterns = patterns[index].copy()
        all_patterns.extend(outputs[index])
        pattern_map = {}
        nine = None
        seven = None
        four = None
        for pattern in all_patterns:
            if len(pattern) == 2:
                pattern_map["".join(sorted(pattern))] = 1

            if len(pattern) == 3:
                pattern_map["".join(sorted(pattern))] = 7
                seven = "".join(sorted(pattern))
                for i in all_patterns:
                    if len(i) == 5:
                        counter = 0
                        for c in pattern:
                            if c in i:
                                counter += 1
                        if counter == 3:
                            pattern_map["".join(sorted(i))] = 3

            if len(pattern) == 7:
                pattern_map["".join(sorted(pattern))] = 8

            if len(pattern) == 4:
                pattern_map["".join(sorted(pattern))] = 4
                four = "".join(sorted(pattern))

        for i in all_patterns:
            if len(i) == 6:
                counter_four, counter_seven = 0, 0
                for c in four:
                    if c in i:
                        counter_four += 1
                for c in seven:
                    if c in i:
                        counter_seven += 1
                if counter_four == 4:
                    pattern_map["".join(sorted(i))] = 9
                    nine = "".join(sorted(i))
                elif counter_four == 3 and counter_seven == 3:
                    pattern_map["".join(sorted(i))] = 0
                elif counter_four == 3 and counter_seven == 2:
                    pattern_map["".join(sorted(i))] = 6

        for i in all_patterns:
            if len(i) == 5:
                counter = 0
                for c in nine:
                    if c in i:
                        counter += 1
                if counter == 5 and "".join(sorted(i)) not in pattern_map.keys():
                    pattern_map["".join(sorted(i))] = 5
                elif counter == 4 and "".join(sorted(i)) not in pattern_map.keys():
                    pattern_map["".join(sorted(i))] = 2

        number = ''
        for output in outputs[index]:
            number += str(pattern_map["".join(sorted(output))])
        result.append(int(number))
    return sum(result)


def parse(data):
    p, o = [], []
    for line in data:
        split_line = line.split(' | ')
        p.append(split_line[0].split(' '))
        o.append(split_line[1].split(' '))
    return p, o


if __name__ == '__main__':
    patterns, outputs = parse([line.strip() for line in open('data.txt')])
    print('Part 1', solve_1())
    print('Part 2', solve_2())
