import numpy as np


def has_won(board):
    for row in board:
        if np.all(row == -1):
            return True
    for row in np.transpose(board):
        if np.all(row == -1):
            return True
    return False


def solve_1():
    def find_winning_board():
        fields_copy = fields.copy()
        for n in numbers:
            temp = []
            for field in fields_copy.copy():
                replaced_field = np.where(field == n, -1, field)
                if has_won(replaced_field):
                    return replaced_field, n
                temp.append(replaced_field)
            fields_copy = temp

    b, last_n = find_winning_board()
    return (b.sum() + np.count_nonzero(b == -1)) * last_n


def solve_2():
    def find_last_board():
        fields_copy = fields.copy()
        for n in numbers:
            temp = []
            for field in fields_copy.copy():
                replaced_field = np.where(field == n, -1, field)
                won = has_won(replaced_field)
                if len(fields_copy) == 1 and won:
                    return replaced_field, n
                if won is False:
                    temp.append(replaced_field)
            fields_copy = temp

    b, last_n = find_last_board()
    return (b.sum() + np.count_nonzero(b == -1)) * last_n


def parse(data):
    n = [int(i) for i in data[0].split(',')]
    p, field, row = [], [], []
    for i, line in enumerate(data[2:]):
        if line:
            for a in line.split(' '):
                if a:
                    row.append(int(a.strip()))
            field.append(row.copy())
            row = []
        if len(field) == 5:
            p.append(np.array(field))
            field = []

    return n, p


if __name__ == '__main__':
    numbers, fields = parse([line.strip() for line in open('data.txt')])
    print('Part 1', solve_1())
    print('Part 2', solve_2())
