import numpy as np


def fold(m, instruction):
    w, v = instruction
    if w == 'x':
        m1 = m[:, :v]
        m2 = m[:, v + 1:]
        for a, r in enumerate(m2):
            for f, _ in enumerate(r):
                if np.fliplr(m2)[a, f] == '#':
                    m1[a, f] = '#'
        return m1
    elif w == 'y':
        m1 = m[:v]
        m2 = m[v + 1:]
        for a, r in enumerate(m2):
            for f, _ in enumerate(r):
                if np.flipud(m2)[a, f] == '#':
                    m1[a, f] = '#'
        return m1


def solve_1():
    fold_result = fold(marked_map.copy(), fold_instructions[0])
    return len(np.where(fold_result == '#')[0])


def solve_2():
    folded_map = marked_map.copy()
    for i in fold_instructions:
        folded_map = fold(folded_map, i)

    return folded_map


def parse(data):
    seperator = data.index('')
    f = []
    row, col = None, None
    for i in range(seperator + 1, len(data)):
        a, b = data[i].split('fold along ')[1].split('=')
        fold_num = int(b)
        if row is None and a == 'y':
            row = fold_num * 2 + 1
        if col is None and a == 'x':
            col = fold_num * 2 + 1
        f.append((a, fold_num))

    m = np.full((row, col), '.')
    for i in range(seperator):
        x, y = data[i].split(',')
        m[int(y), int(x)] = '#'

    return m, f


if __name__ == '__main__':
    marked_map, fold_instructions = parse([line.strip() for line in open('data.txt')])
    print('Part 1', solve_1())
    print('Part 2')
    print(np.array2string(solve_2(), max_line_width=200))
