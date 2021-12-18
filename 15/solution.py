import heapq
from collections import defaultdict

import numpy as np


def solve(risk_map):
    def create_graph():
        g = {}
        for row_index, row in enumerate(risk_map):
            for col_index, risk in enumerate(row):
                neighbors = {}
                if -1 != row_index - 1:
                    if (row_index - 1, col_index) != (0, 0):
                        neighbors[row_index - 1, col_index] = risk_map[row_index - 1, col_index]
                if -1 != col_index - 1:
                    if (row_index, col_index - 1) != (0, 0):
                        neighbors[row_index, col_index - 1] = risk_map[row_index, col_index - 1]
                if num_cols != col_index + 1:
                    if (row_index, col_index + 1) != (0, 0):
                        neighbors[row_index, col_index + 1] = risk_map[row_index, col_index + 1]
                if num_rows != row_index + 1:
                    if (row_index + 1, col_index) != (0, 0):
                        neighbors[row_index + 1, col_index] = risk_map[row_index + 1, col_index]
                g[(row_index, col_index)] = neighbors
        return g

    num_rows, num_cols = risk_map.shape
    graph = create_graph()
    visited = set()
    pq = []
    node_costs = defaultdict(lambda: float('inf'))
    node_costs[(0, 0)] = 0
    heapq.heappush(pq, (0, (0, 0)))

    while pq:
        _, node = heapq.heappop(pq)
        visited.add(node)

        for adjacent_node, weight in graph[node].items():
            if adjacent_node in visited:
                continue

            new_cost = node_costs[node] + weight
            if node_costs[adjacent_node] > new_cost:
                node_costs[adjacent_node] = new_cost
                heapq.heappush(pq, (new_cost, adjacent_node))

    return node_costs[max(node_costs.keys())]


def parse(data):
    c = []
    for line in data:
        c.append([int(i) for i in list(line)])

    return np.array(c)


def parse_2(data):
    result = data
    adder = np.full(data.shape, 1)
    big_map = [data.copy()]
    increased = np.add(data, adder)
    increased = np.where(increased == 10, 1, increased)

    for _ in range(4):
        big_map.append(increased.copy())
        result = np.concatenate((result, increased.copy()), 1)
        increased = np.add(increased, adder)
        increased = np.where(increased == 10, 1, increased)

    big_map = [big_map.copy()]
    for i in range(4):
        next_row = big_map[i][1:]
        next_row.append(increased)
        row = next_row[0]
        for a in range(4):
            row = np.concatenate((row, next_row[a + 1]), 1)
        result = np.concatenate((result, row))

        increased = np.add(increased, adder)
        increased = np.where(increased == 10, 1, increased)
        big_map.append(next_row)

    return result


if __name__ == '__main__':
    chiton_risk = parse([line.strip() for line in open('data.txt')])
    print('Part 1', solve(chiton_risk.copy()))
    print('Part 2', solve(parse_2(chiton_risk)))
