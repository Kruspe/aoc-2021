import numpy as np


def process_step(data):
    with np.nditer(data, op_flags=['readwrite']) as it:
        for x in it:
            x[...] = x + 1
    blinked = np.asarray(np.where(data > 9)).T.tolist()
    for x, y in blinked:
        go_right = num_cols != y + 1
        go_left = -1 != y - 1
        go_up = -1 != x - 1
        go_down = num_rows != x + 1
        if go_right:
            data[x, y + 1] = data[x, y + 1] + 1
            if data[x, y + 1] > 9 and [x, y + 1] not in blinked:
                blinked.append([x, y + 1])
            if go_up:
                data[x - 1, y + 1] = data[x - 1, y + 1] + 1
                if data[x - 1, y + 1] > 9 and [x - 1, y + 1] not in blinked:
                    blinked.append([x - 1, y + 1])
            if go_down:
                data[x + 1, y + 1] = data[x + 1, y + 1] + 1
                if data[x + 1, y + 1] > 9 and [x + 1, y + 1] not in blinked:
                    blinked.append([x + 1, y + 1])
        if go_left:
            data[x, y - 1] = data[x, y - 1] + 1
            if data[x, y - 1] > 9 and [x, y - 1] not in blinked:
                blinked.append([x, y - 1])
            if go_up:
                data[x - 1, y - 1] = data[x - 1, y - 1] + 1
                if data[x - 1, y - 1] > 9 and [x - 1, y - 1] not in blinked:
                    blinked.append([x - 1, y - 1])
            if go_down:
                data[x + 1, y - 1] = data[x + 1, y - 1] + 1
                if data[x + 1, y - 1] > 9 and [x + 1, y - 1] not in blinked:
                    blinked.append([x + 1, y - 1])
        if go_up:
            data[x - 1, y] = data[x - 1, y] + 1
            if data[x - 1, y] > 9 and [x - 1, y] not in blinked:
                blinked.append([x - 1, y])
        if go_down:
            data[x + 1, y] = data[x + 1, y] + 1
            if data[x + 1, y] > 9 and [x + 1, y] not in blinked:
                blinked.append([x + 1, y])
    for x, y in blinked:
        data[x, y] = 0
    return data, blinked


def solve_1():
    counter = 0
    copy = octopuses.copy()
    for _ in range(100):
        copy, blinked = process_step(copy)
        counter += len(blinked)

    return counter


def solve_2():
    copy = octopuses.copy()
    synced = False
    counter = 0
    while not synced:
        copy, _ = process_step(copy)
        counter += 1
        if np.all(copy == 0):
            return counter



if __name__ == '__main__':
    octopuses = np.array([list(line.strip()) for line in open('data.txt')], dtype=int)
    num_rows, num_cols = octopuses.shape
    print('Part 1', solve_1())
    print('Part 2', solve_2())
