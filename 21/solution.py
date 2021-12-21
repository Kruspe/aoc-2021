from collections import Counter

import numpy as np


def solve_1():
    def turn(position, score, first_throw):
        movement = 0
        temp_throw = first_throw
        for i in range(first_throw, first_throw + 3):
            temp_throw = (i % 100) + 1
            movement = movement + temp_throw

        position = int(str(position + movement)[-1])
        if position == 0:
            position = 10
        score += position
        return position, score, temp_throw

    last_throw, rolls = 0, 0
    p1, score_1 = position_1, 0
    p2, score_2 = position_2, 0
    while True:
        p1, score_1, last_throw = turn(p1, score_1, last_throw)
        rolls += 3
        if score_1 >= 1000:
            return score_2 * rolls
        p2, score_2, last_throw = turn(p2, score_2, last_throw)
        rolls += 3
        if score_2 >= 1000:
            return score_1 * rolls


def solve_2():
    def turn(game_key, player_number):
        keys = []
        for i in np.array(np.meshgrid([1, 2, 3], [1, 2, 3], [1, 2, 3])).T.reshape(-1, 3):
            steps = sum(i)
            if player_number == 1:
                position = int(str(game_key[0] + steps)[-1])
                if position == 0:
                    position = 10
                score = game_key[1] + position
                if score < 21:
                    keys.append((position, score, game_key[2], game_key[3]))
            if player_number == 2:
                position = int(str(game_key[2] + steps)[-1])
                if position == 0:
                    position = 10
                score = game_key[3] + position
                if score < 21:
                    keys.append((game_key[0], game_key[1], position, score))
        return keys

    won_1, won_2 = 0, 0
    games = Counter([(position_1, 0, position_2, 0)])
    current_player = 1
    while sum(games.values()) > 0:
        games_copy = games.copy()
        for key, count in games_copy.items():
            if count > 0:
                games[key] -= count
                new_keys = turn(key, current_player)
                if current_player == 1:
                    won_1 += (27 - len(new_keys)) * count
                else:
                    won_2 += (27 - len(new_keys)) * count
                for k in new_keys:
                    games[k] += count
        if current_player == 1:
            current_player = 2
        else:
            current_player = 1

    return max(won_1, won_2)


if __name__ == '__main__':
    position_1, position_2 = [int(line.strip().split(': ')[1]) for line in open('data.txt')]
    print('Part 1', solve_1())
    print('Part 2', solve_2())
