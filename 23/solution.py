from functools import cache


def solve_1():
    @cache
    def move(piece, up, lor, down):
        if piece == 'A':
            return up + lor + down
        if piece == 'B':
            return 10 * (up + lor + down)
        if piece == 'C':
            return 100 * (up + lor + down)
        if piece == 'D':
            return 1000 * (up + lor + down)

    
    print(row_2)
    print(row_3)
    print(row_4)


def parse(data):
    upper_row = data[2].split('###')[1].split('#')
    lower_row = data[3].split('#')

    r1 = [lower_row[1], upper_row[0]]
    r2 = [lower_row[2], upper_row[1]]
    r3 = [lower_row[3], upper_row[2]]
    r4 = [lower_row[4], upper_row[3]]

    return r1, r2, r3, r4


if __name__ == '__main__':
    row_1, row_2, row_3, row_4 = parse([line.strip() for line in open('sample.txt')])
    print('Part 1', solve_1())
    # print('Part 2', solve_2())
