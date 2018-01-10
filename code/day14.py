'''
@author: Nick DeMasi

Code to complete Day 14 of 2017 Advent of
Code using Python 3

'''


import os

from day10 import KnotHash


ABS_PATH = 'C://Users/ldema/Coding/python_projects/adventofcode2017'

hex_to_bin = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'a': '1010',
    'b': '1011',
    'c': '1100',
    'd': '1101',
    'e': '1110',
    'f': '1111'
}

class KnotGraph(object):
    def __init__(self, key):
        self.grid = self.__load(key)

    def contiguous_groups(self):
        used = self.used()

        def f(c, used):
            adjacent = self.__adjacent(c)
            for a in adjacent:
                if a in used:
                    used.remove(a)
                    f(a, used)

        for c in used:
            used.remove(c)
            f(c, used)

        return len(used)

    def used(self):
        '''Counts number of used spaces in Knot Graph'''

        used = 0

        for row in self.grid:
            for c in row:
                if c == '1':
                    used += 1

        return used

    def __adjacent(self, coordinate):
        '''Finds all adjacent coordinates'''

        adjacent = []
        adjacent.append((coordinate[0] - 1, coordinate[1]))
        adjacent.append((coordinate[0] + 1, coordinate[1]))
        adjacent.append((coordinate[0], coordinate[1] - 1))
        adjacent.append((coordinate[0], coordinate[1] + 1))

        return adjacent

    def __load(self, s):
        '''Creates a 128x128 grid of 0s and 1s using knot hashes'''

        # instantiate KnotHash object
        kh = KnotHash()
        # create empty list to hold grid
        grid = []

        # perform row creation method 128 times
        for i in range(128):
            # reset KnotHash
            kh.reset()

            # create empty list to hold row
            binary_string = []

            # create key
            key = '{}-{}'.format(s, i)

            # create knot hash from key
            knot_hash = kh.create_hash(key)

            # iterate through chars in knot hash and convert to binay
            for c in knot_hash:
                binary_string.append(hex_to_bin[c])

            # append row to grid
            grid.append(''.join(binary_string))

        return grid


if __name__ == '__main__':
    # instantiate KnotGraph
    graph = KnotGraph('ljoxqyyw')

    # count number of used spaces for part 1
    print("Part 1:           ", graph.used())

    contiguous_groups = grid.contiguous_groups()
    print("Part 2:           ", contiguous_groups)
