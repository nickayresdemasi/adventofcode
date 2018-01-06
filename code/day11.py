'''
@author: Nick DeMasi

Code to complete Day 11 of 2017 Advent of
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

    def step(self, direction):
        '''Evaluates a direction in a hexagrid and updates register of steps'''
        if direction == 'nw':
            # look for presence of direct opposite
            if self.map['se'] > 0:
                self.map['se'] -= 1

            # look for presence of combination movements
            elif self.map['s'] > 0:
                self.map['s'] -= 1
                self.step('sw')
            elif self.map['ne'] > 0:
                self.map['ne'] -= 1
                self.step('n')

            # increase step in direction by 1
            else:
                self.map['nw'] += 1

        # repeate above process for all directions
        elif direction == 'n':
            # direct opposite
            if self.map['s'] > 0:
                self.map['s'] -= 1

            # combos
            elif self.map['sw'] > 0:
                self.map['sw'] -= 1
                self.step('nw')
            elif self.map['se'] > 0:
                self.map['se'] -= 1
                self.step('ne')

            else:
                self.map['n'] += 1

        elif direction == 'ne':
            # direct opposite
            if self.map['sw'] > 0:
                self.map['sw'] -= 1

            # combos
            elif self.map['s'] > 0:
                self.map['s'] -= 1
                self.step('se')
            elif self.map['nw'] > 0:
                self.map['nw'] -= 1
                self.step('n')


            else:
                self.map['ne'] += 1

        elif direction == 'se':
            # direct opposite
            if self.map['nw'] > 0:
                self.map['nw'] -= 1

            # combos
            elif self.map['sw'] > 0:
                self.map['sw'] -= 1
                self.step('s')
            elif self.map['n'] > 0:
                self.map['n'] -= 1
                self.step('ne')

            else:
                self.map['se'] += 1

        elif direction == 's':
            # direct opposite
            if self.map['n'] > 0:
                self.map['n'] -= 1

            # combos
            elif self.map['nw'] > 0:
                self.map['nw'] -= 1
                self.step('sw')
            elif self.map['ne'] > 0:
                self.map['ne'] -= 1
                self.step('se')

            else:
                self.map['s'] += 1

        elif direction == 'sw':
            # direct opposite
            if self.map['ne'] > 0:
                self.map['ne'] -= 1

            # combos
            elif self.map['se'] > 0:
                self.map['se'] -= 1
                self.step('s')
            elif self.map['n'] > 0:
                self.map['n'] -= 1
                self.step('nw')

            else:
                self.map['sw'] += 1

    def count_steps(self):
        '''Counts how many steps away from center current position is'''
        steps = 0
        for v in self.map.values():
            steps += v

        return steps

if __name__ == '__main__':
    path = os.path.join(ABS_PATH, 'input/day11.txt')
    file = open(path, 'r')
    directions = file.read().split(',')

    # instantiate hexgrid
    hg = HexGrid()

    # count total number of steps needed to get to final position
    # also collect data to find max number of steps away

    max_steps = 0
    for d in directions:
        hg.step(d)

        # get current steps away
        steps_away = hg.count_steps()

        # adjust max if greater
        if steps_away > max_steps:
            max_steps = steps_away

    print("Part 1:          ", hg.count_steps())
    print("Part 2:          ", max_steps)
