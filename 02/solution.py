def solve_1():
    x, y = 0, 0
    for line in lines:
        command, value = line.split(" ")
        value = int(value)
        if command == "forward":
            x += value
        elif command == "down":
            y += value
        else:
            y -= value
    return x * y


def solve_2():
    x, y, z = 0, 0, 0
    for line in lines:
        command, value = line.split(" ")
        value = int(value)
        if command == "forward":
            x += value
            y = y + value * z
        elif command == "down":
            z += value
        else:
            z -= value
    return x * y


if __name__ == '__main__':
    lines = [line.strip() for line in open('data.txt')]
    print('Part 1', solve_1())
    print('Part 2', solve_2())
