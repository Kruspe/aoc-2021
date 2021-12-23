from copy import deepcopy
from dataclasses import dataclass

import numpy as np


class RangedInstruction:
    def __init__(self, state, coordinates):
        self.state = state
        self.__transform_ranges__(coordinates)
        self.x = coordinates['x']
        self.y = coordinates['y']
        self.z = coordinates['z']

    @staticmethod
    def __transform_ranges__(coordinates):
        if coordinates['x'][0] < -50:
            coordinates['x'][0] = -50
        if coordinates['y'][0] < -50:
            coordinates['y'][0] = -50
        if coordinates['z'][0] < -50:
            coordinates['z'][0] = -50
        if coordinates['x'][1] > 50:
            coordinates['x'][1] = 49
        if coordinates['y'][1] > 50:
            coordinates['y'][1] = 49
        if coordinates['z'][1] > 50:
            coordinates['z'][1] = 49

    def transforms_in_range(self):
        if self.x[0] > 50 or self.y[0] > 50 or self.z[0] > 50:
            return False
        if self.x[1] < -50 or self.y[1] < -50 or self.z[1] < -50:
            return False

        return True


class Instruction:
    def __init__(self, state, coordinates):
        self.state = state
        self.box = Box(coordinates['x'][0], coordinates['x'][1] + 1,
                       coordinates['y'][0], coordinates['y'][1] + 1,
                       coordinates['z'][0], coordinates['z'][1] + 1)


@dataclass(frozen=True)
class Box:
    x1: int
    x2: int
    y1: int
    y2: int
    z1: int
    z2: int

    def count(self):
        return abs(self.x1 - self.x2) * abs(self.y1 - self.y2) * abs(self.z1 - self.z2)

    def get_overlap(self, b):
        if not (self.x1 < b.x2 and self.x2 > b.x1
                and self.y1 < b.y2 and self.y2 > b.y1
                and self.z1 < b.z2 and self.z2 > b.z1):
            yield self
        else:
            b = Box(min(max(b.x1, self.x1), self.x2), min(max(b.x2, self.x1), self.x2),
                    min(max(b.y1, self.y1), self.y2), min(max(b.y2, self.y1), self.y2),
                    min(max(b.z1, self.z1), self.z2), min(max(b.z2, self.z1), self.z2))

            yield Box(self.x1, b.x1, self.y1, self.y2, self.z1, self.z2)
            yield Box(b.x2, self.x2, self.y1, self.y2, self.z1, self.z2)
            yield Box(b.x1, b.x2, self.y1, b.y1, self.z1, self.z2)
            yield Box(b.x1, b.x2, b.y2, self.y2, self.z1, self.z2)
            yield Box(b.x1, b.x2, b.y1, b.y2, self.z1, b.z1)
            yield Box(b.x1, b.x2, b.y1, b.y2, b.z2, self.z2)


def solve_1(instructions: list[RangedInstruction]):
    core = np.zeros((101, 101, 101), dtype=int)
    for i in instructions:
        if i.transforms_in_range():
            for x in range(i.x[0], i.x[1] + 1):
                for y in range(i.y[0], i.y[1] + 1):
                    for z in range(i.z[0], i.z[1] + 1):
                        if i.state == 'on':
                            core[x, y, z] = 1
                        else:
                            core[x, y, z] = 0

    return len(np.where(core == 1)[0])


def solve_2(instructions: list[Instruction]):
    boxes = []
    for i in instructions:
        cuboid = i.box
        boxes = [child for other in boxes
                 for child in other.get_overlap(cuboid)
                 if child.count() > 0]
        if i.state == 'on':
            boxes.append(cuboid)

    return sum(box.count() for box in boxes)


def parse(data):
    ranged: list[RangedInstruction] = []
    i: list[Instruction] = []
    for line in data:
        state, cuboid = line.split(' ')
        m = {}
        for c in cuboid.split(','):
            split_coord = c.split('=')
            m[split_coord[0]] = list(map(lambda x: int(x), split_coord[-1].split('..')))
        i.append(Instruction(state, deepcopy(m)))
        ranged.append(RangedInstruction(state, deepcopy(m)))

    return ranged, i


if __name__ == '__main__':
    rangedInstructions, allInstructions = parse([line.strip() for line in open('data.txt')])
    print('Part 1', solve_1(rangedInstructions))
    print('Part 2', solve_2(allInstructions))
