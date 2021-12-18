from io import StringIO
from math import prod


def solve(buffer):
    global version_sum

    def get_info():
        return int(buffer.read(3), 2), int(buffer.read(3), 2)

    def literal():
        n = ''
        while True:
            if buffer.read(1) == '0':
                return int(n + buffer.read(4), 2)
            else:
                n += buffer.read(4)

    version, type_id = get_info()
    version_sum += version
    if type_id == 4:
        return literal()

    packets = []
    if buffer.read(1) == '0':
        length = int(buffer.read(15), 2)
        target_length = buffer.tell() + length
        while buffer.tell() != target_length:
            packets.append(solve(buffer))
    else:
        amount = int(buffer.read(11), 2)
        for _ in range(amount):
            packets.append(solve(buffer))

    if type_id == 0:
        return sum(packets)
    if type_id == 1:
        return prod(packets)
    if type_id == 2:
        return min(packets)
    if type_id == 3:
        return max(packets)
    if type_id == 5:
        return int(packets[0] > packets[1])
    if type_id == 6:
        return int(packets[0] < packets[1])
    if type_id == 7:
        return int(packets[0] == packets[1])


def parse(data):
    b = bin(int(data, 16))[2:]
    b = b.zfill(len(data) * 4)
    padding = 0 if len(b) % 4 == 0 else 4 - len(b) % 4
    return StringIO(b.zfill(len(b) + padding))


if __name__ == '__main__':
    version_sum = 0
    binary = parse([line.strip() for line in open('data.txt')][0])
    result = solve(binary)
    print('Part 1', version_sum)
    print('Part 2', result)
