'''
@author: Nick DeMasi

Code to complete Day 22 of 2017 Advent of
Code using Python 3

'''


import os


ABS_PATH = 'C://Users/ldema/Coding/python_projects/adventofcode2017'


class Virus(object):
    LEFTS = {
       'n': 'w',
       'e': 'n',
       's': 'e',
       'w': 's'
    }

    RIGHTS = {
        'n': 'e',
        'e': 's',
        's': 'w',
        'w': 'n'
    }

    def __init__(self, v_map):
        self.map = v_map
        self.pos = (12, 12)
        self.direction = 'n'

    def clean(self):
        '''Cleans a node if previously infected'''
        self.map[self.pos] = '.'

    def flag(self):
        '''Flags a node that is infected'''
        self.map[self.pos] = 'F'

    def get_node(self):
        '''Returns the value of the node at the current position'''
        if self.pos not in self.map.keys():
            self.map[self.pos] = '.'
        return self.map[self.pos]

    def infect(self):
        '''Infects the current node if previously uninfected'''
        self.map[self.pos] = '#'

    def move(self):
        '''Moves forward one space in indicated direction'''
        if self.direction == 'n':
            self.pos = (self.pos[0], self.pos[1] + 1)
        elif self.direction == 'e':
            self.pos = (self.pos[0] + 1, self.pos[1])
        elif self.direction == 's':
            self.pos = (self.pos[0], self.pos[1] - 1)
        elif self.direction == 'w':
            self.pos = (self.pos[0] - 1, self.pos[1])

    def reverse(self):
        '''Reverses the direction of the virus'''
        self.direction = self.RIGHTS[self.RIGHTS[self.direction]]

    def turn(self, direction):
        '''turns right or left and moves one depending on value of
        current node'''
        if direction == 'l':
            self.direction = self.LEFTS[self.direction]
        elif direction == 'r':
            self.direction = self.RIGHTS[self.direction]

    def weaken(self):
        '''Weakens a clean node'''
        self.map[self.pos] = 'W'


if __name__ == '__main__':
    # read in puzzle input
    path = os.path.join(ABS_PATH, 'input/day22.txt')
    file = open(path, 'r')
    grid = [[c for c in line] for line in file.read().split('\n')]

    # convert grid to dictionary
    v_map = {}
    for i, row in enumerate(grid[::-1]):
        for j, node in enumerate(row):
            v_map[(j, i)] = node

    # instantiate Virus object
    v = Virus(v_map)

    # count infections over 10000 steps
    infections = 0
    for i in range(10000):
        if v.get_node() == '#':
            v.turn('r')
            v.clean()
        elif v.get_node() == '.':
            v.turn('l')
            v.infect()
            infections += 1
        v.move()

    print("Part 1:           %d" % infections)

    # reset infinite grid for part 2
    v_map = {}
    for i, row in enumerate(grid[::-1]):
        for j, node in enumerate(row):
            v_map[(j, i)] = node

    # count infections over 10000000 steps
    v = Virus(v_map)
    infections = 0
    for i in range(10000000):
        node = v.get_node()
        if node == '#':
            v.turn('r')
            v.flag()
        elif node == 'F':
            v.reverse()
            v.clean()
        elif node == '.':
            v.turn('l')
            v.weaken()
        elif node == 'W':
            v.infect()
            infections += 1
        v.move()


    print("Part 2:           %d" % infections)
