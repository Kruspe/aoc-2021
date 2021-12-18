import math

import numpy as np


class Number:
    left, right = None, None

    def __init__(self, n, parent, position, depth):
        self.parent = parent
        self.position = position
        self.depth = depth

        center = None
        if n[1].isdecimal():
            center = n.find(',')
            self.left = int(n[1:center])
        if n[-2].isdecimal():
            center = n.rfind(',')
            self.right = int(n[center + 1:-1])

        if center:
            if self.left is None:
                self.left = Number(n[1:center], self, 'left', depth + 1)
            if self.right is None:
                self.right = Number(n[center + 1:-1], self, 'right', depth + 1)
        else:
            open_brackets, closing_brackets, open_index, closing_index = [], [], 0, 0
            while n[1:-1].find('[', open_index) != -1:
                open_index = n[1:-1].find('[', open_index) + 1
                open_brackets.append(open_index)
            while n[1:-1].find(']', closing_index) != -1:
                closing_index = n[1:-1].find(']', closing_index) + 1
                closing_brackets.append(closing_index)
            counter = 1
            while True:
                if open_brackets[counter] > closing_brackets[counter - 1]:
                    break
                counter += 1
            self.left = Number(n[1:open_brackets[counter] - 1], self, 'left', depth + 1)
            self.right = Number(n[open_brackets[counter]:-1], self, 'right', depth + 1)

    def __str__(self):
        return '[' + str(self.left) + ',' + str(self.right) + ']'

    def has_left_child(self):
        return type(self.left) is not int

    def has_right_child(self):
        return type(self.right) is not int


def explode(node: Number):
    parent = node.parent
    if node.position == 'right':
        if parent.has_left_child():
            temp = parent.left
            while temp.has_right_child():
                temp = temp.right
            temp.right += node.left
        else:
            parent.left += node.left

        temp = parent
        while temp.position == 'right':
            temp = temp.parent
        if temp.position != 'root':
            if temp.parent.has_right_child():
                temp = temp.parent.right
                while temp.has_left_child():
                    temp = temp.left
                temp.left += node.right
            else:
                temp.parent.right += node.right
        parent.right = 0
    else:
        if parent.has_right_child():
            temp = parent.right
            while temp.has_left_child():
                temp = temp.left
            temp.left += node.right
        else:
            parent.right += node.right

        temp = parent
        while temp.position == 'left':
            temp = temp.parent
        if temp.position != 'root':
            if temp.parent.has_left_child():
                temp = temp.parent.left
                while temp.has_right_child():
                    temp = temp.right
                temp.right += node.left
            else:
                temp.parent.left += node.left
        parent.left = 0


def split(node: Number, side: str):
    if side == 'left':
        node_num = node.left
        node.left = Number('[' + str(math.floor(node_num / 2)) + ',' + str(math.ceil(node_num / 2)) + ']', node, side, node.depth + 1)
    else:
        node_num = node.right
        node.right = Number('[' + str(math.floor(node_num / 2)) + ',' + str(math.ceil(node_num / 2)) + ']', node, side, node.depth + 1)


def search_deep_node(node: Number):
    if node.depth >= 4 and not node.has_left_child() and not node.has_right_child():
        return node
    if node.has_left_child():
        deep_node = search_deep_node(node.left)
        if deep_node:
            return deep_node
    if node.has_right_child():
        return search_deep_node(node.right)


def search_big_node(node: Number):
    if node.has_left_child():
        big_node = search_big_node(node.left)
        if big_node:
            return big_node
    else:
        if node.left > 9:
            return node, 'left'
    if node.has_right_child():
        return search_big_node(node.right)
    else:
        if node.right > 9:
            return node, 'right'


def get_magnitude(node: Number):
    if node.has_left_child():
        node.left = get_magnitude(node.left)
    if node.has_right_child():
        node.right = get_magnitude(node.right)
    return node.left * 3 + node.right * 2


def add(node: Number):
    while True:
        changed = False
        node_to_explode = search_deep_node(node)
        while node_to_explode:
            changed = True
            explode(node_to_explode)
            node_to_explode = search_deep_node(node)
        result = search_big_node(node)
        if result:
            changed = True
            split(result[0], result[1])
        if not changed:
            break


def solve_1():
    number = str(numbers[0])
    for n in numbers[1:]:
        number = Number('[' + str(number) + ',' + n + ']', None, 'root', 0)
        add(number)

    return get_magnitude(number)


def solve_2():
    magnitudes = []
    for combination in np.array(np.meshgrid(numbers, numbers)).T.reshape(-1, 2):
        number = Number('[' + str(combination[0]) + ',' + combination[1] + ']', None, 'root', 0)
        add(number)
        magnitudes.append(get_magnitude(number))
    return max(magnitudes)


if __name__ == '__main__':
    numbers = [line.strip() for line in open('data.txt')]
    print('Part 1', solve_1())
    print('Part 2', solve_2())
