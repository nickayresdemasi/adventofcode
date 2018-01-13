'''
@author: Nick DeMasi

Code to complete Day 18 of 2017 Advent of
Code using Python 3

'''


import os
import string


ABS_PATH = 'C://Users/ldema/Coding/python_projects/adventofcode2017'


class PacketMap(object):
    OPPOSITES = {
        'n': 's',
        'e': 'w',
        's': 'n',
        'w': 'e'
    }

    def __init__(self, map_path):
        self.direction = 's'
        self.map = map_path[::-1]
        self.pos = self.__find_start()

    def get_path(self, pos=None):
        '''Returns current path type'''
        if pos:
            return self.map[pos[1]][pos[0]]
        return self.map[self.pos[1]][self.pos[0]]

    def move(self):
        '''Move depending on direction'''
        if self.direction == 'n':
            self.pos = (self.pos[0], self.pos[1] + 1)
        elif self.direction == 'e':
            self.pos = (self.pos[0] + 1, self.pos[1])
        elif self.direction == 's':
            self.pos = (self.pos[0], self.pos[1] - 1)
        elif self.direction == 'w':
            self.pos = (self.pos[0] - 1, self.pos[1])

    def reroute(self):
        '''Changes the direction'''
        adjacent = self.__adjacent()

        for k in adjacent.keys():
            # check that direction is not the same as current or oppostie
            if k == self.direction or k == self.OPPOSITES[self.direction]:
                continue
            map_path = self.get_path(adjacent[k])
            if map_path == '-' or map_path == '|':
                self.direction = k
                break

    def __adjacent(self):
        '''Returns a hash map of adjacent moves and their directions'''
        adjacent = {}

        adjacent['n'] = (self.pos[0], self.pos[1] + 1)
        adjacent['e'] = (self.pos[0] + 1, self.pos[1])
        adjacent['s'] = (self.pos[0], self.pos[1] - 1)
        adjacent['w'] = (self.pos[0] - 1, self.pos[1])

        return adjacent

    def __find_start(self):
        for i, path in enumerate(self.map[len(self.map) - 1]):
            if path == '|':
                return (i, len(self.map) - 1)


if __name__ == '__main__':
    # load puzzle input
    path = os.path.join(ABS_PATH, 'input/day19.txt')
    file = open(path, 'r')
    text = file.read().split('\n')

    # instantiate PacketMap
    pm = PacketMap(text)

    # manuver through map while logging letters
    letters = []
    steps = 0
    while True:
        map_path = pm.get_path()
        if map_path == '|' or map_path == '-':
            pm.move()
            steps += 1
        elif map_path == '+':
            pm.reroute()
            pm.move()
            steps += 1
        elif map_path in string.ascii_uppercase:
            letters.append(map_path)
            pm.move()
            steps += 1
        else:
            break

    print("Part 1:               %s" % "".join(letters))
    print("Part 2:               %d" % steps)
