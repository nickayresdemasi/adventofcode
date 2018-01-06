'''
@author: Nick DeMasi

Code to complete Day 10 of 2017 Advent of
Code using Python 3

'''


import os


ABS_PATH = 'C://Users/ldema/Coding/python_projects/adventofcode2017'


class HexGrid(object):
    def __init__(self):
        self.map = {
            'nw': 0,
            'n':  0,
            'ne': 0,
            'se': 0,
            's':  0,
            'sw': 0
        }
        self.steps = 0

    def step(self, direction):
        '''Evaluates a direction in a hexagrid and updates register of steps'''
        if direction == 'nw':
            if self.map['se'] > 0:
                self.map['se'] -= 1
            else:
                self.map['nw'] += 1
        elif direction == 'n':
            if self.map['s'] > 0:
                self.map['s'] -= 1
            else:
                self.map['n'] += 1
        elif direction == 'ne':
            if self.map['sw'] > 0:
                self.map['sw'] -= 1
            else:
                self.map['ne'] += 1
        elif direction == 'se':
            if self.map['nw'] > 0:
                self.map['nw'] -= 1
            else:
                self.map['se'] += 1
        elif direction == 's':
            if self.map['n'] > 0:
                self.map['n'] -= 1
            else:
                self.map['s'] += 1
        elif direction == 'sw':
            if self.map['ne'] > 0:
                self.map['ne'] -= 1
            else:
                self.map['sw'] += 1

    def reduce_map(self):
        for k in self.map.keys():
            if self.map[k] == 0:
                continue

            if k == 'nw':
                if self.map[k] <= self.map['s'] or self.map[k] <= self.map['se']:
                    continue
            elif k == 'n':
                if self.map[k] <= self.map['sw'] or self.map[k] <= self.map['se']:
                    continue
            elif k == 'ne':
                if self.map[k] <= self.map['s'] or self.map[k] <= self.map['nw']:
                    continue
            elif k == 'se':
                if self.map[k] <= self.map['n'] or self.map[k] <= self.map['sw']:
                    continue
            elif k == 's':
                if self.map[k] <= self.map['ne'] or self.map[k] <= self.map['nw']:
                    continue
            elif k == 'sw':
                if self.map[k] <= self.map['n'] or self.map[k] <= self.map['se']:
                    continue

            self.steps += self.map[k]

if __name__ == '__main__':
    path = os.path.join(ABS_PATH, 'input/day11.txt')
    file = open(path, 'r')
    directions = file.read().split(',')

    # instantiate hexgrid
    hg = HexGrid()

    # count total number of steps needed to get to final position
    for d in directions:
        hg.step(d)

    hg.reduce_map()

    print(hg.map)
    print("Part 1:          ", hg.steps)
