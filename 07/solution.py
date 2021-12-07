def solve_1():
    min_position, max_position = min(positions), max(positions)
    min_fuel_cost = None
    for i in range(min_position, max_position + 1):
        fuel_cost = 0
        for position in positions:
            fuel_cost += abs(i - position)
        if min_fuel_cost is None or fuel_cost < min_fuel_cost:
            min_fuel_cost = fuel_cost

    return min_fuel_cost


def solve_2():
    min_position, max_position = min(positions), max(positions)
    min_fuel_cost = None
    for i in range(min_position, max_position + 1):
        fuel_cost = 0
        for position in positions:
            n = abs(i - position)
            fuel_cost += int((n * (n + 1)) / 2)
        if min_fuel_cost is None or fuel_cost < min_fuel_cost:
            min_fuel_cost = fuel_cost

    return min_fuel_cost


if __name__ == '__main__':
    line = [line.strip() for line in open('data.txt')]
    positions = [int(i) for i in line[0].split(',')]
    print('Part 1', solve_1())
    print('Part 2', solve_2())
