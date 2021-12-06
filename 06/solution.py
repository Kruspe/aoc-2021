from collections import Counter


def solve(days):
    c = Counter(fish)
    for _ in range(days):
        n = Counter()
        for key in c:
            if key == 0:
                n[6] += c[key]
                n[8] = c[key]
            elif key == 7:
                n[6] += c[key]
            else:
                n[key - 1] = c[key]
        c = n
    return sum(c.values())


if __name__ == '__main__':
    line = [line.strip() for line in open('data.txt')]
    fish = [int(i) for i in line[0].split(',')]
    print('Part 1', solve(80))
    print('Part 2', solve(256))
