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
        '''Counts the number of contiguous groups in grid'''

        groups = 0
        visited = []

        for i in range(128):
            for j in range(128):
                if (i, j) in visited:
                    continue
                if not self.grid[i][j]:
                    continue
                self.__dfs((i, j), visited)
                groups += 1

        return groups

    def used(self):
        '''Counts number of used spaces in Knot Graph'''

        used = 0

        for row in self.grid:
            used += sum(row)

        return used

    def __adjacent(self, coordinate):
        '''Finds all adjacent nodes to coordinate in KnotGraph'''

        adjacent = []

        if coordinate[0] > 0:
            adjacent.append((coordinate[0] - 1, coordinate[1]))
        if coordinate[1] > 0:
            adjacent.append((coordinate[0], coordinate[1] - 1))
        if coordinate[0] < 127:
            adjacent.append((coordinate[0] + 1, coordinate[1]))
        if coordinate[1] < 127:
            adjacent.append((coordinate[0], coordinate[1] + 1))

        return adjacent

    def __dfs(self, coordinate, visited):
        '''Performs a depth-first search on a node in a graph'''

        if coordinate in visited:
            return

        if not self.grid[coordinate[0]][coordinate[1]]:
            return

        visited.append(coordinate)
        for child in self.__adjacent(coordinate):
            self.__dfs(child, visited)


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

            # create knot hash from key
            knot_hash = kh.create_hash('%s-%d' % (s, i))

            # iterate through chars in knot hash and convert to binay
            for c in knot_hash:
                binary_string.append(hex_to_bin[c])

            # append row to grid
            grid.append(list(map(int, ''.join(binary_string))))

        return grid


if __name__ == '__main__':
    # instantiate KnotGraph
    graph = KnotGraph('ljoxqyyw')

    # count number of used spaces for part 1
    print("Part 1:           ", graph.used())

    # count number of contiguous groups
    print("Part 2:           ", graph.contiguous_groups())
