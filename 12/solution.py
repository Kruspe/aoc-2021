from collections import defaultdict


def solve_1():
    def gen_way(way):
        for next_point in connection_map[way[-1]]:
            if next_point == 'end':
                ways.append(way)
            elif next_point.isupper() or next_point.islower() and next_point not in way:
                copied_way = way.copy()
                copied_way.append(next_point)
                gen_way(copied_way)

    ways = []
    for p in connection_map['start']:
        gen_way([p])
    return len(ways)


def solve_2():
    def gen_way(way):
        contains_two_lower = False
        for lc in lower_caves:
            if way.count(lc) == 2:
                contains_two_lower = True
        for next_point in connection_map[way[-1]]:
            if next_point == 'end':
                ways.append(way)
            elif contains_two_lower and next_point.islower() and next_point not in way or next_point.isupper():
                copied_way = way.copy()
                copied_way.append(next_point)
                gen_way(copied_way)
            elif not contains_two_lower:
                copied_way = way.copy()
                copied_way.append(next_point)
                gen_way(copied_way)

    lower_caves = list(filter(lambda x: x.islower(), connection_map.keys()))
    ways = []
    for p in connection_map['start']:
        gen_way([p])
    return len(ways)


def parse(data):
    c = defaultdict(set)
    for line in data:
        start, end = line.split('-')
        if start == 'start':
            c[start].add(end)
        elif end == 'start':
            c[end].add(start)
        elif start == 'end':
            c[end].add(start)
        elif end == 'end':
            c[start].add(end)
        else:
            c[start].add(end)
            c[end].add(start)
    return c


if __name__ == '__main__':
    connection_map = parse([line.strip() for line in open('data.txt')])
    print('Part 1', solve_1())
    print('Part 2', solve_2())
