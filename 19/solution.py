from collections import Counter, defaultdict


def solve():
    def transform(point):
        return [
            [point[0], point[1], point[2]],
            [point[0], -point[1], -point[2]],
            [-point[0], -point[1], point[2]],
            [-point[0], point[1], -point[2]],
            [point[0], point[2], -point[1]],
            [point[0], -point[2], point[1]],
            [-point[0], -point[2], -point[1]],
            [-point[0], point[2], point[1]],

            [point[1], point[0], -point[2]],
            [point[1], -point[0], point[2]],
            [-point[1], point[0], point[2]],
            [-point[1], -point[0], -point[2]],
            [point[1], point[2], point[0]],
            [point[1], -point[2], -point[0]],
            [-point[1], point[2], -point[0]],
            [-point[1], -point[2], point[0]],

            [point[2], point[0], point[1]],
            [point[2], -point[0], -point[1]],
            [-point[2], -point[0], point[1]],
            [-point[2], point[0], -point[1]],
            [point[2], point[1], -point[0]],
            [point[2], -point[1], point[0]],
            [-point[2], -point[1], -point[0]],
            [-point[2], point[1], point[0]]
        ]

    def find_overlap(d):
        for k, distances_for_transformation in d.items():
            counter = Counter(distances_for_transformation)
            for result, amount in counter.items():
                if amount >= 12:
                    return k, result

    def find_match(sc):
        for scanner_key, beacon_list in sc.items():
            distances = defaultdict(list)
            for beacon in scanners[0]:
                for point in beacon_list:
                    for i, transformed in enumerate(transform(point)):
                        distance = (beacon[0] - transformed[0], beacon[1] - transformed[1], beacon[2] - transformed[2])
                        distances[i].append(distance)

            overlap = find_overlap(distances)
            if overlap is not None:
                return scanner_key, overlap[0], overlap[1],

    scanners_to_check = scanners.copy()
    scanners_to_check.pop(0)
    location_of_scanners = []
    while scanners_to_check:
        scanner_to_remove, transformation_key, distance_to_use = find_match(scanners_to_check)
        location_of_scanners.append(distance_to_use)
        for p in scanners[scanner_to_remove]:
            transformed_p = transform(p)[transformation_key]
            scanners[0].add((transformed_p[0] + distance_to_use[0], transformed_p[1] + distance_to_use[1],
                             transformed_p[2] + distance_to_use[2]))
        scanners_to_check.pop(scanner_to_remove)

    max_dist = 0
    for i, scanner in enumerate(location_of_scanners):
        for other_scanner in location_of_scanners[i + 1:]:
            man_distance = sum(abs(x - y) for x, y in zip(scanner, other_scanner))
            if max_dist < man_distance:
                max_dist = man_distance

    return len(scanners[0]), max_dist


def parse(data):
    s = {}
    scanner_starts = []
    for i, line in enumerate(data):
        if line.startswith('--- sc'):
            scanner_starts.append(i)

    for i, scanner in enumerate(scanner_starts[:-1]):
        beacons = set()
        for line in data[scanner + 1:scanner_starts[i + 1] - 1]:
            beacons.add(tuple(map(lambda x: int(x), line.split(','))))
        s[i] = beacons

    beacons = set()
    for line in data[scanner_starts[len(scanner_starts) - 1] + 1:]:
        beacons.add(tuple(map(lambda x: int(x), line.split(','))))
    s[len(scanner_starts) - 1] = beacons

    return s


if __name__ == '__main__':
    scanners = parse([line.strip() for line in open('data.txt')])
    number_of_beacons, furthest_distance = solve()
    print('Part 1', number_of_beacons)
    print('Part 2', furthest_distance)
