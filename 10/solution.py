def solve_1():
    points = {')': 3, ']': 57, '}': 1197, '>': 25137}
    opening_brackets = '([{<'

    remaining_brackets = []
    score = 0
    for line in lines:
        brackets = []
        is_corrupted = False
        for char in line:
            if char in opening_brackets:
                brackets.append(char)
            else:
                expected_closing_bracket = closing_bracket_ref[brackets.pop()]
                if expected_closing_bracket != char:
                    is_corrupted = True
                    score += points[char]
                    break
        if not is_corrupted:
            remaining_brackets.append(''.join(brackets))
    return score, remaining_brackets


def solve_2(i):
    points = {')': 1, ']': 2, '}': 3, '>': 4}
    scores = []
    for brackets in i:
        score = 0
        for bracket in reversed(brackets):
            score = score * 5 + points[closing_bracket_ref[bracket]]
        scores.append(score)
    return sorted(scores)[int((len(scores) - 1) / 2)]


if __name__ == '__main__':
    closing_bracket_ref = {'(': ')', '[': ']', '{': '}', '<': '>'}
    lines = [line.strip() for line in open('data.txt')]
    s, r = solve_1()
    print('Part 1', s)
    print('Part 2', solve_2(r))
