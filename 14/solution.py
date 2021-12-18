from collections import Counter


def apply_template(c):
    new_counter = c.copy()
    for key, times in c.items():
        insert = templates[''.join(key)]
        new_counter[(key[0], insert)] += times
        new_counter[insert, (key[1])] += times
        new_counter[key] -= times

    return new_counter


def get_min_max(c):
    counter = Counter()
    for key, times in c.items():
        counter[key[0]] += times
    counter[polymer[-1]] += 1

    return min(counter.values()), max(counter.values())


def solve_1():
    counter = polymer_counter.copy()
    for _ in range(10):
        counter = apply_template(counter)

    min_appearance, max_appearance = get_min_max(counter)
    return max_appearance - min_appearance


def solve_2():
    counter = polymer_counter.copy()
    for _ in range(40):
        counter = apply_template(counter)

    min_appearance, max_appearance = get_min_max(counter)
    return max_appearance - min_appearance


def parse(data):
    p = list(data[0])
    t = {}
    for line in data[2:]:
        pair, insert = line.split(' -> ')
        t[pair] = insert
    return p, Counter(list(zip(p[:-1], p[1:]))), t


if __name__ == '__main__':
    polymer, polymer_counter, templates = parse([line.strip() for line in open('data.txt')])
    print('Part 1', solve_1())
    print('Part 2', solve_2())
