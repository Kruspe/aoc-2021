import numpy as np


def solve_1():
    result = []
    coordinates = []
    for (x, y), item in np.ndenumerate(height_map):
        low_spot = True
        if low_spot and x > 0:
            low_spot = height_map[x - 1, y] > item
        if low_spot and x < num_rows - 1:
            low_spot = height_map[x + 1, y] > item
        if low_spot and y > 0:
            low_spot = height_map[x, y - 1] > item
        if low_spot and y < num_cols - 1:
            low_spot = height_map[x, y + 1] > item
        if low_spot:
            result.append(item)
            coordinates.append((x, y))
    return result, coordinates


def solve_2():
    def basin(a, b):
        height = height_map[a, b]
        r = {(a, b)}
        if num_cols != b + 1 and height_map[a, b + 1] > height and height_map[a, b + 1] != 9:
            r = r.union(basin(a, b + 1))
        if -1 != a - 1 and height_map[a - 1, b] > height and height_map[a - 1, b] != 9:
            r = r.union(basin(a - 1, b))
        if -1 != b - 1 and height_map[a, b - 1] > height and height_map[a, b - 1] != 9:
            r = r.union(basin(a, b - 1))
        if num_rows != a + 1 and height_map[a + 1, b] > height and height_map[a + 1, b] != 9:
            r = r.union(basin(a + 1, b))
        return r

    result = []
    for (x, y) in low_points:
        basin_len = len(basin(x, y))
        if len(result) < 3:
            result.append(basin_len)
        elif min(result) < basin_len:
            result.remove(min(result))
            result.append(basin_len)
    return np.prod(result)


def parse(data):
    r = []
    for line in data:
        r.append(list(map(lambda x: int(x), list(line))))
    return np.array(r)


if __name__ == '__main__':
    height_map = parse([line.strip() for line in open('data.txt')])
    num_rows, num_cols = height_map.shape
    numbers, low_points = solve_1()
    print('Part 1', sum(map(lambda a: a + 1, numbers)))
    print('Part 2', solve_2())
