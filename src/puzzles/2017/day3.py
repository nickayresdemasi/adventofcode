'''
@author: Nick DeMasi

Code to complete Part 2 of Day 3 of
2017 Advent of Code using Python 3

'''

import sys


class  SpiralGraph(object):
    def __init__(self):
        self.grid = {}

    def build_graph(self, num):
        '''Constructs a sprial graph in counterclockwise direction.

        INPUT:
            - num (int):    number at which to stop graph building
        '''
        self.grid[(0, 0)] = 1
        x, y = 1, 0
        self.grid[(x, y)] = 1
        while True:
            while x != y:
                y += 1
                self.grid[(x, y)] = self.__calculate_value(x, y)
                if self.grid[(x, y)] > num:
                    print(self.grid[x, y])
                    sys.exit()
            while -x != y:
                x -= 1
                self.grid[(x, y)] = self.__calculate_value(x, y)
                if self.grid[(x, y)] > num:
                    print(self.grid[x, y])
                    sys.exit()
            while x != y:
                y -= 1
                self.grid[(x, y)] = self.__calculate_value(x, y)
                if self.grid[(x, y)] > num:
                    print(self.grid[x, y])
                    sys.exit()
            while -x != y:
                x += 1
                self.grid[(x, y)] = self.__calculate_value(x, y)
                if self.grid[(x, y)] > num:
                    print(self.grid[x, y])
                    sys.exit()

            x += 1
            self.grid[(x, y)] = self.__calculate_value(x, y)
            if self.grid[(x, y)] > num:
                print(self.grid[x, y])
                sys.exit()


    def __calculate_value(self, x, y):
        '''Calculates next value in Spiral Graph by adding up adding up all
        adjacent existing values'''
        num = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                coordinates = (x - i, y - j)
                if coordinates in self.grid.keys():
                    num += self.grid[coordinates]
        return num

if __name__ == '__main__':
    sg = SpiralGraph()
    sg.build_graph(361527)
