import numpy as np


def all_solutions():
    def get_min_x():
        x = 0
        while True:
            x += 1
            if (x * (x + 1)) / 2 >= range_x[0]:
                return x

    possible_x = list(range(get_min_x(), range_x[1] + 1))
    possible_y = list(range(range_y[0], -range_y[0]))

    solutions = set()
    for s in np.array(np.meshgrid(possible_x, possible_y)).T.reshape(-1, 2):
        step, position_x, position_y = 0, 0, 0
        while True:
            if step < s[0]:
                position_x += s[0] - step
            position_y += s[1] - step
            if position_x > range_x[1] or position_y < range_y[0]:
                break
            if range_x[0] <= position_x <= range_x[1] and range_y[1] >= position_y >= range_y[0]:
                solutions.add((s[0], s[1]))
                break
            step += 1

    return len(solutions)


def parse(data):
    x, y = data.split('target area: x=')[1].split(', y=')
    return list(map(lambda a: int(a), x.split('..'))), list(map(lambda a: int(a), y.split('..')))


if __name__ == '__main__':
    range_x, range_y = parse([line.strip() for line in open('data.txt')][0])
    print('Part 1', int(((-range_y[0] - 1) * -range_y[0]) / 2))
    print('Part 2', all_solutions())
