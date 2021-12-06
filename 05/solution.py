import numpy as np


def solve_1():
    result = np.zeros((x, y), dtype=int)
    for spot in spots:
        x1, y1, x2, y2 = spot
        if x1 == x2:
            for i in range(min([y1, y2]), max([y1, y2]) + 1):
                np.add.at(result, (i, x1), 1)
        if y1 == y2:
            for i in range(min([x1, x2]), max([x1, x2]) + 1):
                np.add.at(result, (y1, i), 1)
    return len(np.where(result > 1)[0])


def solve_2():
    result = np.zeros((x, y), dtype=int)
    for spot in spots:
        x1, y1, x2, y2 = spot
        if x1 == x2:
            for i in range(min([y1, y2]), max([y1, y2]) + 1):
                np.add.at(result, (i, x1), 1)
        elif y1 == y2:
            for i in range(min([x1, x2]), max([x1, x2]) + 1):
                np.add.at(result, (y1, i), 1)
        else:
            for i in range(max([x1, x2]) - min([x1, x2]) + 1):
                if x1 > x2:
                    if y1 > y2:
                        np.add.at(result, (y1 - i, x1 - i), 1)
                    else:
                        np.add.at(result, (y1 + i, x1 - i), 1)
                else:
                    if y1 > y2:
                        np.add.at(result, (y1 - i, x1 + i), 1)
                    else:
                        np.add.at(result, (y1 + i, x1 + i), 1)

    return len(np.where(result > 1)[0])


def parse(data):
    l = []
    max_x, max_y = 0, 0
    for line in data:
        line_split = line.split(' -> ')
        temp = []
        for p in line_split:
            split = [int(e) for e in p.split(',')]
            if split[0] > max_x:
                max_x = split[0]
            if split[1] > max_y:
                max_y = split[1]
            temp.extend(split)
        l.append(temp)

    return l, max_x + 1, max_y + 1


if __name__ == '__main__':
    spots, x, y = parse([line.strip() for line in open('data.txt')])
    print('Part 1', solve_1())
    print('Part 2', solve_2())
