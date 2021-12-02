if __name__ == '__main__':
    lines = [int(line.strip()) for line in open('data.txt')]
    counter1 = 0
    for i, line in enumerate(lines[1:]):
        if lines[i] < line:
            counter1 += 1

    counter2 = 0
    mappedInput = {}
    for i, _ in enumerate(lines[:-2]):
        mappedInput[i] = lines[i] + lines[i + 1] + lines[i + 2]
    for i in range(len(mappedInput.keys()) - 1):
        if mappedInput[i] < mappedInput[i + 1]:
            counter2 += 1
    print('Part 1', counter1)
    print('Part 2', counter2)
